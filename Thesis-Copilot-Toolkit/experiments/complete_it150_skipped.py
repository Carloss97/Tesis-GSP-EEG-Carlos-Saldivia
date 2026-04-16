"""
complete_it150_skipped.py

Attempt to complete iterations listed in `it150_skipped_iterations.json` inside
`results_rms_full150`. Tries to load missing datasets using proxies/synthetics
and re-run the missing IterDefs using the same engine as `run_full_150_normalized.py`.

Usage:
  $env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'; $env:PYTHONPATH='Thesis-Copilot-Toolkit'; \
    & .venv\Scripts\python.exe Thesis-Copilot-Toolkit\experiments\complete_it150_skipped.py --light-profile

"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Import the bulk runner module to access build_defs and base_mod
RUNNER_PATH = ROOT / 'experiments' / 'run_full_150_normalized.py'
spec = importlib.util.spec_from_file_location('bulk_mod', str(RUNNER_PATH))
bulk_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
assert loader is not None
sys.modules[spec.name] = bulk_mod
loader.exec_module(bulk_mod)

RESULTS = getattr(bulk_mod, 'RESULTS', ROOT / 'results_rms_full150')
SKIP_FILE = RESULTS / 'it150_skipped_iterations.json'


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
                raise RuntimeError(f'No loader available for dataset key: {key}')

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

    if not SKIP_FILE.exists():
        print('No skip file found at', SKIP_FILE)
        return

    skipped = json.loads(SKIP_FILE.read_text(encoding='utf-8'))
    if not skipped:
        print('No skipped iterations to process.')
        return

    # Rebuild defs and index by key
    defs = bulk_mod.build_defs(n=args.n)
    defs_by_key = {d.key: d for d in defs}

    # Load base engine availability/data
    base_mod = bulk_mod.base_mod
    check = base_mod.load_data_availability()
    availability = check.get('availability', {})
    data = check.get('data', {})

    from src.data import data_loader as dl  # type: ignore

    remaining = []
    for entry in skipped:
        iter_name = entry.get('iteration')
        it = defs_by_key.get(iter_name)
        if it is None:
            print(f'Definition not found for {iter_name}; skipping')
            remaining.append({'iteration': iter_name, 'error': 'definition_not_found'})
            continue

        # Ensure datasets exist
        ds_ok = True
        for ds_key in it.datasets:
            ok = ensure_dataset(dl, availability, data, ds_key)
            if not ok:
                ds_ok = False

        if not ds_ok:
            remaining.append({'iteration': iter_name, 'error': 'datasets_not_available'})
            continue

        try:
            it_run = replace(it, seeds=[0, 1]) if args.light_profile else it
            base_mod._run_iteration(it_run, availability, data, operational_close_profile=False)
            print(f'[OK] {iter_name}')
        except Exception as exc:
            print(f'[FAILED] {iter_name}: {exc}')
            remaining.append({'iteration': iter_name, 'error': str(exc)})

    SKIP_FILE.write_text(json.dumps(remaining, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Done. Remaining skipped: {len(remaining)}')


if __name__ == '__main__':
    main()
