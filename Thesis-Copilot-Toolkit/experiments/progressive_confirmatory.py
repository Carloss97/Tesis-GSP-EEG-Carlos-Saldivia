"""
progressive_confirmatory.py

Start confirmatory runs progressively from partial screening results.
This script reads `b1_b2_b3_b4.csv` from a screening results folder, picks
the top-K tags, builds confirmatory `IterDef`s and runs them into a dedicated
confirmatory results folder so analysis can start before the full screening
finishes.

Usage:
  $env:PYTHONPATH='Thesis-Copilot-Toolkit'; & .venv\Scripts\python.exe Thesis-Copilot-Toolkit\experiments\progressive_confirmatory.py --results results_screening_2000 --top-k 20 --seeds 20
"""
from __future__ import annotations

import importlib.util
import json
import sys
import time
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

# load base engine module
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'
spec = importlib.util.spec_from_file_location('base_mod', str(BASE_SCRIPT))
base_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
import sys as _sys
_sys.modules[spec.name] = base_mod
assert loader is not None
loader.exec_module(base_mod)

IterDef = base_mod.IterDef


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


def ensure_dataset(ds: str, availability: Dict[str, Any], data: Dict[str, Any], fallback_prefix: str) -> str:
    if availability.get(ds, {}).get('ok'):
        return ds
    # try mne_sample
    if availability.get('mne_sample', {}).get('ok'):
        return 'mne_sample'
    # else pick any available key
    for k, v in availability.items():
        if v.get('ok'):
            return k
    # as last resort, try to add synthetic data key if available via data loader
    try:
        from src.data.data_loader import load_synthetic_eeg

        p = load_synthetic_eeg(n_channels=16)
        key = f'synthetic_progressive_{fallback_prefix}'
        data[key] = p
        availability[key] = {'ok': True, 'shape': list(np.asarray(p['signals']).shape)}
        return key
    except Exception:
        raise RuntimeError('No datasets available to fallback')


def choose_best_method(results_dir: Path, tag: str) -> str | None:
    stats_p = results_dir / f"{tag}_stats.csv"
    raw_p = results_dir / f"{tag}_raw.csv"
    try:
        if stats_p.exists():
            df = pd.read_csv(stats_p)
            if 'mae_mean' in df.columns:
                return df.sort_values('mae_mean').iloc[0]['method']
        if raw_p.exists():
            df = pd.read_csv(raw_p)
            return df.groupby('method', as_index=False)['mae'].median().sort_values('mae').iloc[0]['method']
    except Exception:
        return None
    return None


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--results', type=str, default='results_screening_2000')
    parser.add_argument('--top-k', type=int, default=20)
    parser.add_argument('--seeds', type=int, default=20)
    parser.add_argument('--light-profile', action='store_true')
    args = parser.parse_args()

    results_dir = ROOT / args.results
    if not results_dir.exists():
        print('Results folder not found:', results_dir)
        return

    b1 = results_dir / 'b1_b2_b3_b4.csv'
    if not b1.exists():
        print('B1–B4 CSV not found in', results_dir)
        return

    df_b1 = pd.read_csv(b1)
    if 'gain_pct' in df_b1.columns:
        candidates = df_b1.sort_values('gain_pct', ascending=False)['tag'].tolist()[: args.top_k]
    else:
        candidates = df_b1['tag'].tolist()[: args.top_k]

    # load availability and data
    check = base_mod.load_data_availability()
    availability = check.get('availability', {})
    data = check.get('data', {})

    # prepare confirmatory results folder
    now = time.strftime('%Y-%m-%d_%H-%M-%S')
    confirm_dir = ROOT / f'results_confirmatory_progressive_{now}'
    confirm_dir.mkdir(parents=True, exist_ok=True)
    base_mod.RESULTS = confirm_dir

    completed = []
    failed = []

    idx = 0
    for tag in candidates:
        meta_p = results_dir / f"{tag}_run_metadata.json"
        if not meta_p.exists():
            print('Metadata not found for', tag, '- skipping')
            continue
        try:
            meta = json.loads(meta_p.read_text(encoding='utf-8'))
        except Exception as exc:
            print('Failed reading metadata for', tag, exc)
            continue

        ds_list = meta.get('datasets', [])
        if not ds_list:
            print('No datasets in metadata for', tag, '- skipping')
            continue
        ds = ds_list[0]
        ds_key = ensure_dataset(ds, availability, data, fallback_prefix=tag)

        graphs = meta.get('graphs', [])
        graph_spec = ('knn', {'k': 3})
        if graphs:
            gname, gparams = parse_graph_tag(str(graphs[0]))
            graph_spec = (gname, gparams)

        missing_ratios = meta.get('missing_ratios', [])
        mlist: List[Any] = []
        if missing_ratios:
            for m in missing_ratios:
                # keep 'Nch' style specifications as-is (handled later)
                if isinstance(m, str) and m.endswith('ch'):
                    mlist.append(m)
                    continue
                try:
                    v = float(m)
                    if not np.isfinite(v) or v <= 0:
                        # skip invalid numeric entries
                        continue
                    mlist.append(v)
                except Exception:
                    mlist.append(0.2)
        if not mlist:
            mlist = [0.2]

        best_method = choose_best_method(results_dir, tag)
        methods = [best_method] if best_method else None

        it_key = f'confirm_prog_{idx:03d}_{tag}'
        it = IterDef(
            it_key,
            it_key,
            f'Progressive confirm: {tag}',
            'Confirmatory',
            'Progressive confirmatory run from partial screening',
            [ds_key],
            mode='base',
            missing_list=mlist,
            seeds=list(range(min(args.seeds, 100))),
            graph_specs=[graph_spec],
            methods=methods,
        )

        if args.light_profile:
            it = replace(it, seeds=list(range(min(4, len(it.seeds)))), methods=it.methods or ['trss', 'tikhonov', 'linear'])

        try:
            print('[RUN]', it.key, 'dataset=', ds_key, 'graph=', graph_spec, 'methods=', it.methods)
            base_mod._run_iteration(it, availability, data, operational_close_profile=False)
            completed.append(it.key)
            print('[DONE]', it.key)
        except Exception as exc:
            print('[FAILED]', it.key, exc)
            failed.append({'iter': it.key, 'error': str(exc)})

        idx += 1

    (confirm_dir / 'confirm_prog_completed.json').write_text(json.dumps(completed, ensure_ascii=False, indent=2), encoding='utf-8')
    if failed:
        (confirm_dir / 'confirm_prog_failed.json').write_text(json.dumps(failed, ensure_ascii=False, indent=2), encoding='utf-8')

    print('Progressive confirmatory finished. Results in', confirm_dir)


if __name__ == '__main__':
    main()
