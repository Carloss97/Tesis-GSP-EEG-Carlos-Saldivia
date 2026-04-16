"""
Supervisor: wait for screening results, run B1–B4, pick top-K candidates,
estimate confirmatory seeds using pilot variance, and run confirmatory
iterations automatically.

Usage (from repo root):
  $env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'; $env:PYTHONPATH='Thesis-Copilot-Toolkit'; \
    & .venv/Scripts/python.exe Thesis-Copilot-Toolkit/experiments/supervisor_screening_to_confirmatory.py

Notes:
  - Adjust `EXPECTED` and `TOP_K` below as needed.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import time
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

# Screening results to monitor
SCREENING_RESULTS = ROOT / 'results_screening_2000'
EXPECTED = 2000
POLL = 60

# Confirmatory parameters
TOP_K = 20
DEFAULT_CONFIRM_SEEDS = 34
CONFIRM_RESULTS = ROOT / f'results_confirmatory_{time.strftime("%Y-%m-%d")}'
CONFIRM_RESULTS.mkdir(parents=True, exist_ok=True)

# Load base engine
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'
spec = importlib.util.spec_from_file_location('base_mod', str(BASE_SCRIPT))
base_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
import sys as _sys
_sys.modules[spec.name] = base_mod
assert loader is not None
loader.exec_module(base_mod)

IterDef = base_mod.IterDef


def count_completed(results_dir: Path) -> int:
    return len(list(results_dir.glob('*_run_metadata.json')))


def run_generator_on(path: Path):
    cmd = [sys.executable, str(ROOT / 'experiments' / 'generate_b1_b4.py'), '--results', str(path.name)]
    print('Running generator:', ' '.join(cmd))
    subprocess.run(cmd, check=False)


def parse_graph_tag(tag: str) -> Tuple[str, Dict[str, Any]]:
    if '__' in tag:
        parts = tag.split('__')
        g = parts[0]
        params = {}
        rest = '__'.join(parts[1:])
        for token in rest.split('_'):
            if token.startswith('k') and token[1:].isdigit():
                params['k'] = int(token[1:])
            elif token.startswith('sigma'):
                try:
                    params['sigma'] = float(token.replace('sigma', ''))
                except Exception:
                    pass
        return g, params
    return tag, {}


def ensure_dataset_availability(ds: str, availability: Dict[str, Any], data: Dict[str, Any], key_prefix: str) -> str:
    # If dataset is available, return it as-is
    if availability.get(ds, {}).get('ok'):
        return ds

    # Try sensible fallback substitutions
    if 'physionet' in ds:
        if availability.get('mne_sample', {}).get('ok'):
            return 'mne_sample'
        # create a proxy entry
        p = base_mod.load_data_availability().get('data', {}).get('mne_sample')
        if p is not None:
            key = f'mne_sample_proxy_{key_prefix}'
            data[key] = p
            availability[key] = {'ok': True, 'shape': list(np.asarray(p['signals']).shape)}
            return key

    if ds.startswith('bci_iv2a'):
        # try proxy or synthetic
        try:
            from src.data.data_loader import load_bci_competition_proxy

            p = load_bci_competition_proxy(subject=1)
            key = f'bci_proxy_{key_prefix}'
            data[key] = p
            availability[key] = {'ok': True, 'shape': list(np.asarray(p['signals']).shape)}
            return key
        except Exception:
            from src.data.data_loader import load_synthetic_eeg

            p = load_synthetic_eeg(n_channels=16)
            key = f'synthetic_{key_prefix}'
            data[key] = p
            availability[key] = {'ok': True, 'shape': list(np.asarray(p['signals']).shape)}
            return key

    # Generic fallback: synthetic EEG
    from src.data.data_loader import load_synthetic_eeg

    p = load_synthetic_eeg(n_channels=16)
    key = f'synthetic_{key_prefix}'
    data[key] = p
    availability[key] = {'ok': True, 'shape': list(np.asarray(p['signals']).shape)}
    return key


def recommend_seeds_from_pilot(pilot_results_dir: Path, effect_d: float = 0.5, alpha: float = 0.05, power: float = 0.8) -> int:
    """Simple estimator using pooled sd from pilot MAE and two-sample t-test formula.
    This is an approximation; returns per-group sample size (rounded up).
    """
    # collect MAE values across pilot raw files
    maes = []
    for raw in sorted(pilot_results_dir.glob('*_raw.csv')):
        try:
            df = pd.read_csv(raw)
            maes.extend(df['mae'].dropna().values.tolist())
        except Exception:
            continue
    if not maes:
        return DEFAULT_CONFIRM_SEEDS

    sd = float(np.std(maes, ddof=1))
    # two-sample t-test sample size per group: n = 2 * ( (z_{1-alpha/2} + z_{power}) * sd / (d * sd) )^2 = 2 * (zsum / d)^2
    # cancels sd: n = 2 * (zsum / d)^2
    from math import ceil
    import scipy.stats as st

    z_alpha = st.norm.ppf(1 - alpha / 2)
    z_power = st.norm.ppf(power)
    zsum = z_alpha + z_power
    n = ceil(2 * (zsum / effect_d) ** 2)
    return max(4, min(n, 500))


def main():
    parser = base_mod.argparse.ArgumentParser()
    parser.add_argument('--screening-results', type=str, default=str(SCREENING_RESULTS))
    parser.add_argument('--expected', type=int, default=EXPECTED)
    parser.add_argument('--poll', type=int, default=POLL)
    parser.add_argument('--top-k', type=int, default=TOP_K)
    parser.add_argument('--confirm-seeds', type=int, default=DEFAULT_CONFIRM_SEEDS)
    args = parser.parse_args()

    results_dir = Path(args.screening_results)
    expected = args.expected
    poll = args.poll
    top_k = args.top_k
    confirm_seeds = args.confirm_seeds

    print('Supervisor: waiting for screening results in', results_dir)
    while True:
        done = count_completed(results_dir) if results_dir.exists() else 0
        print(f'Completed runs: {done}/{expected}')
        if done >= expected:
            print('Screening complete — generating B1–B4')
            break
        time.sleep(poll)

    run_generator_on(results_dir)

    csv_path = results_dir / 'b1_b2_b3_b4.csv'
    if not csv_path.exists():
        print('B1–B4 CSV not found, exiting')
        return

    df = pd.read_csv(csv_path)
    top_tags = df.sort_values('gain_pct', ascending=False)['tag'].tolist()[:top_k]
    print('Top tags selected for confirmatory:', top_tags)

    # load availability/data
    check = base_mod.load_data_availability()
    availability = check.get('availability', {})
    data = check.get('data', {})

    # estimate seeds from pilot
    pilot_dir = ROOT / 'results_pilot_960'
    est_n = recommend_seeds_from_pilot(pilot_dir, effect_d=0.5)
    print('Suggested per-config seeds (effect d=0.5):', est_n)
    seeds_to_use = confirm_seeds or est_n

    # Build confirmatory IterDefs and run them sequentially
    confirm_idx = 0
    for tag in top_tags:
        stats_path = results_dir / f"{tag}_stats.csv"
        meta_path = results_dir / f"{tag}_run_metadata.json"
        if not meta_path.exists():
            print('Missing metadata for', tag, ' — skipping')
            continue

        meta = json.loads(meta_path.read_text(encoding='utf-8'))
        ds_list = meta.get('datasets', [])
        graphs = meta.get('graphs', [])
        missing_ratios = meta.get('missing_ratios', [])

        if not ds_list:
            print('No datasets for', tag, ' — skipping')
            continue

        ds = ds_list[0]
        ds_key = ensure_dataset_availability(ds, availability, data, key_prefix=tag)

        # select the best method from stats
        best_method = None
        if stats_path.exists():
            try:
                sst = pd.read_csv(stats_path)
                best_method = sst.sort_values('mae_mean').iloc[0]['method']
            except Exception:
                best_method = None

        if best_method is None:
            # fallback to parse raw
            rawp = results_dir / f"{tag}_raw.csv"
            if rawp.exists():
                try:
                    rdf = pd.read_csv(rawp)
                    best_method = rdf.groupby('method', as_index=False)['mae'].median().sort_values('mae').iloc[0]['method']
                except Exception:
                    best_method = None

        if best_method is None:
            print('Could not determine best method for', tag, ' — skipping')
            continue

        graph_tag = graphs[0] if graphs else 'knn__k3'
        gname, gparams = parse_graph_tag(str(graph_tag))
        miss_list = [float(m) if isinstance(m, str) and m.replace('.', '', 1).isdigit() else m for m in missing_ratios]
        if not miss_list:
            miss_list = [0.2]

        key = f"confirm_{confirm_idx:03d}_{tag}"
        desc = f"Confirmatory run for {tag} (best_method={best_method})"

        it = IterDef(
            key,
            key,
            desc,
            'Confirmatory',
            'Auto-generated confirmatory iteration',
            [ds_key],
            mode='base',
            missing_list=miss_list,
            seeds=list(range(seeds_to_use)),
            graph_specs=[(gname, gparams)],
            methods=[best_method],
        )

        try:
            print('[RUNNING CONFIRM]', key, 'dataset=', ds_key, 'method=', best_method)
            base_mod._run_iteration(it, availability, data, operational_close_profile=False)
            print('[DONE CONFIRM]', key)
            confirm_idx += 1
        except Exception as exc:
            print('[FAILED CONFIRM]', key, exc)

    print('Confirmatory stage complete. Results in', CONFIRM_RESULTS)


if __name__ == '__main__':
    main()
