"""
Small pilot harness to validate inclusion of `temporal_laplacian` in the TV family.

Usage (from repo root):
  $env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'
  python Thesis-Copilot-Toolkit/experiments/pilot_methods.py --light-profile

This script selects the first available dataset (prefers local real EEG keys), runs a
very short pilot (seeds=[0,1] in `--light-profile`) and writes artifacts to
`results_pilot_methods/`.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'
spec = importlib.util.spec_from_file_location('base_mod', str(BASE_SCRIPT))
base_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
assert loader is not None
loader.exec_module(base_mod)

IterDef = base_mod.IterDef

RESULTS = ROOT / 'results_pilot_methods'
RESULTS.mkdir(parents=True, exist_ok=True)


def build_defs(availability: dict) -> list[IterDef]:
    # Preferred local real datasets; fall back to any available dataset
    preferred = ['mne_sample', 'physionet_real', 'bci_iv2a_real_s1', 'iv100hz_mat', 'iris_graph_signal']
    available = [k for k, v in availability.items() if v.get('ok')]
    chosen = [k for k in preferred if k in available]
    if not chosen:
        chosen = available[:1]
    if not chosen:
        # nothing available: use synthetic placeholder (will be skipped but script stays safe)
        chosen = ['synthetic_16ch']

    methods = ['mean', 'nearest', 'tikhonov', 'trss', 'graph_time_tikhonov', 'temporal_laplacian']

    it = IterDef(
        key='pilot_temporal_laplacian_001',
        tag='pilot_temporal_laplacian_001',
        description='Pilot: temporal_laplacian inclusion check',
        fase='Pilot',
        objective='Quick pilot to validate temporal_laplacian behavior vs instant methods',
        datasets=chosen,
        mode='base',
        missing_list=[0.2],
        seeds=[0, 1],
        graph_specs=[('knn', {'k': 3})],
        methods=methods,
    )
    return [it]


def main():
    parser = argparse.ArgumentParser(description='Run short pilot for temporal_laplacian')
    parser.add_argument('--light-profile', action='store_true')
    parser.add_argument('--stop-on-error', action='store_true')
    args = parser.parse_args()

    info = base_mod.load_data_availability()
    availability = info.get('availability', {})
    data = info.get('data', {})

    defs = build_defs(availability)

    completed = []
    failed = []
    for it in defs:
        try:
            print(f"Running pilot iteration: {it.key} on datasets: {it.datasets}")
            base_mod._run_iteration(it, availability, data, operational_close_profile=False)
            completed.append(it.key)
            print(f"[OK] {it.key}")
        except Exception as exc:
            failed.append({'iteration': it.key, 'error': str(exc)})
            print(f"[SKIPPED] {it.key}: {exc}")
            if args.stop_on_error:
                break

    (RESULTS / 'pilot_completed_list.json').write_text(json.dumps(completed, ensure_ascii=False, indent=2), encoding='utf-8')
    if failed:
        (RESULTS / 'pilot_skipped_iterations.json').write_text(json.dumps(failed, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done. Completed:', len(completed), 'Skipped:', len(failed))


if __name__ == '__main__':
    main()
