"""
Run a bulk of 150 normalized iterations combining real EEG datasets (MNE, Physionet, BCI),
other datasets and a diverse set of graph constructors and methods.

Usage (from repo root):
  $env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'; $env:PYTHONPATH='Thesis-Copilot-Toolkit'; \
    & .venv\Scripts\python.exe Thesis-Copilot-Toolkit\experiments\run_full_150_normalized.py

Options:
  --light-profile    Reduce seeds/scenarios for quick validation
  --stop-on-error    Stop at first failure
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Any, List, Tuple, Dict

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

RESULTS = ROOT / 'results_rms_full150'
base_mod.RESULTS = RESULTS
RESULTS.mkdir(parents=True, exist_ok=True)


def build_defs(n: int = 150) -> List[IterDef]:
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
        ('gaussian', {'sigma': 1.0}),
        ('gaussian', {'sigma': 0.6}),
        ('kalofolias', {}),
        ('knng', {'k': 4, 'sigma': 1.0}),
        ('vknng', {'k': 4}),
        ('aew', {'k': 4}),
    ]

    missing_list_pool = [[0.1], [0.2], [0.3], [0.4]]
    modes = ['base', 'lambda', 'noise']

    defs: List[IterDef] = []
    idx = 0
    i = 0
    while idx < n:
        ds = ds_pool[i % len(ds_pool)]
        g = graph_specs[(i // len(ds_pool)) % len(graph_specs)]
        miss = missing_list_pool[(i // (len(ds_pool) * len(graph_specs))) % len(missing_list_pool)]
        mode = modes[(i // (len(ds_pool) * len(graph_specs) * len(missing_list_pool))) % len(modes)]

        key = f"it150_{idx+1:03d}"
        tag = key
        desc = f"Bulk normalized run {key} dataset={ds} graph={g[0]} miss={miss} mode={mode}"

        seeds = list(range(6))
        lambdas = [0.05, 0.1, 0.2, 0.4]
        snr_levels = [25.0, 15.0, 5.0]

        it = IterDef(
            key,
            tag,
            desc,
            'BulkRun',
            'Auto-generated bulk normalized run',
            [ds],
            mode=mode,
            missing_list=miss,
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
    parser = argparse.ArgumentParser(description='Run 150 normalized bulk iterations')
    parser.add_argument('--light-profile', action='store_true')
    parser.add_argument('--stop-on-error', action='store_true')
    parser.add_argument('--n', type=int, default=150, help='Number of iterations to generate (default:150)')
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
        (RESULTS / 'it150_skipped_iterations.json').write_text(json.dumps(failed, ensure_ascii=False, indent=2), encoding='utf-8')
    (RESULTS / 'it150_completed_list.json').write_text(json.dumps(completed, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done. Completed:', len(completed), 'Skipped:', len(failed))


if __name__ == '__main__':
    main()
