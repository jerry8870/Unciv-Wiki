"""Translation of exported wiki text, using the game properties catalogue."""
import re
from pathlib import Path

POINTY_RE = re.compile(r"<([^>]*)>")
SQUARE_RE = re.compile(r"\[([^\]]*)\]")

# Website wording for these exact 1293 rules; verified against the pinned engine.
# Keep upstream keys intact so refreshed exports and generated pages stay reproducible.
ZH_RULE_OVERRIDES = {
    '[Great Scientist] is earned [50]% faster': '大科学家点数获取速率提高 50%',
    '[+2 Science] from every specialist [in all cities]': '所有城市中，每位已安排工作的专家 +2 科研',
    '[+2 Science] from every [Great Improvement]': '每个伟人改良地块的产出 +2 科研（需要市民工作）',
    'Receive a tech boost when scientific buildings/wonders are built in capital': '在首都建成与科研相关的建筑或奇观时，获得一次科研点数奖励',
    '[+25]% Production towards any buildings that already exist in the Capital': '建造首都已建成的同名建筑时，生产力提高 25%',
    '[-50]% City-State Influence degradation': '城邦影响力衰减速率降低 50%',
    'City-State Influence recovers at twice the normal rate': '城邦影响力低于均衡点时，向均衡点恢复的速率为正常值的两倍',
}


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
        self.parameters: dict[str, list[str]] = {}
        for k, v in raw.items():
            if "[" in k and "<" not in k:
                self.table[get_placeholder_text(k)] = v
                self.parameters[get_placeholder_text(k)] = get_placeholder_params(k)
            else:
                self.table[k] = v

    def translate(self, text: str) -> str:
        """翻译一段文本（含占位符回填）。找不到则回退英文原文。"""
        text = re.sub(r'<Civilopedia link \[[^]]+\]>', '', text).strip()
        if not text:
            return text
        if text in ZH_RULE_OVERRIDES:
            return ZH_RULE_OVERRIDES[text]
        # 1) 无括号：直接查表
        if "[" not in text and "<" not in text:
            if text in self.table:
                return self.table[text]
            # Stat parameters are values such as "+1 Science", not literal translation keys.
            match = re.fullmatch(r'([+-]?\d+(?:\.\d+)?)(%)? (Food|Production|Gold|Science|Culture|Faith|Happiness)', text)
            if match:
                return match[1] + (match[2] or '') + ' ' + self.table.get(match[3], match[3])
            return text

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

        # Match translated placeholders by their source names: Chinese can reorder them.
        source_params = self.parameters.get(key, [])
        if len(source_params) != len(params):
            return text
        values = {source: self._expand_filters(self.translate(value))
                  for source, value in zip(source_params, params)}
        return SQUARE_RE.sub(lambda match: values.get(match[1], match[0]), template)

    def _expand_filters(self, p: str) -> str:
        """展开 {A} {B} 过滤器为可读形式（如 {Military} {Water} -> 军事 海上）。"""
        def repl(m):
            inner = m.group(1)
            parts = [self.table.get(x, x) for x in inner.split()]
            return " ".join(parts)
        return re.sub(r"\{([^}]*)\}", repl, p)

