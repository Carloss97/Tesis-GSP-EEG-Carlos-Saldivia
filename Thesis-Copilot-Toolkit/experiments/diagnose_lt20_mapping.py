#!/usr/bin/env python3
"""
Diagnose mapping between IterDef.datasets and load_data_availability() keys.
Usage: python diagnose_lt20_mapping.py [--tag TAG]
"""
import importlib.util
import sys
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / 'experiments' / 'run_reruns_selected.py'
RESULTS = ROOT / 'results'


def load_runner_module(path: Path):
    spec = importlib.util.spec_from_file_location('runner_mod', str(path))
    runner = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = runner
    spec.loader.exec_module(runner)
    return runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tag', default=None)
    args = parser.parse_args()

    runner = load_runner_module(RUNNER)
    defs = getattr(runner, '_defs', [])
    base_mod = getattr(runner, 'mod', None)
    if base_mod is None:
        print('Base engine (mod) not found in runner module.')
        sys.exit(1)

    av = base_mod.load_data_availability()
    availability = av.get('availability', {})
    data = av.get('data', {})

    keys = [d.key for d in defs]
    missing = [k for k in keys if not (RESULTS / f"{k}_raw.csv").exists()]

    tag = args.tag or (missing[0] if missing else None)
    if not tag:
        print('No missing tags found.')
        return

    it = next((d for d in defs if d.key == tag), None)
    if it is None:
        print('Tag not found in runner:', tag)
        return

    print('=== Diagnostic for', tag, '===')
    print('IterDef.datasets:', it.datasets)
    print('Availability keys:', sorted(list(availability.keys())))
    print('Data keys loaded:', sorted(list(data.keys())))

    available_ds = [ds for ds in it.datasets if availability.get(ds, {}).get('ok')]
    print('Available datasets for this IterDef:', available_ds)

    print('\nDetails per requested dataset:')
    for ds in it.datasets:
        print(' -', ds, '->', availability.get(ds))

    print('\nSummary:')
    for k in sorted(availability.keys()):
        v = availability.get(k)
        print(f' * {k}: ok={v.get("ok")}, reason={v.get("reason")}')


if __name__ == '__main__':
    main()
