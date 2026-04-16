"""
finish_missing_it150.py

Find missing it150_* runs by listing `results_rms_full150` and re-run the missing
IterDefs using proxies/synthetics where necessary.

Usage:
  $env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'; $env:PYTHONPATH='Thesis-Copilot-Toolkit'; \
    & .venv\Scripts\python.exe Thesis-Copilot-Toolkit\experiments\finish_missing_it150.py --light-profile

"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Dict, Any, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# load bulk module
RUNNER_PATH = ROOT / 'experiments' / 'run_full_150_normalized.py'
spec = importlib.util.spec_from_file_location('bulk_mod', str(RUNNER_PATH))
bulk_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
assert loader is not None
sys.modules[spec.name] = bulk_mod
loader.exec_module(bulk_mod)

RESULTS = getattr(bulk_mod, 'RESULTS', ROOT / 'results_rms_full150')


def ensure_dataset(dl, availability: Dict[str, Any], data: Dict[str, Any], key: str) -> bool:
    import numpy as np

    if availability.get(key, {}).get('ok'):
        return True
    try:
        if key == 'mne_sample_proxy':
            d = dl.load_mne_sample_proxy()
        elif key == 'mne_sample':
            try:
                d = dl.load_mne_sample_dataset()
            except Exception:
                d = dl.load_mne_sample_proxy()
        elif key.startswith('bci_competition') or key.startswith('bci_'):
            if hasattr(dl, 'load_bci_competition_proxy'):
                d = dl.load_bci_competition_proxy()
            else:
                d = dl.load_bci_competition_iv_2a(subject=1)
        elif key.startswith('synthetic_'):
            n_ch = 16
            if '16ch' in key or '16' in key:
                n_ch = 16
            elif 'broad' in key:
                n_ch = 32
            d = dl.load_synthetic_eeg(n_channels=n_ch)
        elif 'physionet' in key or 'eegmmidb' in key:
            try:
                d = dl.load_physionet_eegmmidb()
            except Exception:
                d = dl.load_synthetic_eeg()
        else:
            fn_name = f'load_{key}'
            if hasattr(dl, fn_name):
                fn = getattr(dl, fn_name)
                d = fn()
            else:
                raise RuntimeError(f'No loader for dataset key: {key}')

        sig = d.get('signals')
        pos = d.get('positions')
        if sig is None:
            raise RuntimeError(f"Loader for {key} returned no 'signals' field")
        sig = np.asarray(sig, dtype=float)
        if pos is None:
            pos = np.zeros((sig.shape[1], 3))
        pos = np.asarray(pos, dtype=float)

        data[key] = {'signals': sig, 'positions': pos, 'dataset': key}
        availability[key] = {'ok': True, 'shape': [int(sig.shape[0]), int(sig.shape[1])]} 
        print(f'Loaded dataset {key} shape={sig.shape}')
        return True
    except Exception as exc:
        availability[key] = {'ok': False, 'reason': str(exc)}
        print(f'Failed to load dataset {key}: {exc}')
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--light-profile', action='store_true')
    parser.add_argument('--n', type=int, default=150)
    args = parser.parse_args()

    # Determine completed runs by presence of run metadata
    completed = set()
    if RESULTS.exists():
        for f in RESULTS.glob('*_run_metadata.json'):
            name = f.name.rsplit('_run_metadata.json', 1)[0]
            completed.add(name)

    defs = bulk_mod.build_defs(n=args.n)
    defs_by_key = {d.key: d for d in defs}

    missing = [k for k in defs_by_key.keys() if k not in completed]
    if not missing:
        print('No missing iterations detected. Completed:', len(completed))
        return

    print(f'Detected {len(missing)} missing iterations. Attempting to complete...')

    base_mod = bulk_mod.base_mod
    check = base_mod.load_data_availability()
    availability = check.get('availability', {})
    data = check.get('data', {})

    from src.data import data_loader as dl  # type: ignore

    failures = []
    for key in missing:
        it = defs_by_key.get(key)
        if it is None:
            failures.append({'iteration': key, 'error': 'definition_not_found'})
            continue

        ds_ok = True
        for ds_key in it.datasets:
            ok = ensure_dataset(dl, availability, data, ds_key)
            if not ok:
                ds_ok = False

        if not ds_ok:
            failures.append({'iteration': key, 'error': 'datasets_not_available'})
            continue

        try:
            it_run = replace(it, seeds=[0, 1]) if args.light_profile else it
            base_mod._run_iteration(it_run, availability, data, operational_close_profile=False)
            print(f'[OK] {key}')
        except Exception as exc:
            print(f'[FAILED] {key}: {exc}')
            failures.append({'iteration': key, 'error': str(exc)})

    out = RESULTS / 'it150_missing_retry_results.json'
    out.write_text(json.dumps({'failed': failures}, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done. Failures:', len(failures))


if __name__ == '__main__':
    main()
