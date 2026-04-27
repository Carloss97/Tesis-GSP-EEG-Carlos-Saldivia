import pandas as pd
import numpy as np
import os
import ast
from pathlib import Path
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data.data_loader import load_physionet_eegmmidb, load_bci_competition_iv_2a, load_mne_sample_dataset
from src.interpolation_methods import interpolate_signals
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph

DATASETS = {
    "physionet": load_physionet_eegmmidb,
    "bci_iv": lambda: load_bci_competition_iv_2a(subject=1),
    "mne_sample": load_mne_sample_dataset
}

def simulate_mask(signals, positions, val, mode, random_state=42):
    rng = np.random.default_rng(random_state)
    n_ch = signals.shape[1]
    val_f = float(val)
    if mode == "random":
        mc = int(np.round(n_ch * val_f)) if val_f < 1.0 else int(val_f)
        idx = rng.choice(n_ch, size=min(mc, n_ch-2), replace=False)
    else:
        mc = int(np.round(n_ch * val_f)) if val_f < 1.0 else int(val_f)
        start = rng.integers(0, n_ch)
        dists = np.linalg.norm(positions - positions[start], axis=1)
        idx = np.argsort(dists)[:min(mc, n_ch-2)]
    s = signals.copy()
    s[:, idx] = np.nan
    return s

def process_csv(path):
    if not os.path.exists(path): return
    df = pd.read_csv(path)
    updated = False
    
    for i, row in df.iterrows():
        # Target mne_sample specifically or any NaNs
        if pd.isna(row.get("snr")) or row["dataset"] == "mne_sample":
            print(f"Recalculating {row['method']} for {row['dataset']} {row['missing_mode']} {row['missing_val']}...")
            try:
                ds_fn = DATASETS.get(row["dataset"])
                if not ds_fn: continue
                data = ds_fn()
                signals_full = data["signals"][:5000]
                positions = data["positions"]
                sfreq = data["info"].get("sfreq", 250.0)
                
                gap = int(2.0 * sfreq)
                n_train = int(0.7 * len(signals_full))
                n_test_start = min(n_train + gap, len(signals_full) - 1)
                
                sig_clean_test = signals_full[n_test_start:]
                if len(sig_clean_test) < 10: continue
                    
                sig_full_miss = simulate_mask(signals_full, positions, row["missing_val"], row["missing_mode"])
                sig_miss_test = sig_full_miss[n_test_start:]
                
                try:
                    params = ast.literal_eval(row["params"]) if isinstance(row["params"], str) and row["params"].startswith("{") else {}
                except:
                    params = {}
                
                method = row["method"]
                if method in ["trss", "tikhonov"]:
                    k = params.get("k", 5 if row["dataset"] != "physionet" else 8)
                    sigma = params.get("sigma", 1.0)
                    graph = build_graph("knng", positions, signals=signals_full[:n_train], k=k, sigma=sigma)
                    adj = graph["adjacency"].toarray() if hasattr(graph["adjacency"], "toarray") else np.asarray(graph["adjacency"])
                    
                    if method == "trss":
                        # Better defaults for TRSS: lower alpha/beta, more iterations
                        alpha_t = params.get("alpha", 0.01)
                        beta_t = params.get("beta", 0.005) 
                        res = interpolate_signals("trss", sig_miss_test, adjacency=adj, alpha=alpha_t, beta=beta_t, lr=0.01, n_iter=250)
                    else:
                        alpha_tik = params.get("alpha", 0.1)
                        res = interpolate_signals("tikhonov", sig_miss_test, adjacency=adj, alpha=alpha_tik)
                elif method == "spherical_spline":
                    res = interpolate_signals("spherical_spline", sig_miss_test, positions=positions, m=params.get("m", 4))
                elif method == "rbfi_tps":
                    res = interpolate_signals("rbfi_tps", sig_miss_test, positions=positions, smoothing=params.get("smoothing", 0.05))
                elif method == "ica":
                    res = interpolate_signals("ica", sig_miss_test, positions=positions)
                else:
                    continue
                
                m_test = evaluate_signals(sig_clean_test, res["reconstructed"], 
                                         metrics=["mae", "rmse", "snr", "dtw", "lsd", "coherence_mean"], sfreq=sfreq)
                
                for k_met, v_met in m_test.items():
                    df.at[i, k_met] = v_met
                updated = True
                print(f"  Success: SNR={m_test.get('snr'):.2f} MAE={m_test.get('mae'):.2e}")
            except Exception as e:
                print(f"  Error recalculating {row['method']}: {e}")
                
    if updated:
        df.to_csv(path, index=False)
        print(f"Updated {path}")

if __name__ == "__main__":
    process_csv("results_optuna_final/optuna_best_results.csv")
    process_csv("results_optuna_baselines/optuna_best_results_baselines.csv")
