import ast
import warnings
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import welch

from experiments.run_optuna_optimization import simulate_mask
from src.data.data_loader import load_physionet_eegmmidb
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals

ROOT = Path(__file__).resolve().parent


def main() -> None:
    df = pd.read_csv(ROOT / 'results_optuna_final' / 'optuna_best_results.csv')
    case = df[(df['dataset'] == 'physionet') & (df['missing_mode'] == 'random') & (df['missing_val'] == 0.1) & (df['missing_type'] == 'ratio')]
    if case.empty:
        raise SystemExit('No se encontró configuración physionet random 0.1 en optuna_best_results.csv')

    row_trss = case[case['method'] == 'trss'].iloc[0]
    row_tik = case[case['method'] == 'tikhonov'].iloc[0]
    params_trss = ast.literal_eval(row_trss['params'])
    params_tik = ast.literal_eval(row_tik['params'])

    data = load_physionet_eegmmidb(subject=1, run=4)
    signals = data['signals'][:1000]
    positions = data['positions']
    sfreq = data['info'].get('sfreq', 250.0)
    ch_names = data['info'].get('ch_names', [])

    target_name = 'Cz' if 'Cz' in ch_names else ch_names[len(ch_names) // 2]
    target_idx = ch_names.index(target_name)

    signals_missing = simulate_mask(signals, positions, 0.1, 'random', random_state=42)
    signals_missing[:, target_idx] = np.nan

    n_samples = int(1.5 * sfreq)
    time_axis = np.arange(n_samples) / sfreq
    gt_signal = signals[:n_samples, target_idx]

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        graph = build_graph('knng', positions, signals=signals, k=params_trss['k'], sigma=params_trss['sigma'])
        adjacency = graph['adjacency'].toarray() if hasattr(graph['adjacency'], 'toarray') else np.asarray(graph['adjacency'])
        sig_trss = interpolate_signals('trss', signals_missing, adjacency=adjacency, alpha=params_trss['alpha'], beta=params_trss['beta'], lr=0.05, n_iter=80)['reconstructed']

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        graph = build_graph('knng', positions, signals=signals, k=params_tik['k'], sigma=params_tik['sigma'])
        adjacency = graph['adjacency'].toarray() if hasattr(graph['adjacency'], 'toarray') else np.asarray(graph['adjacency'])
        sig_tik = interpolate_signals('tikhonov', signals_missing, adjacency=adjacency, alpha=params_tik['alpha'])['reconstructed']

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        sig_ica = interpolate_signals('ica_mne', signals_missing, positions=positions, sfreq=sfreq, ica_method='picard')['reconstructed']

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        sig_mne = interpolate_signals('mne_bads', signals_missing, positions=positions, sfreq=sfreq, interpolate_method='MNE')['reconstructed']

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        sig_ss = interpolate_signals('spherical_spline', signals_missing, positions=positions)['reconstructed']

    methods_data = [
        ('TRSS (GSP)', sig_trss, 'blue'),
        ('Tikhonov', sig_tik, 'cyan'),
        ('ICA (MNE Picard)', sig_ica, 'green'),
        ('MNE interpolate_bads', sig_mne, 'magenta'),
        ('Spherical Spline', sig_ss, 'purple'),
    ]

    metrics_rows = []
    gt_eval = gt_signal.reshape(-1, 1)
    for name, sig, _color in methods_data:
        pred_eval = sig[:n_samples, target_idx].reshape(-1, 1)
        metrics = evaluate_signals(gt_eval, pred_eval, metrics=['mae', 'lsd'])
        metrics_rows.append({'method': name, 'mae': float(metrics['mae']), 'lsd': float(metrics['lsd'])})

    metrics_df = pd.DataFrame(metrics_rows).sort_values('mae').reset_index(drop=True)
    metrics_out = ROOT / 'results_optuna_final' / 'erp_physionet_cz_random_0.1_metrics.csv'
    metrics_df.to_csv(metrics_out, index=False)

    print('\nMetric comparison (target channel, first 1.5 s):')
    print(metrics_df.to_string(index=False))

    fig_metrics, axes_metrics = plt.subplots(1, 2, figsize=(14, 5))
    for ax, metric_name, color in zip(axes_metrics, ['mae', 'lsd'], ['#4C78A8', '#F58518']):
        ordered = metrics_df.sort_values(metric_name)
        ax.barh(ordered['method'], ordered[metric_name], color=color, alpha=0.9)
        ax.set_title(metric_name.upper())
        ax.set_xlabel(metric_name.upper())
        ax.grid(True, axis='x', linestyle=':', alpha=0.5)
        ax.invert_yaxis()
    fig_metrics.suptitle(f'Metric Comparison - PhysioNet | Channel {target_name} | Random 10% Missing', fontsize=15, fontweight='bold')
    plt.tight_layout()
    metrics_plot = ROOT / 'results_optuna_final' / 'erp_physionet_cz_random_0.1_metrics.png'
    plt.savefig(metrics_plot, dpi=150, bbox_inches='tight')
    plt.close(fig_metrics)

    fig_psd, ax_psd = plt.subplots(figsize=(14, 6))
    nperseg = min(256, n_samples)
    gt_freqs, gt_psd = welch(gt_signal, fs=sfreq, nperseg=nperseg)
    ax_psd.semilogy(gt_freqs, gt_psd, color='black', linestyle='--', linewidth=2.2, label='Ground Truth')
    for name, sig, color in methods_data:
        freqs, pxx = welch(sig[:n_samples, target_idx], fs=sfreq, nperseg=nperseg)
        ax_psd.semilogy(freqs, pxx, color=color, linewidth=1.8, label=name)
    ax_psd.set_xlim(0.0, min(60.0, sfreq / 2.0))
    ax_psd.set_xlabel('Frequency (Hz)')
    ax_psd.set_ylabel('PSD')
    ax_psd.set_title(f'Comparative PSD - PhysioNet | Channel {target_name} | Random 10% Missing')
    ax_psd.grid(True, linestyle=':', alpha=0.5)
    ax_psd.legend(fontsize=9, ncol=2)
    plt.tight_layout()
    psd_plot = ROOT / 'results_optuna_final' / 'erp_physionet_cz_random_0.1_psd.png'
    plt.savefig(psd_plot, dpi=150, bbox_inches='tight')
    plt.close(fig_psd)

    fig, axes = plt.subplots(len(methods_data), 1, figsize=(14, 12), sharex=True, sharey=True)
    fig.suptitle(f'ERP Reconstruction - PhysioNet | Channel {target_name} | Random 10% Missing\nTarget electrode forced missing', fontsize=15, fontweight='bold')

    for ax, (name, sig, color) in zip(axes, methods_data):
        ax.plot(time_axis, gt_signal, label='Ground Truth', color='black', linestyle='--', linewidth=2.2, alpha=0.85)
        ax.plot(time_axis, sig[:n_samples, target_idx], label=name, color=color, linewidth=2.1)
        ax.set_ylabel('Amp. (µV)')
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(fontsize=9, loc='upper right')

    axes[-1].set_xlabel('Time (s)')
    plt.xlim(0, 1.5)
    plt.tight_layout()
    out = ROOT / 'results_optuna_final' / 'erp_physionet_cz_random_0.1.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(metrics_out)
    print(metrics_plot)
    print(psd_plot)
    print(out)


if __name__ == '__main__':
    main()
