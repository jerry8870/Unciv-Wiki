#!/usr/bin/env python3
"""Restore the selected, checksummed guide PNGs from the pinned source commit."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-repo', type=Path, required=True)
    args = parser.parse_args()
    manifest_path = ROOT / 'data/guide-assets.json'
    manifest = json.loads(manifest_path.read_text())
    credit = manifest['creditSource']
    entries = manifest['assets'] + [{
        'sourcePath': credit['path'], 'path': credit['localCopy'],
        'sha256': credit['sha256'],
    }]
    outputs = {}
    for entry in entries:
        raw = subprocess.check_output([
            'git', '-C', str(args.source_repo), 'show',
            manifest['sourceCommit'] + ':' + entry['sourcePath'],
        ])
        if hashlib.sha256(raw).hexdigest() != entry['sha256']:
            raise ValueError('Source checksum mismatch: ' + entry['sourcePath'])
        outputs[entry['path']] = raw
    # Source access or checksum failure must not leave a partially refreshed asset set.
    outputs['public/game-assets/manifest.json'] = manifest_path.read_bytes()
    for name, raw in outputs.items():
        destination = ROOT / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)
    print(f'Restored {len(manifest["assets"])} original PNGs and attribution files.')


if __name__ == '__main__':
    main()
