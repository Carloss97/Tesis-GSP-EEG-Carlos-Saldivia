import sys
from pathlib import Path
import warnings
import numpy as np
import pandas as pd
import ast
from scipy.spatial.distance import cdist

ROOT = Path('.').resolve()
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_physionet_eegmmidb, load_mne_sample_dataset, load_bci_competition_proxy
from src.interpolation_methods import interpolate_signals
from src.evaluation.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph

df = pd.read_csv('results_optuna_final/optuna_best_results.csv')

def simulate_static_mask(signals, positions, missing_val, mode, random_state=42):
    N, D = signals.shape
    if isinstance(missing_val, float) and missing_val < 1.0:
        n_missing = max(1, int(round(D * missing_val)))
    else:
        n_missing = int(missing_val)
        
    rng = np.random.default_rng(random_state)
    signals_masked = signals.copy()
    
    if mode == 'random':
        bad_idx = rng.choice(D, n_missing, replace=False)
    else: # nearby
        dists = cdist(positions, positions)
        center_idx = rng.choice(D)
        bad_idx = np.argsort(dists[center_idx])[:n_missing]
        
    signals_masked[:, bad_idx] = np.nan
    nan_mask = np.isnan(signals_masked)
    return signals_masked, nan_mask, bad_idx

datasets = {
    'physionet': load_physionet_eegmmidb,
    'mne_sample': load_mne_sample_dataset,
    'bci_iv': load_bci_competition_proxy
}

missing_vals = [0.1, 0.4]
missing_modes = ['random', 'nearby']

results = []

for d_name, loader in datasets.items():
    print(f"\nLoading {d_name}...")
    data = loader()
    signals_clean = data['signals'][:4000] # Use enough samples for reliable PSD/LSD
    positions = data['positions']
    sfreq = data['info'].get('sfreq', 250.0)
    
    for m_mode in missing_modes:
        for m_val in missing_vals:
            print(f"  Evaluating {d_name} | {m_mode} | {m_val}...")
            signals_missing, nan_mask, bad_idx = simulate_static_mask(signals_clean, positions, m_val, m_mode, random_state=42)
            
            # 1. MNE interpolate_bads
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                res_mne = interpolate_signals('mne_bads', signals_missing, positions=positions, sfreq=sfreq, interpolate_method='MNE')
            met_mne = evaluate_signals(signals_clean[:, bad_idx], res_mne['reconstructed'][:, bad_idx], metrics=['mae', 'lsd'], sfreq=sfreq)
            
            # 2. TRSS (Default)
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                g_def = build_graph('knn', positions, k=4)
                adj_def = g_def['adjacency'].toarray() if hasattr(g_def['adjacency'], 'toarray') else np.asarray(g_def['adjacency'])
                res_trss_def = interpolate_signals('trss', signals_missing, adjacency=adj_def, alpha=1.0, beta=0.1, lr=0.01, n_iter=100)
            met_trss_def = evaluate_signals(signals_clean[:, bad_idx], res_trss_def['reconstructed'][:, bad_idx], metrics=['mae', 'lsd'], sfreq=sfreq)
            
            # 3. TRSS (Optimized)
            try:
                row_trss = df[(df['dataset'] == d_name) & (df['missing_mode'] == m_mode) & (df['missing_val'] == m_val) & (df['method'] == 'trss')].iloc[0]
                p_trss = ast.literal_eval(row_trss['params'])
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    g_opt = build_graph('knng', positions, signals=signals_clean, k=p_trss.get('k', 4), sigma=p_trss.get('sigma', 1.0))
                    adj_opt = g_opt['adjacency'].toarray() if hasattr(g_opt['adjacency'], 'toarray') else np.asarray(g_opt['adjacency'])
                    res_trss_opt = interpolate_signals('trss', signals_missing, adjacency=adj_opt, alpha=p_trss['alpha'], beta=p_trss['beta'], lr=0.05, n_iter=80)
                met_trss_opt = evaluate_signals(signals_clean[:, bad_idx], res_trss_opt['reconstructed'][:, bad_idx], metrics=['mae', 'lsd'], sfreq=sfreq)
            except Exception as e:
                print(f"    Error in TRSS opt: {e}")
                met_trss_opt = {'mae': np.nan, 'lsd': np.nan}
                
            results.append({
                'dataset': d_name, 'mode': m_mode, 'loss': m_val,
                'MNE_MAE': met_mne['mae'], 'MNE_LSD': met_mne['lsd'],
                'TRSS_def_MAE': met_trss_def['mae'], 'TRSS_def_LSD': met_trss_def['lsd'],
                'TRSS_opt_MAE': met_trss_opt['mae'], 'TRSS_opt_LSD': met_trss_opt['lsd']
            })

df_res = pd.DataFrame(results)
print("\n" + "="*120)
print(df_res.to_string(index=False))
print("="*120)
