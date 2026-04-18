from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Tuple

# Ensure non-interactive backend
os.environ.setdefault('MPLBACKEND', 'Agg')

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd

from src.data.data_loader import load_physionet_eegmmidb, simulate_missing_channels
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.evaluation import evaluate_signals

RESULTS = ROOT / 'results'
RESULTS.mkdir(parents=True, exist_ok=True)

TAG = 'it11_physionet_high_missing_plus3seeds'

# Helpers (copied/adapted)

def _safe_positions(n_channels: int) -> np.ndarray:
    theta = np.linspace(0, 2 * np.pi, n_channels, endpoint=False)
    return np.stack([np.cos(theta), np.sin(theta), np.zeros(n_channels)], axis=1)


def _sample_segment(signals: np.ndarray, *, n_times: int = 320, max_ch: int = 24) -> np.ndarray:
    x = np.asarray(signals, dtype=float)
    if x.ndim != 2:
        raise ValueError(f"Expected 2D signals array, got shape={x.shape}")
    x = np.nan_to_num(x, nan=0.0, posinf=0.0, neginf=0.0)
    if x.shape[0] > n_times:
        x = x[:n_times]
    if x.shape[1] > max_ch:
        idx = np.round(np.linspace(0, x.shape[1] - 1, max_ch)).astype(int)
        x = x[:, idx]
    return x


def _stats(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby('method', as_index=False)
        .agg(
            mae_mean=('mae', 'mean'),
            mae_std=('mae', 'std'),
            mae_median=('mae', 'median'),
            time_mean_sec=('time_sec', 'mean'),
        )
        .sort_values('mae_mean')
    )


def _significance(df: pd.DataFrame) -> pd.DataFrame:
    INSTANT_METHODS = ['mean', 'nearest', 'tikhonov']
    TV_METHODS = ['tv', 'trss', 'graph_time_tikhonov', 'temporal_laplacian', 'directed_tv']
    tv = df[df['method'].isin(TV_METHODS)]['mae'].to_numpy()
    inst = df[df['method'].isin(INSTANT_METHODS)]['mae'].to_numpy()
    if len(tv) == 0 or len(inst) == 0:
        return pd.DataFrame([
            {
                'comparison': 'TV_vs_Instant',
                'tv_median': np.nan,
                'instant_median': np.nan,
                'u_statistic': np.nan,
                'p_value': 1.0,
                'decision': 'NO-GO',
                'gain_pct': 0.0,
            }
        ])
    from scipy.stats import mannwhitneyu
    u, p = mannwhitneyu(tv, inst, alternative='less')
    tv_m = float(np.median(tv))
    in_m = float(np.median(inst))
    gain = float(((in_m - tv_m) / in_m) * 100.0) if in_m != 0 else 0.0
    decision = 'GO' if (p < 0.05 and gain > 0) else 'NO-GO'
    return pd.DataFrame([
        {
            'comparison': 'TV_vs_Instant',
            'tv_median': tv_m,
            'instant_median': in_m,
            'u_statistic': float(u),
            'p_value': float(p),
            'decision': decision,
            'gain_pct': gain,
        }
    ])


def _write_figures(tag: str, df: pd.DataFrame):
    rfig = RESULTS / f"{tag}_figures"
    rfig.mkdir(parents=True, exist_ok=True)
    method_stats = df.groupby('method', as_index=False)['mae'].mean().sort_values('mae')
    import matplotlib.pyplot as plt

    # fig02: RMSE boxplot
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    order = method_stats['method']
    ax.boxplot([df[df['method'] == m]['rmse'].values for m in order], labels=order, vert=False)
    ax.set_title('RMSE by method')
    fig.tight_layout()
    fig.savefig(rfig / 'fig02_rmse_boxplot.pdf')
    plt.close(fig)

    # fig05: TV vs Instant median MAE by missing_ratio
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    fam = df.copy()
    tv_methods = ['tv', 'trss', 'graph_time_tikhonov', 'temporal_laplacian', 'directed_tv', 'wavelet_temporal']
    fam['family'] = np.where(fam['method'].isin(tv_methods), 'TV', 'Instant')
    g = fam.groupby(['family', 'missing_ratio'], as_index=False)['mae'].median()
    for f in g['family'].unique():
        s = g[g['family'] == f]
        ax.plot(s['missing_ratio'].astype(str), s['mae'], marker='o', label=f)
    ax.legend(fontsize=7)
    ax.set_title('TV vs Instant')
    fig.tight_layout()
    fig.savefig(rfig / 'fig05_tv_vs_instant_family.pdf')
    plt.close(fig)


def main():
    # Load existing metadata to mirror configuration
    meta_path = RESULTS / 'it11_physionet_high_missing_run_metadata.json'
    if not meta_path.exists():
        print('Original metadata for it11 not found:', meta_path)
        sys.exit(1)
    meta = json.loads(meta_path.read_text(encoding='utf-8'))
    methods = meta.get('methods_used') or meta.get('methods') or []

    # Graph specs approximate (match original graphs_used intent)
    graph_specs = [
        ('aew', {'k': 4, 'sigma_dist': 1.0, 'sigma_corr': 0.5}),
        ('gaussian', {'sigma': 1.0}),
        ('kalofolias', {}),
        ('knn', {'k': 3}),
        ('knn', {'k': 5}),
        ('knng', {'k': 4, 'sigma': 1.0}),
        ('nnk', {'k': 4}),
        ('vknng', {'alpha': 1.0, 'k': 4, 'k_min': 2, 'k_max': 8}),
    ]

    seeds = [0, 1, 2, 3]  # original was 1 seed; we add 3 extra (total 4)
    missing_list = [0.4]

    # Load physionet data
    try:
        d = load_physionet_eegmmidb(subject=1, run=4)
    except Exception as exc:
        print('Failed to load physionet data:', exc)
        sys.exit(2)

    x = np.asarray(d['signals'], dtype=float)
    pos = np.asarray(d.get('positions'), dtype=float)
    x = _sample_segment(x, n_times=320, max_ch=24)
    # Align `pos` to the possibly subsampled `x` channels to avoid adjacency shape mismatch
    if pos.ndim != 2:
        pos = _safe_positions(x.shape[1])
    if pos.shape[0] != x.shape[1]:
        idx = np.round(np.linspace(0, pos.shape[0] - 1, x.shape[1])).astype(int)
        pos = pos[idx]

    rows: List[Dict[str, Any]] = []

    for graph_method, graph_params in graph_specs:
        gobj = build_graph(graph_method, pos, signals=x, **graph_params)
        adj = np.asarray(gobj['adjacency'])
        graph_tag = graph_method if graph_params == {} else graph_method

        for miss in missing_list:
            for seed in seeds:
                masked = simulate_missing_channels(x, missing_ratio=miss, random_state=seed)
                for method in methods:
                    kwargs = {}
                    if method == 'tikhonov':
                        kwargs['alpha'] = 0.1
                    elif method == 'tv':
                        kwargs.update({'lam': 0.2, 'n_iter': 30})
                    elif method == 'trss':
                        kwargs.update({'alpha': 0.7, 'beta': 0.2, 'n_iter': 60, 'lr': 0.03})
                    elif method == 'graph_time_tikhonov':
                        kwargs.update({'alpha': 0.5, 'beta': 0.1})
                    elif method == 'temporal_laplacian':
                        kwargs.update({'alpha': 0.5, 'beta': 0.5})

                    t0 = time.perf_counter()
                    try:
                        rec = interpolate_signals(method, masked, adjacency=adj, positions=pos, **kwargs)['reconstructed']
                    except Exception as exc:
                        rows.append({
                            'dataset': 'physionet_eegmmidb',
                            'graph': graph_tag,
                            'method': method,
                            'missing_ratio': miss,
                            'seed': int(seed),
                            'mae': float('nan'),
                            'rmse': float('nan'),
                            'snr': float('nan'),
                            'dtw': float('nan'),
                            'params': json.dumps(kwargs, ensure_ascii=False),
                            'error': str(exc),
                            'n_missing_ch': int(round(miss * x.shape[1])),
                            'time_sec': 0.0,
                        })
                        continue
                    elapsed = time.perf_counter() - t0
                    met = evaluate_signals(x, rec, metrics=['mae', 'rmse', 'snr', 'dtw'])
                    rows.append({
                        'dataset': 'physionet_eegmmidb',
                        'graph': graph_tag,
                        'method': method,
                        'missing_ratio': miss,
                        'seed': int(seed),
                        'mae': float(met['mae']),
                        'rmse': float(met['rmse']),
                        'snr': float(met['snr']),
                        'dtw': float(met['dtw']),
                        'params': json.dumps(kwargs, ensure_ascii=False),
                        'error': '',
                        'n_missing_ch': int(round(miss * x.shape[1])),
                        'time_sec': float(elapsed),
                    })

    df = pd.DataFrame(rows)
    if df.empty:
        print('No rows generated')
        sys.exit(1)

    # Write artifacts
    (RESULTS / f"{TAG}_raw.csv").write_text(df.to_csv(index=False), encoding='utf-8')
    stats = _stats(df)
    (RESULTS / f"{TAG}_stats.csv").write_text(stats.to_csv(index=False), encoding='utf-8')
    sig = _significance(df)
    (RESULTS / f"{TAG}_significance.csv").write_text(sig.to_csv(index=False), encoding='utf-8')

    # QA report
    qa = sig.iloc[0]
    qa_md = [
        f"# QA Report — {TAG}",
        "",
        f"## Status: {qa['decision']}",
        "",
        "## Summary",
        f"- Total rows: {len(df)}",
        f"- Methods tested: {df['method'].nunique()}",
        f"- Graphs: {df['graph'].nunique()}",
        f"- Missing scenarios: {df['missing_ratio'].nunique()}",
        f"- p-value: {qa['p_value']:.4e}",
        "",
        f"Generated: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}",
    ]
    (RESULTS / f"{TAG}_qa_report.md").write_text('\n'.join(qa_md), encoding='utf-8')

    # Integration log
    il = [f"# Integration Log — {TAG}", f"Started: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}", '']
    for g in sorted(df['graph'].unique()):
        il.append(f"Graph: {g}")
    il.append('')
    il.append(f"Completed: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    (RESULTS / f"{TAG}_integration_log.md").write_text('\n'.join(il), encoding='utf-8')

    # Run metadata
    meta_out = {
        'iteration_tag': TAG,
        'run_timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'datasets': ['physionet_eegmmidb'],
        'scenarios': ['40pct'],
        'n_rows': int(len(df)),
        'methods': sorted(df['method'].unique().tolist()),
        'graphs': sorted(df['graph'].unique().tolist()),
        'seeds': seeds,
    }
    # Provide standard metadata keys required by integration and prompts
    meta_out.setdefault('normalization', None)
    meta_out.setdefault('missing_mode', None)
    (RESULTS / f"{TAG}_run_metadata.json").write_text(json.dumps(meta_out, ensure_ascii=False, indent=2), encoding='utf-8')

    # Figures
    _write_figures(TAG, df)

    print('Replication finished, artifacts written under results/')


if __name__ == '__main__':
    main()
