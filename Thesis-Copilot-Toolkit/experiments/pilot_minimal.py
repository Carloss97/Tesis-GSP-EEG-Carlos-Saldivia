"""
Minimal pilot harness implementing the chosen methods and exclusions.

Usage (from repo root, PowerShell example):
    $env:NORMALIZE_DATASETS='1'
    $env:NORM_METHOD='rms'
    & .venv/Scripts/python.exe Thesis-Copilot-Toolkit/experiments/pilot_minimal.py --stop-on-error

Notes:
- Excludes `iv100hz_mat` (100Hz dataset) and does not use `directed_tv`.
- Methods tested: `linear`, `ica`, `spherical_spline`, `rbfi_tps`, `trss`.
- Graph constructors: `nnk` and `knn`.
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
import sys as _sys
_sys.modules[spec.name] = base_mod
assert loader is not None
loader.exec_module(base_mod)

IterDef = base_mod.IterDef

RESULTS = ROOT / 'results_pilot_minimal'
RESULTS.mkdir(parents=True, exist_ok=True)


def build_defs(availability: dict) -> list[IterDef]:
    # Preferred datasets (exclude 100Hz explicitely)
    preferred = ['mne_sample', 'synthetic_16ch', 'iris_graph_signal']
    available = [k for k, v in availability.items() if v.get('ok')]
    chosen = [k for k in preferred if k in available and k != 'iv100hz_mat']
    if not chosen:
        # fallback to any available non-100hz dataset
        chosen = [k for k in available if k != 'iv100hz_mat'][:1]
    if not chosen:
        chosen = ['synthetic_16ch']

    methods = ['linear', 'ica', 'spherical_spline', 'rbfi_tps', 'trss']

    graph_specs = [('nnk', {'k': 4}), ('knn', {'k': 3})]

    it = IterDef(
        key='pilot_minimal_001',
        tag='pilot_minimal_001',
        description='Pilot mínimo: validación rápida de métodos seleccionados',
        fase='Pilot',
        objective='Comprobar comportamiento básico de ICA y TV (trss) frente a interpoladores espaciales',
        datasets=chosen,
        mode='base',
        missing_list=[0.2],
        seeds=[0, 1, 2],
        graph_specs=graph_specs,
        methods=methods,
    )
    return [it]


def main():
    parser = argparse.ArgumentParser(description='Run minimal pilot for chosen methods')
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

    (RESULTS / 'pilot_minimal_completed.json').write_text(json.dumps(completed, ensure_ascii=False, indent=2), encoding='utf-8')
    if failed:
        (RESULTS / 'pilot_minimal_skipped.json').write_text(json.dumps(failed, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done. Completed:', len(completed), 'Skipped:', len(failed))


if __name__ == '__main__':
    main()
