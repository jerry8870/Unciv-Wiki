#!/usr/bin/env python3
"""Regression checks against pinned game examples and failure-safe generation."""
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from wiki_data import ROOT, SNAPSHOT, load_snapshot, building_cost, resolve_techs

class PipelineTests(unittest.TestCase):
    def test_database_icon_coverage_in_both_languages(self):
        from wiki_data import CONFIG, slug
        _, _, groups = load_snapshot()
        manifest = json.loads((ROOT / 'data/guide-assets.json').read_text())
        assets = {a['path'] for a in manifest['assets']}
        for category, items in groups.items():
            mapping = manifest['databaseIcons'][category]
            self.assertEqual(set(mapping), {item['name'] for item in items})
            for prefix in ['', 'zh/']:
                directory = ROOT / f'src/content/docs/{prefix}database/{category}'
                listing = (directory / 'index.md').read_text()
                self.assertEqual(listing.count('class="database-icon"'), len(items))
                for item in items:
                    path = mapping[item['name']]
                    self.assertIn(path, assets)
                    source = f'src="{CONFIG["base"]}{path.removeprefix("public/")}"'
                    self.assertIn(source, listing)
                    detail = (directory / slug(item['name']) / 'index.md').read_text()
                    self.assertIn(source, detail)
                    self.assertIn('width="80" height="80"', detail)

    def test_guide_assets_match_pinned_manifest(self):
        import struct
        manifest_path = ROOT / 'data/guide-assets.json'
        manifest = json.loads(manifest_path.read_text())
        self.assertEqual((ROOT / 'public/game-assets/manifest.json').read_bytes(), manifest_path.read_bytes())
        self.assertEqual(manifest['sourceCommit'], '5fa2f57457755c403ea82cc21fec9e617feaf2d0')
        for asset in manifest['assets']:
            raw = (ROOT / asset['path']).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), asset['sha256'], asset['path'])
            self.assertEqual(raw[:8], b'\x89PNG\r\n\x1a\n', asset['path'])
            self.assertEqual(struct.unpack('>II', raw[16:24]), (asset['width'], asset['height']))
        credit = manifest['creditSource']
        self.assertEqual(hashlib.sha256((ROOT / credit['localCopy']).read_bytes()).hexdigest(), credit['sha256'])

    def test_civilization_rule_wording_survives_export_and_render(self):
        from translation import Translator
        examples = [
            ('babylon', '[Great Scientist] is earned [50]% faster', '大科学家点数获取速率提高 50%'),
            ('korea', 'Receive a tech boost when scientific buildings/wonders are built in capital', '在首都建成与科研相关的建筑或奇观时，获得一次科研点数奖励'),
            ('korea', '[+2 Science] from every specialist [in all cities]', '所有城市中，每位已安排工作的专家 +2 科研'),
            ('korea', '[+2 Science] from every [Great Improvement]', '每个伟人改良地块的产出 +2 科研（需要市民工作）'),
            ('rome', '[+25]% Production towards any buildings that already exist in the Capital', '建造首都已建成的同名建筑时，生产力提高 25%'),
            ('greece', '[-50]% City-State Influence degradation', '城邦影响力衰减速率降低 50%'),
            ('greece', 'City-State Influence recovers at twice the normal rate', '城邦影响力低于均衡点时，向均衡点恢复的速率为正常值的两倍'),
        ]
        _, data, _ = load_snapshot()
        with tempfile.TemporaryDirectory() as directory:
            props = Path(directory) / 'zh.properties'
            props.write_text('[greatPerson] is earned [relativeAmount]% faster = [greatPerson]的招募速率[relativeAmount]%\n')
            translator = Translator(props)
            for civ, source, expected in examples:
                self.assertEqual(translator.translate(source), expected)
                self.assertEqual(data['zh'][source], expected)
                page = (ROOT / f'src/content/docs/zh/database/civilizations/{civ}/index.md').read_text()
                self.assertIn(expected, page)
            # The exact-key correction must not reinterpret other great-person rules.
            self.assertEqual(translator.translate('[Great General] is earned [50]% faster'), 'Great General的招募速率50%')
    def test_building_effects_survive_export_and_render(self):
        _, _, groups = load_snapshot()
        buildings = {b['name']: b for b in groups['buildings']}
        self.assertEqual(buildings['University']['percentStatBonus'], {'science': 33})
        self.assertEqual(buildings['University']['specialistSlots'], {'Scientist': 2})
        self.assertEqual(buildings['National College']['percentStatBonus'], {'science': 50})
        self.assertEqual(buildings['Market']['percentStatBonus'], {'gold': 25})
        for prefix, expected in [('', ['Science bonus | +33%', 'Scientist × 2']),
                                 ('zh/', ['科研加成 | +33%', '科学家 × 2'])]:
            page = (ROOT / f'src/content/docs/{prefix}database/buildings/university/index.md').read_text()
            for value in expected: self.assertIn(value, page)

    def test_engine_cost_examples(self):
        _, data, groups = load_snapshot()
        tech = {t['name']: t for t in groups['technologies']}
        buildings = {b['name']: b for b in groups['buildings']}
        self.assertEqual((tech['Writing']['cost'], tech['Writing']['costOrigin']), (55, 'inherited'))
        self.assertEqual((tech['Optics']['cost'], tech['Optics']['costOrigin']), (85, 'explicit'))
        for name, expected in [('Library', 75), ('The Great Library', 185), ('Shrine', 40), ('Palace', 0), ('Cathedral', 0), ('National College', 125)]:
            self.assertEqual(buildings[name]['cost'], expected, name)
        self.assertIn('Unbuildable', buildings['Cathedral']['uniques'])
        # The pinned catalogue has no default-cost unbuildable building or inherited national wonder.
        # These engine branches use a clearly synthetic variation of real source entries.
        cathedral = next(b.copy() for b in data['rules']['Buildings'] if b['name'] == 'Cathedral')
        cathedral.pop('cost'); self.assertEqual(building_cost(cathedral, tech), (None, 'unbuildable'))
        college = next(b.copy() for b in data['rules']['Buildings'] if b['name'] == 'National College')
        college['cost'] = -1
        self.assertEqual(building_cost(college, tech), (tech[college['requiredTech']]['column']['wonderCost'], 'inherited'))
        column = {'era': 'Ancient era', 'columnNumber': 0, 'techCost': 20, 'techs': [{'name': 'Agriculture', 'cost': 0}]}
        self.assertEqual(resolve_techs([column])[0]['cost'], 20)

    def test_translated_placeholder_order(self):
        from translation import Translator
        with tempfile.TemporaryDirectory() as directory:
            props = Path(directory) / 'zh.properties'
            props.write_text('Gain a free [building] [cityFilter] = [cityFilter]获得一座免费的[building]\nLibrary = 图书馆\nin this city = 在这个城市中\nScience = 科研\n')
            translator = Translator(props)
            self.assertEqual(translator.translate('Gain a free [Library] [in this city]'), '在这个城市中获得一座免费的图书馆')
            self.assertEqual(translator.translate('+1 Science'), '+1 科研')

    def test_achievement_v3(self):
        _, data, _ = load_snapshot()
        entries = data['achievements-en']['entries']
        self.assertIn('3 combat-earned promotions', entries['N08']['condition'])
        self.assertIn('15 population', entries['N11']['condition'])
        self.assertIn('3 different cities', entries['N32']['condition'])
        rules = {e['id']: e for e in data['achievements']['entries']}
        for aid in rules:
            if aid == 'N40':
                # Matching V3 translation intentionally drops the source's locale-only wording.
                self.assertEqual(data['achievements-zh']['entries'][aid]['condition'], '在本轮测试目录中，完成其余三十九个成就。')
                self.assertEqual(rules[aid]['condition'], '在本轮中文测试目录中，完成其余三十九个成就。')
                continue
            self.assertEqual(re.sub(r'\s+', '', data['achievements-zh']['entries'][aid]['condition']), re.sub(r'\s+', '', rules[aid]['condition']))

    def test_repeatability_manual_preservation_and_failed_input(self):
        def hashes():
            paths = list((ROOT / 'src/content').rglob('*')) + list((ROOT / 'public/achievements').glob('N*.svg')) + [ROOT / 'data/generated-files.json']
            return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}
        before = hashes()
        for _ in range(2): subprocess.run([sys.executable, str(ROOT / 'scripts/generate.py')], check=True, capture_output=True)
        self.assertEqual(before, hashes(), 'Regeneration changed manual or generated content')
        for failure in ['missing', 'checksum', 'reference', 'translation']:
            with tempfile.TemporaryDirectory() as directory:
                snapshot = Path(directory) / 'snapshot'; shutil.copytree(SNAPSHOT, snapshot)
                manifest = json.loads((snapshot / 'manifest.json').read_text())
                if failure == 'missing': (snapshot / 'icons/N01.svg').unlink()
                elif failure == 'checksum': (snapshot / 'rules.json').write_text('{}')
                else:
                    filename = 'rules.json' if failure == 'reference' else 'achievements-en.json'
                    value = json.loads((snapshot / filename).read_text())
                    if failure == 'reference': value['Units'][0]['requiredTech'] = 'Missing technology'
                    else: del value['entries']['N08']
                    (snapshot / filename).write_text(json.dumps(value))
                    manifest['files'][filename] = hashlib.sha256((snapshot / filename).read_bytes()).hexdigest()
                    (snapshot / 'manifest.json').write_text(json.dumps(manifest))
                result = subprocess.run([sys.executable, str(ROOT / 'scripts/generate.py'), '--snapshot', str(snapshot)], capture_output=True)
                self.assertNotEqual(result.returncode, 0, failure)
                self.assertEqual(before, hashes(), 'Failed input changed published files: ' + failure)

if __name__ == '__main__': unittest.main()
