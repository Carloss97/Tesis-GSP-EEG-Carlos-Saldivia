import sys
from pathlib import Path
import warnings
import numpy as np

ROOT = Path('.').resolve()
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_mne_sample_dataset, load_bci_competition_iv_2a
from src.interpolation_methods import interpolate_signals
from experiments.run_optuna_optimization import simulate_mask
import pandas as pd
import ast
from src.graph_construction.graph_constructors import build_graph

df = pd.read_csv('results_optuna_final/optuna_best_results.csv')

def run_comparison(dataset_name, load_func, missing_val, missing_mode):
    print(f'\n=== {dataset_name} | {missing_mode} | {missing_val} ===')
    data = load_func()
    signals_clean = data['signals'][:1000]
    positions = data['positions']
    sfreq = data['info'].get('sfreq', 250.0)
    
    signals_missing = simulate_mask(signals_clean, positions, missing_val, missing_mode, random_state=42)
    nan_mask = np.isnan(signals_missing)
    
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        res_mne = interpolate_signals('mne_bads', signals_missing, positions=positions, sfreq=sfreq, interpolate_method='MNE')
        
    row_trss = df[(df['dataset'] == dataset_name) & (df['missing_mode'] == missing_mode) & (df['missing_val'] == missing_val) & (df['method'] == 'trss')].iloc[0]
    p_trss = ast.literal_eval(row_trss['params'])
    
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        g = build_graph('knng', positions, signals=signals_clean, k=p_trss['k'], sigma=p_trss['sigma'])
        adj = g['adjacency'].toarray() if hasattr(g['adjacency'], 'toarray') else np.asarray(g['adjacency'])
        res_trss = interpolate_signals('trss', signals_missing, adjacency=adj, alpha=p_trss['alpha'], beta=p_trss['beta'], lr=0.05, n_iter=80)
        
    def mae(y_true, y_pred, mask):
        return np.mean(np.abs(y_true[mask] - y_pred[mask]))
        
    def rmse(y_true, y_pred, mask):
        return np.sqrt(np.mean((y_true[mask] - y_pred[mask])**2))
        
    met_mne_mae = mae(signals_clean, res_mne['reconstructed'], nan_mask)
    met_trss_mae = mae(signals_clean, res_trss['reconstructed'], nan_mask)
    
    print('MNE Bads (via spherical spline in optuna):')
    row_mne = df[(df['dataset'] == dataset_name) & (df['missing_mode'] == missing_mode) & (df['missing_val'] == missing_val) & (df['method'] == 'spherical_spline')].iloc[0]
    print(f"  MAE (Optuna Baseline): {row_mne['mae']:.6f}")
    print(f"  RMSE (Optuna Baseline): {row_mne['rmse']:.6f}")
    print(f"  DTW (Optuna Baseline): {row_mne['dtw']:.6f}")
    print(f"  LSD (Optuna Baseline): {row_mne['lsd']:.6f}")
    
    print('TRSS:')
    print(f"  MAE (Optuna Baseline): {row_trss['mae']:.6f}")
    print(f"  RMSE (Optuna Baseline): {row_trss['rmse']:.6f}")
    print(f"  DTW (Optuna Baseline): {row_trss['dtw']:.6f}")
    print(f"  LSD (Optuna Baseline): {row_trss['lsd']:.6f}")

run_comparison('mne_sample', load_mne_sample_dataset, 0.4, 'nearby')
run_comparison('bci_iv', load_bci_competition_iv_2a, 0.4, 'nearby')
