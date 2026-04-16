"""
Re-run skipped pilot iterations using proxies or synthetic datasets when
the originally requested real dataset was unavailable.

This script reads `results_pilot_960/pilot_skipped_iterations.json`, rebuilds
the pilot IterDefs from `run_pilot_960.py`, substitutes blocked datasets with
proxies/synthetic data and calls the base engine `_run_iteration` to emit
artifacts into the same results folder.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Dict, Any, List

ROOT = Path(__file__).resolve().parents[1]

# load base engine module
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'
spec_base = importlib.util.spec_from_file_location('base_mod', str(BASE_SCRIPT))
base_mod = importlib.util.module_from_spec(spec_base)
loader = spec_base.loader
import sys as _sys
_sys.modules[spec_base.name] = base_mod
assert loader is not None
loader.exec_module(base_mod)

# load pilot defs builder
PILOT_SCRIPT = ROOT / 'experiments' / 'run_pilot_960.py'
spec_p = importlib.util.spec_from_file_location('pilot_mod', str(PILOT_SCRIPT))
pilot_mod = importlib.util.module_from_spec(spec_p)
loader_p = spec_p.loader
_sys.modules[spec_p.name] = pilot_mod
assert loader_p is not None
loader_p.exec_module(pilot_mod)

from src.data.data_loader import (
    load_mne_sample_proxy,
    load_bci_competition_proxy,
    load_synthetic_eeg,
)

RESULTS = ROOT / 'results_pilot_960'
SKIPPED_PATH = RESULTS / 'pilot_skipped_iterations.json'


def main():
    if not SKIPPED_PATH.exists():
        print('No skipped list found at', SKIPPED_PATH)
        raise SystemExit(1)

    skipped = json.loads(SKIPPED_PATH.read_text(encoding='utf-8'))
    defs = pilot_mod.build_defs(seeds_count=5)
    defs_map = {d.key: d for d in defs}

    check = base_mod.load_data_availability()
    availability: Dict[str, Any] = check.get('availability', {})
    data: Dict[str, Any] = check.get('data', {})

    failures = []
    successes: List[str] = []

    for item in skipped:
        key = item.get('iteration')
        it = defs_map.get(key)
        if it is None:
            failures.append({'iteration': key, 'error': 'IterDef not found'})
            print('[MISSING-DEF]', key)
            continue

        # build replacement dataset list
        new_ds = []
        for ds in it.datasets:
            if availability.get(ds, {}).get('ok'):
                new_ds.append(ds)
                continue

            # attempt sensible fallbacks
            if 'physionet' in ds:
                if availability.get('mne_sample', {}).get('ok'):
                    new_ds.append('mne_sample')
                else:
                    p = load_mne_sample_proxy()
                    k = f'mne_sample_proxy_for_{key}'
                    data[k] = p
                    availability[k] = {'ok': True, 'shape': list(p['signals'].shape)}
                    new_ds.append(k)
                continue

            if ds.startswith('bci_iv2a'):
                try:
                    p = load_bci_competition_proxy(subject=1)
                    k = f'bci_proxy_for_{key}'
                    data[k] = p
                    availability[k] = {'ok': True, 'shape': list(p['signals'].shape)}
                    new_ds.append(k)
                except Exception:
                    # fallback synthetic
                    p = load_synthetic_eeg(n_channels=16)
                    k = f'synthetic_for_{key}'
                    data[k] = p
                    availability[k] = {'ok': True, 'shape': list(p['signals'].shape)}
                    new_ds.append(k)
                continue

            # generic fallback: synthetic EEG
            p = load_synthetic_eeg(n_channels=16)
            k = f'synthetic_for_{key}'
            data[k] = p
            availability[k] = {'ok': True, 'shape': list(p['signals'].shape)}
            new_ds.append(k)

        # create a runable IterDef with replacement datasets
        it_run = replace(it, datasets=new_ds)
        try:
            base_mod._run_iteration(it_run, availability, data, operational_close_profile=False)
            successes.append(key)
            print('[OK-RERUN]', key)
        except Exception as exc:
            failures.append({'iteration': key, 'error': str(exc)})
            print('[FAILED-RERUN]', key, exc)

    # write summary
    (RESULTS / 'pilot_rerun_summary.json').write_text(json.dumps({'success': successes, 'failures': failures}, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Rerun completed. Success:', len(successes), 'Failed:', len(failures))


if __name__ == '__main__':
    main()
