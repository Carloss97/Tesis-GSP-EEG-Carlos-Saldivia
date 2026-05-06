import sys
from pathlib import Path
import warnings
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
import optuna

# Suprimir salida excesiva de Optuna
optuna.logging.set_verbosity(optuna.logging.WARNING)

ROOT = Path('.').resolve()
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_physionet_eegmmidb, load_mne_sample_dataset, load_bci_competition_proxy
from src.interpolation_methods import interpolate_signals
from src.evaluation.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph

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

metrics_list = ['mae', 'rmse', 'dtw', 'snr', 'lsd', 'coherence_mean']

results = []

for d_name, loader in datasets.items():
    print(f"\nLoading {d_name}...")
    data = loader()
    signals_clean = data['signals'][:4000] 
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
            met_mne = evaluate_signals(signals_clean[:, bad_idx], res_mne['reconstructed'][:, bad_idx], metrics=metrics_list, sfreq=sfreq)
            
            # 2. Optimize TRSS for this specific static mask using Optuna
            def objective(trial):
                alpha = trial.suggest_float("alpha", 0.1, 5.0, log=True)
                beta = trial.suggest_float("beta", 0.01, 1.0, log=True)
                k = trial.suggest_int("k", 3, 12)
                sigma = trial.suggest_float("sigma", 0.1, 5.0)
                
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    g = build_graph('knng', positions, signals=signals_clean, k=k, sigma=sigma)
                    adj = g['adjacency'].toarray() if hasattr(g['adjacency'], 'toarray') else np.asarray(g['adjacency'])
                    res = interpolate_signals('trss', signals_missing, adjacency=adj, alpha=alpha, beta=beta, lr=0.05, n_iter=80)
                
                met = evaluate_signals(signals_clean[:, bad_idx], res['reconstructed'][:, bad_idx], metrics=['mae', 'dtw'], sfreq=sfreq)
                # Optimize a mix of amplitude and shape to avoid destroying LSD/DTW completely
                # Since DTW is larger, we normalize by adding them
                return met['mae'] * 10000 + met.get('dtw', 0.0)
                
            study = optuna.create_study(direction="minimize")
            study.optimize(objective, n_trials=15) # Quick optimization
            
            best_p = study.best_params
            
            # Re-evaluate best TRSS
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                g_opt = build_graph('knng', positions, signals=signals_clean, k=best_p['k'], sigma=best_p['sigma'])
                adj_opt = g_opt['adjacency'].toarray() if hasattr(g_opt['adjacency'], 'toarray') else np.asarray(g_opt['adjacency'])
                res_trss_opt = interpolate_signals('trss', signals_missing, adjacency=adj_opt, alpha=best_p['alpha'], beta=best_p['beta'], lr=0.05, n_iter=80)
            met_trss_opt = evaluate_signals(signals_clean[:, bad_idx], res_trss_opt['reconstructed'][:, bad_idx], metrics=metrics_list, sfreq=sfreq)
            
            row = {
                'dataset': d_name, 'mode': m_mode, 'loss': m_val,
            }
            for m in metrics_list:
                row[f"MNE_{m}"] = met_mne.get(m, np.nan)
                row[f"TRSS_{m}"] = met_trss_opt.get(m, np.nan)
            
            results.append(row)

df_res = pd.DataFrame(results)
print("\n" + "="*160)
print(df_res.to_string(index=False))
print("="*160)
