"""Validated, offline input and the pinned engine's base-cost rules."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'site.config.json').read_text())
SNAPSHOT = ROOT / 'data/snapshots' / CONFIG['snapshot']

def slug(name):
    return re.sub(r'[^a-zA-Z0-9]+', '-', name).strip('-').lower()

def required_techs(item):
    names = [item['requiredTech']] if item.get('requiredTech') else []
    for unique in item.get('uniques', []):
        if unique.startswith(('Only available', 'Can only be built')):
            names += re.findall(r'<after discovering \[([^]]+)\]>', unique)
    return list(dict.fromkeys(names))

def resolve_techs(columns):
    return [{**tech, 'era': col['era'], 'cost': tech.get('cost', 0) or col['techCost'],
             'costOrigin': 'explicit' if tech.get('cost', 0) else 'inherited', 'column': col}
            for col in columns for tech in col['techs']]

def building_cost(item, techs):
    cost = item.get('cost', -1)
    if cost != -1: return cost, 'explicit'
    if 'Unbuildable' in item.get('uniques', []): return None, 'unbuildable'
    columns = [techs[n]['column'] for n in required_techs(item)]
    if not columns: return None, 'unspecified'
    column = max(columns, key=lambda c: c['columnNumber'])
    key = 'wonderCost' if item.get('isWonder') or item.get('isNationalWonder') else 'buildingCost'
    return column[key], 'inherited'

def load_snapshot(path=SNAPSHOT):
    manifest = json.loads((path / 'manifest.json').read_text())
    assert manifest['schemaVersion'] == 1
    assert (manifest['gameVersion'], manifest['appBuild']) == ('4.21.20', 1293)
    assert manifest['sourceCommits'] == {'public': '5fa2f57457755c403ea82cc21fec9e617feaf2d0', 'achievements': '153417ef69baab04ac1013ea496b7ed62e505d4c'}
    required = {'rules.json', 'zh.json', 'achievements.json', 'achievements-en.json', 'achievements-zh.json'} | {f'icons/N{i:02}.svg' for i in range(1, 41)}
    assert set(manifest['files']) == required, 'Incomplete snapshot inventory'
    for name, sha in manifest['files'].items():
        assert hashlib.sha256((path / name).read_bytes()).hexdigest() == sha, f'Checksum mismatch: {name}'
    data = {name[:-5]: json.loads((path / name).read_text()) for name in required if name.endswith('.json')}
    rules = data['rules']
    assert set(rules) == {'Nations', 'Units', 'Buildings', 'Techs'}
    techs = resolve_techs(rules['Techs'])
    nations = [n for n in rules['Nations'] if n.get('leaderName')]
    groups = {'civilizations': nations, 'units': rules['Units'], 'buildings': rules['Buildings'], 'technologies': techs}
    names = {key: {item['name'] for item in items} for key, items in groups.items()}
    assert {k: len(v) for k, v in groups.items()} == {'civilizations': 34, 'units': 127, 'buildings': 124, 'technologies': 80}, 'Pinned source catalogue changed'
    for key, items in groups.items():
        assert len(names[key]) == len(items) == len({slug(i['name']) for i in items}), f'Duplicate name/slug: {key}'
        for item in items:
            for field in ('cost', 'movement', 'strength', 'maintenance'):
                if field in item: assert isinstance(item[field], (int, float)), (item['name'], field)
            for field in ('percentStatBonus', 'specialistSlots'):
                if field not in item: continue
                assert isinstance(item[field], dict), (item['name'], field)
                assert all(isinstance(v, (int, float)) for v in item[field].values()), (item['name'], field)
            for specialist in item.get('specialistSlots', {}):
                assert specialist in data['zh'] and data['zh'][specialist], f'Missing specialist translation: {specialist}'
            refs = [(n, 'technologies') for n in required_techs(item) + item.get('prerequisites', [])]
            for field, target in [('obsoleteTech', 'technologies'), ('uniqueTo', 'civilizations'), ('replaces', key), ('upgradesTo', 'units'), ('requiredBuilding', 'buildings')]:
                if item.get(field): refs.append((item[field], target))
            for name, target in refs: assert name in names[target] or (target == 'civilizations' and name in {n['name'] for n in rules['Nations']}), f'Unknown relation: {item["name"]} -> {name}'
    def validate_text(value):
        if isinstance(value, str): assert value in data['zh'] and isinstance(data['zh'][value], str) and data['zh'][value], f'Missing zh text: {value}'
        elif isinstance(value, list):
            for v in value: validate_text(v)
        elif isinstance(value, dict):
            for v in value.values(): validate_text(v)
    validate_text(rules)
    achievements = data['achievements']; ids = {f'N{i:02}' for i in range(1, 41)}
    assert achievements['catalogVersion'] == achievements['recordingVersion'] == 3
    assert achievements['localPreview'] is True
    assert len(achievements['entries']) == 40 and {e['id'] for e in achievements['entries']} == ids
    assert sum(e['points'] for e in achievements['entries']) == achievements['totalPoints'] == 600
    source_sha = manifest['files']['achievements.json']
    assert manifest['sources']['assets/achievements/preview-v3-zh.json']['sha256'] == source_sha
    for lang in ['en', 'zh']:
        trans = data[f'achievements-{lang}']
        assert trans['sourceSha256'] == source_sha and set(trans['entries']) == ids
        for item in trans['entries'].values():
            for key in ['name', 'condition', 'summary', 'honor', 'clue', 'indexClue']:
                assert isinstance(item[key], str) and item[key].strip(), f'Missing achievement {lang}/{key}'
        if lang == 'en':
            assert not re.search(r'[\u4e00-\u9fff]', json.dumps(trans, ensure_ascii=False)), 'Chinese in English achievement catalogue'
    lookup = {t['name']: t for t in techs}
    for b in groups['buildings']:
        b['cost'], b['costOrigin'] = building_cost(b, lookup)
    return manifest, data, groups
