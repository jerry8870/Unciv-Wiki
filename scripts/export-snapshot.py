#!/usr/bin/env python3
"""One-time source export. Normal generation/builds do not need either repository."""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path
from translation import Translator

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_COMMIT = '5fa2f57457755c403ea82cc21fec9e617feaf2d0'
PRIVATE_COMMIT = '153417ef69baab04ac1013ea496b7ed62e505d4c'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def json_bytes(data):
    return (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode()

def parse(data):
    # Preserve quoted strings, including URLs containing //.
    text = re.sub(r'"(?:\\.|[^"\\])*"|/\*.*?\*/|//[^\n]*',
                  lambda m: m[0] if m[0].startswith('"') else '', data.decode(), flags=re.S)
    return json.loads(text)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--public-repo', type=Path, required=True)
    p.add_argument('--private-repo', type=Path, required=True)
    p.add_argument('--output', type=Path, default=ROOT / 'data/snapshots/4.21.20-1293')
    args = p.parse_args()
    sources, files = {}, {}
    def read(repo, commit, path):
        data = subprocess.check_output(['git', '-C', str(repo), 'show', f'{commit}:{path}'])
        sources[path] = {'commit': commit, 'sha256': digest(data)}
        return data
    prefix = 'android/assets/jsons/'
    fields = set('name leaderName uniqueName preferredVictoryType cityStateType personality startBias uniques unitType movement strength rangedStrength range cost requiredTech obsoleteTech upgradesTo requiredResource replaces uniqueTo promotions maintenance requiredBuilding production food gold science culture faith happiness cityStrength isWonder isNationalWonder quote prerequisites era techs techCost buildingCost wonderCost columnNumber'.split())
    def select(value):
        if isinstance(value, list): return [select(v) for v in value]
        if isinstance(value, dict): return {k: v if k in {'percentStatBonus', 'specialistSlots'} else select(v)
                                            for k, v in value.items() if k in fields or k in {'percentStatBonus', 'specialistSlots'}}
        return value
    rules = {}
    for name in ['Nations', 'Units', 'Buildings', 'Techs']:
        rules[name] = select(parse(read(args.public_repo, PUBLIC_COMMIT, prefix + f'Civ V - Gods & Kings/{name}.json')))
    files['rules.json'] = json_bytes(rules)
    props = read(args.public_repo, PUBLIC_COMMIT, prefix + 'translations/Simplified_Chinese.properties')
    with tempfile.TemporaryDirectory() as temp:
        path = Path(temp) / 'zh.properties'; path.write_bytes(props)
        translator = Translator(path)
        strings = {'Prince', 'King', 'Emperor', 'Immortal', 'Deity'}
        def collect(value):
            if isinstance(value, str): strings.add(value)
            elif isinstance(value, list):
                for v in value: collect(v)
            elif isinstance(value, dict):
                for k, v in value.items():
                    if k == 'specialistSlots': strings.update(v)
                    collect(v)
        collect(rules)
        files['zh.json'] = json_bytes({s: translator.translate(s).strip() for s in sorted(strings)})
    achpath = 'assets/achievements/'
    canonical = read(args.private_repo, PRIVATE_COMMIT, achpath + 'preview-v3-zh.json')
    files['achievements.json'] = canonical
    for lang, name in [('en', 'English'), ('zh', 'Simplified_Chinese')]:
        data = parse(read(args.private_repo, PRIVATE_COMMIT, achpath + f'translations-v3/{name}.json'))
        if data['sourceSha256'] != digest(canonical): raise ValueError('Achievement translation source mismatch')
        # UI-only strings are not needed by the website.
        files[f'achievements-{lang}.json'] = json_bytes({k: data[k] for k in ['sourceSha256', 'language', 'entries']})
    for i in range(1, 41):
        filename = f'N{i:02}.svg'
        files['icons/' + filename] = read(args.private_repo, PRIVATE_COMMIT, achpath + 'ui/' + filename)
    manifest = {'schemaVersion': 1, 'gameVersion': '4.21.20', 'appBuild': 1293,
                'ruleset': 'Civ V - Gods & Kings', 'contentUpdated': '2026-09-12',
                'sourceCommits': {'public': PUBLIC_COMMIT, 'achievements': PRIVATE_COMMIT},
                'sources': sources, 'files': {k: digest(v) for k, v in files.items()}}
    # Read everything successfully before writing any snapshot output.
    for name, data in files.items():
        dest = args.output / name; dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(data)
    (args.output / 'manifest.json').write_bytes(json_bytes(manifest))
    print(f'Exported {len(files)} website-only files to {args.output}')

if __name__ == '__main__': main()
