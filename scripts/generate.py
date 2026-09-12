#!/usr/bin/env python3
"""Unciv Wiki 数据管道。

从本地 Unciv4iOS 源码提取 Gods & Kings 规则集数据 + 成就数据，
复刻 Unciv 的翻译引擎（tr() / getPlaceholderText / getPlaceholderParameters），
JOIN 简体中文翻译，输出中英双语 Starlight 文档页面。

用法:
    python3 scripts/generate.py
"""
import json
import re
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 路径
# ---------------------------------------------------------------------------
BLOG_ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path("/Users/ai/code/Unciv4iOS-Private/public/Unciv4iOS/android/assets/jsons")
GK = SOURCE / "Civ V - Gods & Kings"
TRANSLATIONS = SOURCE / "translations"
ACHIEVEMENTS = Path("/Users/ai/code/Unciv4iOS-Private/assets/achievements")

OUT_DOCS = BLOG_ROOT / "src" / "content" / "docs"
OUT_EN_DB = OUT_DOCS / "database"
OUT_ZH_DB = OUT_DOCS / "zh" / "database"
OUT_ACH = OUT_DOCS / "achievements"
OUT_ZH_ACH = OUT_DOCS / "zh" / "achievements"
OUT_PUBLIC = BLOG_ROOT / "public"

GAME_VERSION = "4.21.19"


# ---------------------------------------------------------------------------
# 容错 JSON 解析（剥离 // 与 /* */ 注释）
# ---------------------------------------------------------------------------
def strip_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"//[^\n]*", "", text)
    return text


def load_json(path: Path):
    return json.loads(strip_comments(path.read_text(encoding="utf-8")))


# ---------------------------------------------------------------------------
# 翻译引擎（复刻 Unciv 的 Translations / tr()）
# ---------------------------------------------------------------------------
POINTY_RE = re.compile(r"<([^>]*)>")
SQUARE_RE = re.compile(r"\[([^\]]*)\]")


def remove_conditionals(s: str) -> str:
    if "<" not in s:
        return s
    return POINTY_RE.sub("", s).replace("  ", " ").strip()


def get_placeholder_params(s: str) -> list[str]:
    s2 = remove_conditionals(s)
    params: list[str] = []
    depth = 0
    start = -1
    for i, c in enumerate(s2):
        if c == "[":
            if depth == 0:
                start = i + 1
            depth += 1
        elif c == "]" and depth > 0:
            depth -= 1
            if depth == 0:
                params.append(s2[start:i])
    return params


def get_placeholder_text(s: str) -> str:
    out = remove_conditionals(s)
    for p in get_placeholder_params(s):
        out = out.replace(f"[{p}]", "[]", 1)
    return out


def load_props(path: Path) -> dict[str, str]:
    """读取 .properties，返回 {key: value}。跳过注释与空值。"""
    d: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.rstrip("\n")
        if not line or line.startswith("#") or " = " not in line:
            continue
        k, v = line.split(" = ", 1)
        if v.strip() == "":
            continue
        # Unciv 把 \n 还原为换行
        d[k.replace("\\n", "\n")] = v.replace("\\n", "\n")
    return d


class Translator:
    """复刻 Unciv 翻译查找：key 若含 [ 且不含 <，则做 getPlaceholderText。"""

    def __init__(self, zh_path: Path):
        raw = load_props(zh_path)
        self.table: dict[str, str] = {}
        for k, v in raw.items():
            if "[" in k and "<" not in k:
                self.table[get_placeholder_text(k)] = v
            else:
                self.table[k] = v

    def translate(self, text: str) -> str:
        """翻译一段文本（含占位符回填）。找不到则回退英文原文。"""
        if not text:
            return text
        # 1) 无括号：直接查表
        if "[" not in text and "<" not in text:
            return self.table.get(text, text)

        # 2) 含条件 <...>：分别翻译基础部分与各条件，再按中文规则拼接
        #    中文 ConditionalsPlacement = "before"：条件在前，基础在后
        if "<" in text:
            base = remove_conditionals(text)
            conds = POINTY_RE.findall(text)
            base_tr = self._translate_plain(base)
            cond_trs = [self._translate_plain(c) for c in conds]
            # 中文：条件在前
            parts = cond_trs + [base_tr]
            return "".join(parts)

        # 3) 含 [ 不含 <：占位符翻译
        return self._translate_plain(text)

    def _translate_plain(self, text: str) -> str:
        """翻译不含 <条件> 的文本，处理 [占位符] 回填。"""
        if not text:
            return text
        if "[" not in text:
            return self.table.get(text, text)

        params = get_placeholder_params(text)
        key = get_placeholder_text(text)
        if key in self.table:
            template = self.table[key]
        else:
            # 回退：直接用原文（去掉条件后的）
            return text

        # 回填：template 里的 [xxx] 依次替换为 params 的翻译
        # 但中文 template 用的是类型名占位符（如 [mapUnitFilter]），需按顺序回填
        # Unciv 的做法：template 的占位符按 originalEntry 的参数顺序替换
        # 这里简化：把 template 里的每个 [typeParam] 按顺序替换为对应 params 的翻译
        tpl_params = get_placeholder_params(template)
        if len(tpl_params) == len(params):
            result = template
            for tpl_p, p in zip(tpl_params, params):
                # 翻译参数本身（参数可能是规则对象名，需要翻译）
                p_tr = self.table.get(p, p)
                # 处理参数内嵌套的 {Military} {Water} 这类
                p_tr = self._expand_filters(p_tr)
                result = result.replace(f"[{tpl_p}]", p_tr, 1)
            return result
        return template

    def _expand_filters(self, p: str) -> str:
        """展开 {A} {B} 过滤器为可读形式（如 {Military} {Water} -> 军事 海上）。"""
        def repl(m):
            inner = m.group(1)
            parts = [self.table.get(x, x) for x in inner.split()]
            return " ".join(parts)
        return re.sub(r"\{([^}]*)\}", repl, p)


zh_translator = Translator(TRANSLATIONS / "Simplified_Chinese.properties")


def tr(text: str) -> str:
    return zh_translator.translate(text)


# ---------------------------------------------------------------------------
# 数据提取
# ---------------------------------------------------------------------------
def extract_nations():
    data = load_json(GK / "Nations.json")
    majors, city_states = [], []
    for n in data:
        if n.get("cityStateType"):
            city_states.append(n)
        elif n.get("leaderName"):
            majors.append(n)
        # Spectator / Barbarians 跳过
    return majors, city_states


def extract_units():
    return load_json(GK / "Units.json")


def extract_buildings():
    return load_json(GK / "Buildings.json")


def extract_techs():
    data = load_json(GK / "Techs.json")
    techs = []
    for era in data:
        for t in era.get("techs", []):
            t["era"] = era.get("era", "")
            techs.append(t)
    return techs


# ---------------------------------------------------------------------------
# 格式化辅助
# ---------------------------------------------------------------------------
def md_escape(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def uniques_list(uniques) -> str:
    """把 uniques 列表转成 Markdown 列表（英文原文，忠实呈现游戏规则语法）。"""
    if not uniques:
        return ""
    # 用反引号包裹，避免 <...> 被当作 HTML、[...] 被当作链接语法
    return "\n".join(f"- `{u}`" for u in uniques)


# ---------------------------------------------------------------------------
# 页面生成
# ---------------------------------------------------------------------------
def write_page(path: Path, frontmatter: dict, body: str):
    fm_lines = ["---"]
    for k, v in frontmatter.items():
        if isinstance(v, str):
            # 冒号需转义，避免 YAML 解析错误
            v = v.replace(": ", "：")
            fm_lines.append(f"{k}: {v}")
        elif isinstance(v, list):
            fm_lines.append(f"{k}:")
            for item in v:
                fm_lines.append(f"  - {item}")
        elif isinstance(v, bool):
            fm_lines.append(f"{k}: {'true' if v else 'false'}")
        elif v is None:
            continue
        else:
            fm_lines.append(f"{k}: {v}")
    fm_lines.append("---")
    fm_lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(fm_lines) + body + "\n", encoding="utf-8")


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    return s


def gen_nations():
    majors, city_states = extract_nations()
    # 英文聚合页
    rows = []
    for n in majors:
        name = n["name"]
        leader = n.get("leaderName", "")
        unique = n.get("uniqueName", "")
        victory = n.get("preferredVictoryType", "")
        rows.append(
            f"| [{name}](./{slugify(name)}/) | {leader} | {unique} | {victory} |"
        )
    table = "\n".join(
        [
            "| Civilization | Leader | Unique Ability | Preferred Victory |",
            "| --- | --- | --- | --- |",
            *rows,
        ]
    )
    body = f"""# Civilizations

{table}

## City-States

"""
    cs_rows = []
    for cs in city_states:
        name = cs["name"]
        cstype = cs.get("cityStateType", "")
        personality = cs.get("personality", "")
        cs_rows.append(f"| {name} | {tr(cstype)} | {tr(personality)} |")
    cs_table = "\n".join(
        [
            "| City-State | Type | Personality |",
            "| --- | --- | --- |",
            *cs_rows,
        ]
    )
    body += cs_table + "\n"
    write_page(
        OUT_EN_DB / "civilizations" / "index.md",
        {"title": "Civilizations", "description": "All civilizations and city-states in Unciv."},
        body,
    )
    # 中文聚合页
    zh_rows = []
    for n in majors:
        name = tr(n["name"])
        leader = tr(n.get("leaderName", ""))
        unique = tr(n.get("uniqueName", ""))
        victory = tr(n.get("preferredVictoryType", ""))
        zh_rows.append(
            f"| [{name}](./{slugify(n['name'])}/) | {leader} | {unique} | {victory} |"
        )
    zh_table = "\n".join(
        [
            "| 文明 | 领袖 | 独特能力 | 偏好胜利 |",
            "| --- | --- | --- | --- |",
            *zh_rows,
        ]
    )
    zh_body = f"""# 文明

{zh_table}

## 城邦

"""
    zh_cs_rows = []
    for cs in city_states:
        name = tr(cs["name"])
        cstype = tr(cs.get("cityStateType", ""))
        personality = tr(cs.get("personality", ""))
        zh_cs_rows.append(f"| {name} | {cstype} | {personality} |")
    zh_cs_table = "\n".join(
        [
            "| 城邦 | 类型 | 性格 |",
            "| --- | --- | --- |",
            *zh_cs_rows,
        ]
    )
    zh_body += zh_cs_table + "\n"
    write_page(
        OUT_ZH_DB / "civilizations" / "index.md",
        {"title": "文明", "description": "Unciv 的全部文明与城邦。"},
        zh_body,
    )
    # 实体独立页（主要文明，全量）
    for n in majors:
        gen_nation_page(n)


def gen_nation_page(n):
    name = n["name"]
    slug = slugify(name)
    leader = n.get("leaderName", "")
    # 英文
    fm = {"title": name, "description": f"{name} — leader, unique ability and start bias in Unciv."}
    body = f"""# {name}

**Leader**: {leader}

**Unique Ability**: {n.get('uniqueName', '')}

"""
    if n.get("uniques"):
        body += "## Unique Abilities\n\n" + uniques_list(n["uniques"]) + "\n\n"
    if n.get("startBias"):
        body += "## Start Bias\n\n" + "\n".join(f"- {b}" for b in n["startBias"]) + "\n\n"
    if n.get("preferredVictoryType"):
        body += f"**Preferred Victory**: {n['preferredVictoryType']}\n\n"
    write_page(OUT_EN_DB / "civilizations" / slug / "index.md", fm, body)
    # 中文
    zh_name = tr(name)
    zh_fm = {"title": zh_name, "description": f"{zh_name}——领袖、独特能力与开局倾向。"}
    zh_body = f"""# {zh_name}

**领袖**：{tr(leader)}

**独特能力**：{tr(n.get('uniqueName', ''))}

"""
    if n.get("uniques"):
        zh_body += "## 独特能力\n\n"
        for u in n["uniques"]:
            zh_body += f"- {tr(u)}\n"
        zh_body += "\n"
    if n.get("startBias"):
        zh_body += "## 开局倾向\n\n" + "\n".join(f"- {tr(b)}" for b in n["startBias"]) + "\n\n"
    write_page(OUT_ZH_DB / "civilizations" / slug / "index.md", zh_fm, zh_body)


def gen_units():
    units = extract_units()
    # 英文聚合
    rows = []
    for u in units:
        name = u["name"]
        utype = u.get("unitType", "")
        cost = u.get("cost", "")
        tech = u.get("requiredTech", "")
        rows.append(
            f"| [{name}](./{slugify(name)}/) | {tr(utype)} | {cost} | [{tech}](../technologies/{slugify(tech)}/) |"
        )
    table = "\n".join(
        [
            "| Unit | Type | Cost | Required Tech |",
            "| --- | --- | --- | --- |",
            *rows,
        ]
    )
    body = f"# Units\n\n{table}\n"
    write_page(
        OUT_EN_DB / "units" / "index.md",
        {"title": "Units", "description": "All units in Unciv — type, cost and required technology."},
        body,
    )
    # 中文聚合
    zh_rows = []
    for u in units:
        name = tr(u["name"])
        utype = tr(u.get("unitType", ""))
        cost = u.get("cost", "")
        tech = tr(u.get("requiredTech", ""))
        zh_rows.append(
            f"| [{name}](./{slugify(u['name'])}/) | {utype} | {cost} | [{tech}](../technologies/{slugify(u.get('requiredTech',''))}/) |"
        )
    zh_table = "\n".join(
        [
            "| 单位 | 类型 | 造价 | 所需科技 |",
            "| --- | --- | --- | --- |",
            *zh_rows,
        ]
    )
    zh_body = f"# 单位\n\n{zh_table}\n"
    write_page(
        OUT_ZH_DB / "units" / "index.md",
        {"title": "单位", "description": "Unciv 的全部单位——类型、造价与所需科技。"},
        zh_body,
    )
    # 实体独立页（全量）
    for u in units:
        gen_unit_page(u)


def gen_unit_page(u):
    name = u["name"]
    slug = slugify(name)
    # 英文
    fm = {"title": name, "description": f"{name} — stats, abilities and tech requirements in Unciv."}
    body = f"# {name}\n\n"
    stat_rows = []
    label_map = {
        "unitType": "Type",
        "movement": "Movement",
        "strength": "Strength",
        "rangedStrength": "Ranged Strength",
        "range": "Range",
        "cost": "Cost",
        "requiredTech": "Required Tech",
        "obsoleteTech": "Obsolete Tech",
        "upgradesTo": "Upgrades To",
        "requiredResource": "Required Resource",
        "replaces": "Replaces",
        "uniqueTo": "Unique To",
    }
    for key, label in label_map.items():
        if key in u and u[key] not in (None, "", []):
            stat_rows.append(f"| {label} | {u[key]} |")
    if stat_rows:
        body += "## Stats\n\n" + "\n".join(
            ["| Attribute | Value |", "| --- | --- |", *stat_rows]
        ) + "\n\n"
    if u.get("uniques"):
        body += "## Abilities\n\n" + uniques_list(u["uniques"]) + "\n\n"
    if u.get("promotions"):
        body += "## Promotions\n\n" + "\n".join(f"- {p}" for p in u["promotions"]) + "\n\n"
    if u.get("civilopediaText"):
        text = u["civilopediaText"][0].get("text", "") if u["civilopediaText"] else ""
        if text:
            body += f"## Civilopedia\n\n{text}\n\n"
    write_page(OUT_EN_DB / "units" / slug / "index.md", fm, body)
    # 中文
    zh_name = tr(name)
    zh_fm = {"title": zh_name, "description": f"{zh_name}——属性、能力与科技需求。"}
    zh_body = f"# {zh_name}\n\n"
    zh_label_map = {
        "unitType": "类型",
        "movement": "移动力",
        "strength": "战斗力",
        "rangedStrength": "远程战斗力",
        "range": "射程",
        "cost": "造价",
        "requiredTech": "所需科技",
        "obsoleteTech": "淘汰科技",
        "upgradesTo": "升级为",
        "requiredResource": "所需资源",
        "replaces": "替代",
        "uniqueTo": "专属文明",
    }
    zh_stat_rows = []
    for key, label in zh_label_map.items():
        if key in u and u[key] not in (None, "", []):
            val = u[key]
            if key in ("requiredTech", "obsoleteTech", "upgradesTo", "replaces", "uniqueTo"):
                val = tr(val)
            zh_stat_rows.append(f"| {label} | {val} |")
    if zh_stat_rows:
        zh_body += "## 属性\n\n" + "\n".join(
            ["| 属性 | 数值 |", "| --- | --- |", *zh_stat_rows]
        ) + "\n\n"
    if u.get("uniques"):
        zh_body += "## 能力\n\n"
        for x in u["uniques"]:
            zh_body += f"- {tr(x)}\n"
        zh_body += "\n"
    if u.get("promotions"):
        zh_body += "## 晋升\n\n" + "\n".join(f"- {tr(p)}" for p in u["promotions"]) + "\n\n"
    write_page(OUT_ZH_DB / "units" / slug / "index.md", zh_fm, zh_body)


def gen_buildings():
    buildings = extract_buildings()
    # 英文聚合
    rows = []
    for b in buildings:
        name = b["name"]
        cost = b.get("cost", "")
        tech = b.get("requiredTech", "")
        kind = "Wonder" if b.get("isWonder") else ("National Wonder" if b.get("isNationalWonder") else "")
        rows.append(
            f"| [{name}](./{slugify(name)}/) | {kind} | {cost} | {tech or '—'} |"
        )
    table = "\n".join(
        [
            "| Building | Type | Cost | Required Tech |",
            "| --- | --- | --- | --- |",
            *rows,
        ]
    )
    body = f"# Buildings\n\n{table}\n"
    write_page(
        OUT_EN_DB / "buildings" / "index.md",
        {"title": "Buildings", "description": "All buildings, wonders and national wonders in Unciv."},
        body,
    )
    # 中文聚合
    zh_rows = []
    for b in buildings:
        name = tr(b["name"])
        cost = b.get("cost", "")
        tech = tr(b.get("requiredTech", "")) if b.get("requiredTech") else ""
        kind = "奇观" if b.get("isWonder") else ("国家奇观" if b.get("isNationalWonder") else "")
        zh_rows.append(
            f"| [{name}](./{slugify(b['name'])}/) | {kind} | {cost} | {tech or '—'} |"
        )
    zh_table = "\n".join(
        [
            "| 建筑 | 类型 | 造价 | 所需科技 |",
            "| --- | --- | --- | --- |",
            *zh_rows,
        ]
    )
    zh_body = f"# 建筑\n\n{zh_table}\n"
    write_page(
        OUT_ZH_DB / "buildings" / "index.md",
        {"title": "建筑", "description": "Unciv 的全部建筑、奇观与国家奇观。"},
        zh_body,
    )
    # 实体独立页（全量）
    for b in buildings:
        gen_building_page(b)


def gen_building_page(b):
    name = b["name"]
    slug = slugify(name)
    # 英文
    fm = {"title": name, "description": f"{name} — cost, effects and tech requirements in Unciv."}
    body = f"# {name}\n\n"
    stat_rows = []
    label_map = {
        "cost": "Cost",
        "maintenance": "Maintenance",
        "requiredTech": "Required Tech",
        "requiredBuilding": "Required Building",
        "requiredResource": "Required Resource",
        "replaces": "Replaces",
        "uniqueTo": "Unique To",
        "production": "Production",
        "food": "Food",
        "gold": "Gold",
        "science": "Science",
        "culture": "Culture",
        "faith": "Faith",
        "happiness": "Happiness",
        "cityStrength": "City Strength",
    }
    for key, label in label_map.items():
        if key in b and b[key] not in (None, "", []):
            stat_rows.append(f"| {label} | {b[key]} |")
    if stat_rows:
        body += "## Stats\n\n" + "\n".join(
            ["| Attribute | Value |", "| --- | --- |", *stat_rows]
        ) + "\n\n"
    if b.get("uniques"):
        body += "## Effects\n\n" + uniques_list(b["uniques"]) + "\n\n"
    if b.get("quote"):
        body += f"> {b['quote']}\n\n"
    write_page(OUT_EN_DB / "buildings" / slug / "index.md", fm, body)
    # 中文
    zh_name = tr(name)
    zh_fm = {"title": zh_name, "description": f"{zh_name}——造价、效果与科技需求。"}
    zh_body = f"# {zh_name}\n\n"
    zh_label_map = {
        "cost": "造价",
        "maintenance": "维护费",
        "requiredTech": "所需科技",
        "requiredBuilding": "所需建筑",
        "requiredResource": "所需资源",
        "replaces": "替代",
        "uniqueTo": "专属文明",
        "production": "产能",
        "food": "食物",
        "gold": "金币",
        "science": "科研",
        "culture": "文化",
        "faith": "信仰",
        "happiness": "快乐",
        "cityStrength": "城市防御",
    }
    zh_stat_rows = []
    for key, label in zh_label_map.items():
        if key in b and b[key] not in (None, "", []):
            val = b[key]
            if key in ("requiredTech", "requiredBuilding", "replaces", "uniqueTo"):
                val = tr(val)
            zh_stat_rows.append(f"| {label} | {val} |")
    if zh_stat_rows:
        zh_body += "## 属性\n\n" + "\n".join(
            ["| 属性 | 数值 |", "| --- | --- |", *zh_stat_rows]
        ) + "\n\n"
    if b.get("uniques"):
        zh_body += "## 效果\n\n"
        for x in b["uniques"]:
            zh_body += f"- {tr(x)}\n"
        zh_body += "\n"
    write_page(OUT_ZH_DB / "buildings" / slug / "index.md", zh_fm, zh_body)


def gen_techs():
    techs = extract_techs()
    # 英文聚合
    rows = []
    for t in techs:
        name = t["name"]
        era = t.get("era", "")
        cost = t.get("cost", "")
        prereqs = ", ".join(t.get("prerequisites", []))
        rows.append(
            f"| [{name}](./{slugify(name)}/) | {tr(era)} | {cost} | {prereqs or '—'} |"
        )
    table = "\n".join(
        [
            "| Technology | Era | Cost | Prerequisites |",
            "| --- | --- | --- | --- |",
            *rows,
        ]
    )
    body = f"# Technologies\n\n{table}\n"
    write_page(
        OUT_EN_DB / "technologies" / "index.md",
        {"title": "Technologies", "description": "All technologies in Unciv — era, cost and prerequisites."},
        body,
    )
    # 中文聚合
    zh_rows = []
    for t in techs:
        name = tr(t["name"])
        era = tr(t.get("era", ""))
        cost = t.get("cost", "")
        prereqs = "、".join(tr(p) for p in t.get("prerequisites", []))
        zh_rows.append(
            f"| [{name}](./{slugify(t['name'])}/) | {era} | {cost} | {prereqs or '—'} |"
        )
    zh_table = "\n".join(
        [
            "| 科技 | 时代 | 花费 | 前置科技 |",
            "| --- | --- | --- | --- |",
            *zh_rows,
        ]
    )
    zh_body = f"# 科技\n\n{zh_table}\n"
    write_page(
        OUT_ZH_DB / "technologies" / "index.md",
        {"title": "科技", "description": "Unciv 的全部科技——时代、花费与前置科技。"},
        zh_body,
    )
    # 实体独立页（全量）
    for t in techs:
        gen_tech_page(t)


def gen_tech_page(t):
    name = t["name"]
    slug = slugify(name)
    # 英文
    fm = {"title": name, "description": f"{name} — era, cost and what it unlocks in Unciv."}
    body = f"# {name}\n\n"
    stat_rows = []
    label_map = {
        "era": "Era",
        "cost": "Cost",
        "prerequisites": "Prerequisites",
    }
    for key, label in label_map.items():
        if key in t and t[key] not in (None, "", []):
            val = t[key]
            if key == "prerequisites":
                val = ", ".join(val)
            stat_rows.append(f"| {label} | {val} |")
    if stat_rows:
        body += "## Info\n\n" + "\n".join(
            ["| Attribute | Value |", "| --- | --- |", *stat_rows]
        ) + "\n\n"
    if t.get("uniques"):
        body += "## Effects\n\n" + uniques_list(t["uniques"]) + "\n\n"
    if t.get("quote"):
        body += f"> {t['quote']}\n\n"
    write_page(OUT_EN_DB / "technologies" / slug / "index.md", fm, body)
    # 中文
    zh_name = tr(name)
    zh_fm = {"title": zh_name, "description": f"{zh_name}——时代、花费与解锁内容。"}
    zh_body = f"# {zh_name}\n\n"
    zh_label_map = {"era": "时代", "cost": "花费", "prerequisites": "前置科技"}
    zh_stat_rows = []
    for key, label in zh_label_map.items():
        if key in t and t[key] not in (None, "", []):
            val = t[key]
            if key == "prerequisites":
                val = "、".join(tr(p) for p in val)
            elif key == "era":
                val = tr(val)
            zh_stat_rows.append(f"| {label} | {val} |")
    if zh_stat_rows:
        zh_body += "## 信息\n\n" + "\n".join(
            ["| 属性 | 数值 |", "| --- | --- |", *zh_stat_rows]
        ) + "\n\n"
    if t.get("uniques"):
        zh_body += "## 效果\n\n"
        for x in t["uniques"]:
            zh_body += f"- {tr(x)}\n"
        zh_body += "\n"
    write_page(OUT_ZH_DB / "technologies" / slug / "index.md", zh_fm, zh_body)


# ---------------------------------------------------------------------------
# 成就
# ---------------------------------------------------------------------------
def gen_achievements():
    en = json.loads((ACHIEVEMENTS / "copy.json").read_text(encoding="utf-8"))
    zh = json.loads((ACHIEVEMENTS / "preview-v3-zh.json").read_text(encoding="utf-8"))
    en_entries = {e["id"]: e for e in en["entries"]}
    zh_entries = {e["id"]: e for e in zh["entries"]}

    # 图标复制到 public
    icon_src = ACHIEVEMENTS / "ui"
    icon_dst = OUT_PUBLIC / "achievements"
    icon_dst.mkdir(parents=True, exist_ok=True)
    for i in range(1, 41):
        sid = f"N{i:02d}"
        src = icon_src / f"{sid}.svg"
        if src.exists():
            shutil.copy2(src, icon_dst / f"{sid}.svg")

    # 英文列表页
    body = "# Achievements\n\n"
    body += "There are **40 achievements** on the iOS port (600 points total). Each is tracked across qualifying new games.\n\n"
    tier_order = ["Simple", "Intermediate", "Hard", "Extreme"]
    for tier in tier_order:
        tier_entries = [e for e in en_entries.values() if e["tier"] == tier]
        if not tier_entries:
            continue
        body += f"## {tier}\n\n"
        for e in sorted(tier_entries, key=lambda x: x["id"]):
            body += f"### {e['id']} — {e['name']}\n\n"
            body += f"<img src=\"/Unciv-Wiki/achievements/{e['id']}.svg\" alt=\"{e['name']}\" width=\"64\" height=\"64\" />\n\n"
            body += f"**Condition**: {e['condition']}\n\n"
            body += f"**Points**: {e['points']}\n\n"
            if e.get("honor"):
                body += f"*{e['honor']}*\n\n"
    write_page(
        OUT_ACH / "index.md",
        {"title": "Achievements", "description": "All 40 iOS achievements with conditions, points and icons."},
        body,
    )
    # 中文列表页
    zh_body = "# 成就\n\n"
    zh_body += "iOS 版共有 **40 项成就**（总计 600 分），每项都在合格的新对局中累计。\n\n"
    tier_zh = {"Simple": "简单", "Intermediate": "中等", "Hard": "困难", "Extreme": "极难"}
    for tier in tier_order:
        tier_entries = [e for e in zh_entries.values() if e["tier"] == tier]
        if not tier_entries:
            continue
        zh_body += f"## {tier_zh[tier]}\n\n"
        for e in sorted(tier_entries, key=lambda x: x["id"]):
            zh_body += f"### {e['id']} — {e['name']}\n\n"
            zh_body += f"<img src=\"/Unciv-Wiki/achievements/{e['id']}.svg\" alt=\"{e['name']}\" width=\"64\" height=\"64\" />\n\n"
            zh_body += f"**达成条件**：{e['condition']}\n\n"
            zh_body += f"**分值**：{e['points']}\n\n"
            if e.get("honor"):
                zh_body += f"*{e['honor']}*\n\n"
    write_page(
        OUT_ZH_ACH / "index.md",
        {"title": "成就", "description": "iOS 版全部 40 项成就，含达成条件、分值与图标。"},
        zh_body,
    )


def main():
    print("== Unciv Wiki 数据管道 ==")
    print("生成文明…")
    gen_nations()
    print("生成单位…")
    gen_units()
    print("生成建筑…")
    gen_buildings()
    print("生成科技…")
    gen_techs()
    print("生成成就…")
    gen_achievements()
    print("完成 ✅")


if __name__ == "__main__":
    main()
