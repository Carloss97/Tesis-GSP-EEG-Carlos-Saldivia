"""
Run a large screening sweep (~2000 iterations) with light repeats to filter
method-family candidates. This is the screening-stage: wide coverage, low
repetitions per config. Artifacts are written to `results_screening_2000`.

Usage (from repo root):
  $env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'; $env:PYTHONPATH='Thesis-Copilot-Toolkit'; \
    & .venv\Scripts\python.exe Thesis-Copilot-Toolkit\experiments\run_screening_2000.py --light-profile --n 2000
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'
spec = importlib.util.spec_from_file_location('base_mod', str(BASE_SCRIPT))
base_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
import sys as _sys
_sys.modules[spec.name] = base_mod
assert loader is not None
loader.exec_module(base_mod)

IterDef = base_mod.IterDef

RESULTS = ROOT / 'results_screening_2000'
base_mod.RESULTS = RESULTS
RESULTS.mkdir(parents=True, exist_ok=True)


def build_defs(n: int = 2000) -> List[IterDef]:
    ds_reals = [
        'mne_sample',
        'physionet_real',
        'bci_iv2a_real_s1',
        'bci_iv2a_real_s2',
        'bci_iv2a_real_s3',
    ]
    ds_others = [
        'iv100hz_mat',
        'iris_graph_signal',
        'movielens_graph_signal',
        'synthetic_alpha',
        'synthetic_beta',
        'synthetic_broad',
        'synthetic_16ch',
    ]
    ds_pool = ds_reals + ds_others

    graph_specs: List[Tuple[str, Dict[str, Any]]] = [
        ('knn', {'k': 3}),
        ('knn', {'k': 5}),
        ('knn', {'k': 7}),
        ('gaussian', {'sigma': 1.0}),
        ('gaussian', {'sigma': 0.6}),
        ('kalofolias', {}),
        ('knng', {'k': 4, 'sigma': 1.0}),
        ('vknng', {'k': 4}),
        ('aew', {'k': 4}),
    ]

    missing_list_pool = ['1ch', '2ch', '3ch', [0.1], [0.2], [0.3], [0.4]]
    modes = ['base', 'lambda', 'noise']

    defs: List[IterDef] = []
    idx = 0
    i = 0
    while idx < n:
        ds = ds_pool[i % len(ds_pool)]
        g = graph_specs[(i // len(ds_pool)) % len(graph_specs)]
        miss = missing_list_pool[(i // (len(ds_pool) * len(graph_specs))) % len(missing_list_pool)]
        mode = modes[(i // (len(ds_pool) * len(graph_specs) * len(missing_list_pool))) % len(modes)]

        key = f"scr_{idx+1:05d}"
        tag = key
        desc = f"Screening {key} ds={ds} graph={g[0]} miss={miss} mode={mode}"

        seeds = list(range(3))
        lambdas = [0.05, 0.1, 0.2]
        snr_levels = [25.0, 15.0, 5.0]

        it = IterDef(
            key,
            tag,
            desc,
            'Screening',
            'Auto-generated screening iteration',
            [ds],
            mode=mode,
            missing_list=miss if isinstance(miss, list) else [miss],
            seeds=seeds,
            graph_specs=[g],
            lambdas=lambdas,
            snr_levels=snr_levels,
            methods=None,
        )
        defs.append(it)
        idx += 1
        i += 1

    return defs


def main():
    parser = argparse.ArgumentParser(description='Run screening-stage bulk iterations')
    parser.add_argument('--light-profile', action='store_true')
    parser.add_argument('--stop-on-error', action='store_true')
    parser.add_argument('--n', type=int, default=2000, help='Number of iterations to generate')
    args = parser.parse_args()

    defs = build_defs(n=args.n)

    check = base_mod.load_data_availability()
    availability = check.get('availability', {})
    data = check.get('data', {})

    failed = []
    completed = []
    for it in defs:
        try:
            it_run = replace(it, seeds=[0, 1]) if args.light_profile else it
            base_mod._run_iteration(it_run, availability, data, operational_close_profile=False)
            completed.append(it.key)
            print(f"[OK] {it.key}")
        except Exception as exc:
            failed.append({'iteration': it.key, 'error': str(exc)})
            print(f"[SKIPPED] {it.key}: {exc}")
            if args.stop_on_error:
                break

    if failed:
        (RESULTS / 'screening_skipped_iterations.json').write_text(json.dumps(failed, ensure_ascii=False, indent=2), encoding='utf-8')
    (RESULTS / 'screening_completed_list.json').write_text(json.dumps(completed, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done. Completed:', len(completed), 'Skipped:', len(failed))


if __name__ == '__main__':
    main()
