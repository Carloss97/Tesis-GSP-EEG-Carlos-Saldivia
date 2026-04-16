"""
Run a pilot of ~960 normalized iterations to estimate variance and guide power
analysis. This script builds IterDefs programmatically and reuses the base
engine in `run_future_work_it121_it130.py`.

Usage (from repo root):
  $env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'; $env:PYTHONPATH='Thesis-Copilot-Toolkit'; \
    & .venv\Scripts\python.exe Thesis-Copilot-Toolkit\experiments\run_pilot_960.py --light-profile

Options:
  --light-profile    Reduce seeds for quick validation (will use seeds=[0,1])
  --stop-on-error    Stop at first failure
  --n_seeds N        Override number of seeds (default 5)
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

RESULTS = ROOT / 'results_pilot_960'
base_mod.RESULTS = RESULTS
RESULTS.mkdir(parents=True, exist_ok=True)


def build_defs(seeds_count: int = 5) -> List[IterDef]:
    # Datasets: 4 representatives (real EEG + proxy/synthetic)
    ds_pool = [
        'mne_sample',
        'physionet_real',
        'bci_iv2a_real_s1',
        'synthetic_16ch',
    ]

    graph_specs: List[Tuple[str, Dict[str, Any]]] = [
        ('knn', {'k': 3}),
        ('gaussian', {'sigma': 1.0}),
    ]

    # Missing patterns: 1/2/3 channels (use random selection here) and percentage scenarios
    missing_variants: List[Any] = [
        '1ch', '2ch', '3ch',
        [0.1], [0.2], [0.3],
    ]

    methods = ['mean', 'nearest', 'tv', 'trss']

    seeds = list(range(seeds_count))

    defs: List[IterDef] = []
    idx = 0
    for ds in ds_pool:
        for g in graph_specs:
            for miss in missing_variants:
                key = f"pilot_{idx+1:04d}"
                tag = key
                desc = f"Pilot run {key} dataset={ds} graph={g[0]} miss={miss}"

                it = IterDef(
                    key,
                    tag,
                    desc,
                    'Pilot',
                    'Auto-generated pilot iteration',
                    [ds],
                    mode='base',
                    missing_list=(miss if isinstance(miss, list) else [miss]),
                    seeds=seeds,
                    graph_specs=[g],
                    methods=methods,
                )
                defs.append(it)
                idx += 1

    return defs


def main():
    parser = argparse.ArgumentParser(description='Run pilot ~960 normalized iterations')
    parser.add_argument('--light-profile', action='store_true')
    parser.add_argument('--stop-on-error', action='store_true')
    parser.add_argument('--n_seeds', type=int, default=5)
    args = parser.parse_args()

    defs = build_defs(seeds_count=args.n_seeds)

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
        (RESULTS / 'pilot_skipped_iterations.json').write_text(json.dumps(failed, ensure_ascii=False, indent=2), encoding='utf-8')
    (RESULTS / 'pilot_completed_list.json').write_text(json.dumps(completed, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done. Completed:', len(completed), 'Skipped:', len(failed))


if __name__ == '__main__':
    main()
