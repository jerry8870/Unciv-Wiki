#!/usr/bin/env python3
"""Validate all snapshot inputs, render in staging, then publish owned files only."""
import argparse
import html
import json
import re
import tempfile
from pathlib import Path
from wiki_data import ROOT, CONFIG, SNAPSHOT, load_snapshot, required_techs, slug

LABELS = {'civilizations': ('Civilizations', '文明'), 'units': ('Units', '单位'),
          'buildings': ('Buildings', '建筑'), 'technologies': ('Technologies', '科技')}
GUIDES = {
    'strategies/babylon': ('Babylon: early science', '巴比伦：早期科研'),
    'strategies/korea': ('Korea: specialists and the capital', '朝鲜：专家与首都建设'),
    'strategies/rome': ('Rome: construction and war', '罗马：建设与战争'),
    'strategies/greece': ('Greece: city-state networks', '希腊：城邦网络'),
    'mechanics/policies': ('Policy planning', '政策规划'),
    'mechanics/resources-improvements': ('Citizens, resources and improvements', '市民、资源与改良'),
    'mechanics/combat-promotions': ('Terrain and promotions', '地形与晋升'),
    'mechanics/religion-beliefs': ('Belief effects and returns', '信条效果与收益'),
}
RELATED_GUIDES = {
    ('buildings', 'University'): ['mechanics/policies', 'mechanics/resources-improvements', 'strategies/babylon', 'strategies/korea'],
    ('buildings', 'Library'): ['strategies/rome', 'strategies/babylon', 'strategies/korea'],
    ('buildings', 'National College'): ['strategies/babylon', 'strategies/korea', 'strategies/rome'],
    ('buildings', 'Temple'): ['mechanics/religion-beliefs'],
    ('buildings', 'Shrine'): ['mechanics/religion-beliefs', 'mechanics/policies'],
    ('buildings', 'Pagoda'): ['mechanics/religion-beliefs'],
    ('buildings', 'Courthouse'): ['strategies/rome'],
    ('units', 'Great Scientist'): ['strategies/babylon', 'strategies/korea', 'mechanics/resources-improvements'],
    ('units', 'Worker'): ['mechanics/resources-improvements'],
    ('units', 'Trebuchet'): ['mechanics/combat-promotions', 'strategies/korea'],
    ('units', 'Catapult'): ['mechanics/combat-promotions', 'strategies/rome'],
    ('technologies', 'Writing'): ['strategies/babylon', 'strategies/korea'],
    ('technologies', 'Education'): ['strategies/babylon', 'strategies/korea', 'mechanics/resources-improvements'],
    ('technologies', 'Iron Working'): ['strategies/rome', 'mechanics/resources-improvements'],
    ('technologies', 'Mathematics'): ['strategies/rome'],
}
FIELDS = {'leaderName': ('Leader', '领袖'), 'uniqueName': ('Unique ability', '独特能力'),
 'preferredVictoryType': ('Preferred victory', '偏好胜利'), 'unitType': ('Type', '类型'),
 'movement': ('Movement', '移动力'), 'strength': ('Strength', '战斗力'), 'rangedStrength': ('Ranged strength', '远程战斗力'),
 'range': ('Range', '射程'), 'cost': ('Base cost', '基础花费'), 'maintenance': ('Maintenance', '维护费'),
 'requiredTech': ('Required technology', '所需科技'), 'obsoleteTech': ('Obsolete technology', '淘汰科技'),
 'upgradesTo': ('Upgrades to', '升级为'), 'requiredResource': ('Required resource', '所需资源'),
 'requiredBuilding': ('Required building', '所需建筑'), 'replaces': ('Replaces', '替代'), 'uniqueTo': ('Unique to', '专属文明'),
 'production': ('Production', '生产力'), 'food': ('Food', '食物'), 'gold': ('Gold', '金币'),
 'science': ('Science', '科研'), 'culture': ('Culture', '文化'), 'faith': ('Faith', '信仰'),
 'happiness': ('Happiness', '快乐'), 'cityStrength': ('City strength', '城市防御'), 'era': ('Era', '时代')}

def table(headers, rows):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(str(v).replace('|', '\\|').replace('\n', ' ') for v in row) + ' |' for row in rows]) + '\n\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--snapshot', type=Path, default=SNAPSHOT)
    args = parser.parse_args()
    manifest, data, groups = load_snapshot(args.snapshot)
    icons = json.loads((ROOT / 'data/guide-assets.json').read_text())['databaseIcons']
    fragments = {lang: (ROOT / f'src/content/fragments/achievements-{lang}.md').read_text() for lang in ['en', 'zh']}
    outputs = {}
    for lang in ['en', 'zh']:
        ix = int(lang == 'zh'); prefix = 'zh/' if ix else ''
        def tr(value):
            text = data['zh'].get(str(value), str(value)) if ix else str(value)
            return re.sub(r'<Civilopedia link \[[^]]+\]>', '', text).strip()
        def url(path): return CONFIG['base'] + prefix + path
        def icon(category, name, detail=False):
            source = CONFIG['base'] + icons[category][name].removeprefix('public/')
            size = 80 if detail else 32
            return f'<span class="database-icon-frame"><img class="database-icon" src="{source}" alt="{html.escape(tr(name), quote=True)}" width="{size}" height="{size}" loading="lazy" decoding="async" /></span>'
        credit_link = f'[{"图标来源与署名" if ix else "Icon sources and credits"}]({url("credits/")})'
        def link(category, name):
            if name and name not in {i['name'] for i in groups[category]}: return html.escape(tr(name))
            return f'[{html.escape(tr(name))}]({url("database/" + category + "/" + slug(name) + "/")})' if name else '—'
        def page(path, title, description, body):
            fm = {'title': title, 'description': description, 'gameVersion': manifest['gameVersion'],
                  'appBuild': manifest['appBuild'], 'ruleset': manifest['ruleset'],
                  'sources': ['snapshot:' + CONFIG['snapshot']], 'lastUpdated': manifest['contentUpdated']}
            outputs['src/content/docs/' + prefix + path + 'index.md'] = ('---\n' + json.dumps(fm, ensure_ascii=False, indent=2) + '\n---\n\n' + body).encode()
        note = ('数值为 **Gods & Kings 规则集基础数值**，不等于每局最终价格。速度、难度、城市数量及规则效果等可能修正花费。' if ix else '**Gods & Kings ruleset base values** are not final prices in every game. Speed, difficulty, city count and rule effects can modify costs.')
        note += f' [{"花费说明" if ix else "How costs work"}]({url("mechanics/")}).\n\n'
        for category, items in groups.items():
            title = LABELS[category][ix]
            rows = []
            for item in items:
                name = item['name']; kind = ''
                if category == 'civilizations':
                    rows.append([icon(category, name) + ' ' + link(category, name), tr(item.get('leaderName', '—')), tr(item.get('uniqueName', '—')), tr(item.get('preferredVictoryType', '—'))])
                else:
                    if category == 'units': kind = tr(item.get('unitType', '—'))
                    if category == 'buildings': kind = ('世界奇观' if ix else 'World wonder') if item.get('isWonder') else ('国家奇观' if ix else 'National wonder') if item.get('isNationalWonder') else ('建筑' if ix else 'Building')
                    if category == 'technologies': kind = tr(item['era'])
                    cost = item.get('cost', '—')
                    if cost is None: cost = '—'
                    if 'Unbuildable' in item.get('uniques', []): cost = f'{cost} ({"不可直接建造" if ix else "not directly buildable"})'
                    rows.append([icon(category, name) + ' ' + link(category, name), kind, cost, ', '.join(link('technologies', n) for n in (item.get('prerequisites', []) if category == 'technologies' else required_techs(item))) or '—'])
                stats = []
                for field, labels in FIELDS.items():
                    if field not in item or item[field] in (None, '', []): continue
                    value = item[field]
                    target = {'requiredTech': 'technologies', 'obsoleteTech': 'technologies', 'upgradesTo': 'units', 'requiredBuilding': 'buildings', 'replaces': category, 'uniqueTo': 'civilizations'}.get(field)
                    stats.append([labels[ix], link(target, value) if target else html.escape(tr(value))])
                if category == 'buildings':
                    stats.insert(0, ['类型' if ix else 'Type', kind])
                    for stat, value in item.get('percentStatBonus', {}).items():
                        stats.append([FIELDS[stat][ix] + ('加成' if ix else ' bonus'), f'{value:+g}%'])
                    if item.get('specialistSlots'):
                        stats.append(['专家槽位' if ix else 'Specialist slots',
                                      ', '.join(f'{html.escape(tr(name))} × {count}' for name, count in item['specialistSlots'].items())])
                body = icon(category, name, detail=True) + '\n\n' + credit_link + '\n\n' + note + table(('属性', '值') if ix else ('Attribute', 'Value'), stats)
                if item.get('costOrigin'):
                    origins = {'explicit': ('Explicit source value (including zero).', '采用源码显式数值（包括零值）。'), 'inherited': ('Inherited from the required technology column.', '继承所需科技列的默认花费。'), 'unbuildable': ('Not directly buildable; no production cost inherited.', '不可直接建造；不继承生产花费。'), 'unspecified': ('No base cost resolved; this is not a free building.', '无法确定基础造价，不表示免费建筑。')}
                    body += origins[item['costOrigin']][ix] + '\n\n'
                if item.get('prerequisites'): body += ('前置科技：' if ix else 'Prerequisites: ') + ', '.join(link('technologies', n) for n in item['prerequisites']) + '\n\n'
                for field, titles in [('uniques', ('Rules and effects', '规则与效果')), ('promotions', ('Promotions', '晋升')), ('startBias', ('Starting bias', '开局倾向'))]:
                    if item.get(field): body += f'## {titles[ix]}\n\n' + '\n'.join('- ' + html.escape(tr(u)) for u in item[field] if '<hidden from Civilopedia>' not in u) + '\n\n'
                related = []
                if category == 'technologies':
                    for cat in ['units', 'buildings']:
                        related += [link(cat, v['name']) for v in groups[cat] if name in required_techs(v)]
                    related += [link('technologies', v['name']) for v in groups['technologies'] if name in v.get('prerequisites', [])]
                elif category == 'civilizations':
                    for cat in ['units', 'buildings']: related += [link(cat, v['name']) for v in groups[cat] if v.get('uniqueTo') == name]
                else:
                    related += [link(category, v['name']) for v in items if v.get('replaces') == name or v.get('upgradesTo') == name]
                if related: body += ('## 解锁与关联\n\n' if ix else '## Unlocks and related entries\n\n') + '\n'.join('- ' + v for v in related) + '\n\n'
                guides = list(RELATED_GUIDES.get((category, name), []))
                civilization = name if category == 'civilizations' else item.get('uniqueTo', '')
                civ_guide = 'strategies/' + slug(civilization)
                if civ_guide in GUIDES: guides.insert(0, civ_guide)
                if category == 'units' and civ_guide in GUIDES: guides.append('mechanics/combat-promotions')
                if guides:
                    body += ('## 对局与机制攻略\n\n' if ix else '## Match and mechanics guides\n\n')
                    body += '\n'.join(f'- [{GUIDES[g][ix]}]({url(g + "/")})' for g in dict.fromkeys(guides)) + '\n\n'
                if item.get('quote'): body += '> ' + html.escape(tr(item['quote'])) + '\n\n'
                desc = f'{tr(name)}：4.21.20（1293）{title}基础属性、规则和关联条目。' if ix else f'{name}: base values, rules and related {title.lower()} in Unciv 4.21.20 (1293).'
                page(f'database/{category}/{slug(name)}/', tr(name), desc, body)
            headers = (['文明', '领袖', '独特能力', '偏好胜利'] if ix else ['Civilization', 'Leader', 'Unique ability', 'Preferred victory']) if category == 'civilizations' else (['名称', '类型 / 时代', '基础花费', '所需 / 前置科技'] if ix else ['Name', 'Type / era', 'Base cost', 'Required / prerequisite technology'])
            body = note + table(headers, rows) + credit_link + '\n\n'
            if category == 'civilizations':
                body += ('## 城邦\n\n' if ix else '## City-states\n\n') + table(['城邦', '类型', '性格'] if ix else ['City-state', 'Type', 'Personality'], [[tr(n['name']), tr(n.get('cityStateType', '—')), tr(n.get('personality', '—'))] for n in data['rules']['Nations'] if n.get('cityStateType')])
            page('database/' + category + '/', title, f'4.21.20 (1293) · {title} · Gods & Kings', body)
        body = fragments[lang].replace('{{BASE}}', CONFIG['base']) + '\n\n'
        entries = data['achievements']['entries']; trans = data[f'achievements-{lang}']['entries']
        for tier, labels in [('Simple', ('Easy', '简单')), ('Intermediate', ('Intermediate', '中等')), ('Hard', ('Hard', '困难')), ('Extreme', ('Extreme', '极难'))]:
            body += f'## {labels[ix]}\n\n'
            for e in entries:
                if e['tier'] != tier: continue
                text = trans[e['id']]; aid = e['id']; name = html.escape(text['name'])
                body += f'<span id="{aid}"></span>\n\n### {aid} — {name}\n\n<img src="{CONFIG["base"]}achievements/{aid}.svg" alt="{name}" width="64" height="64" loading="lazy" />\n\n'
                body += f'**{"达成条件" if ix else "Condition"}**: {html.escape(text["condition"])}\n\n'
                difficulty = tr(e['minimumDifficulty']) if e['minimumDifficulty'] else ('不限' if ix else 'Any')
                body += f'**{"分值 / 最低难度 / 最少 AI 对手" if ix else "Points / minimum difficulty / minimum AI opponents"}**: {e["points"]} / {difficulty} / {e["minimumOpponents"]}\n\n'
                body += f'*{html.escape(text["honor"])}*\n\n'
        page('achievements/', '成就' if ix else 'Achievements', '1293 V3：40 项本机成就，共 600 分，含条件、难度和排查入口。' if ix else '1293 V3: 40 local achievements, 600 points, with requirements, difficulty and troubleshooting.', body)
    for i in range(1, 41): outputs[f'public/achievements/N{i:02}.svg'] = (args.snapshot / f'icons/N{i:02}.svg').read_bytes()
    # Owned-path inventory includes generated category/entity pages and icons, never manual articles.
    inventory = ROOT / 'data/generated-files.json'
    old = set(json.loads(inventory.read_text())) if inventory.exists() else set()
    def owned(name):
        return bool(__import__('re').fullmatch(r'(src/content/docs/(zh/)?(database/(civilizations|units|buildings|technologies)/([a-z0-9-]+/)?index.md|achievements/index.md)|public/achievements/N\d{2}.svg)', name))
    assert all(owned(name) for name in old | set(outputs)), 'Invalid generated-file ownership'
    differences = [name for name, content in outputs.items() if not (ROOT / name).exists() or (ROOT / name).read_bytes() != content] + sorted(old - set(outputs))
    inventory_content = (json.dumps(sorted(outputs), indent=2) + '\n').encode()
    if not inventory.exists() or inventory.read_bytes() != inventory_content: differences.append('data/generated-files.json')
    if args.check:
        if differences: raise SystemExit('Generated files differ: ' + ', '.join(differences[:10]))
        print(f'Validated snapshot and {len(outputs)} generated files; reproducible.'); return
    # All validation and rendering has succeeded before any public output is changed.
    with tempfile.TemporaryDirectory(prefix='unciv-wiki-') as temp:
        stage = Path(temp)
        for name, content in outputs.items():
            dest = stage / name; dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(content)
        for name in outputs:
            dest = ROOT / name; dest.parent.mkdir(parents=True, exist_ok=True)
            if name in differences: dest.write_bytes((stage / name).read_bytes())
        for name in old - set(outputs): (ROOT / name).unlink(missing_ok=True)
        inventory.write_bytes(inventory_content)
    print(f'Generated {len(outputs)} owned files; {len(differences)} changed.')

if __name__ == '__main__': main()
