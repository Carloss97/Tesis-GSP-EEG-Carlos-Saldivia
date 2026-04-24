"""
run_global_hyperparams_eval.py
===============================
Evaluates TRSS with GLOBAL (fixed per-dataset) hyperparameters across all
missing-channel scenarios. This demonstrates that TRSS does NOT require
per-scenario re-optimization to maintain competitive performance.

The global hyperparameters are selected as the median of the per-scenario
optimal values found by Optuna, providing a single robust configuration.
"""

import os
import sys
import warnings
import ast
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_physionet_eegmmidb, load_bci_competition_iv_2a, load_mne_sample_dataset
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from experiments.run_optuna_optimization import simulate_mask

os.environ["BCI_IV_2A_PATH"] = str(ROOT / "datasets" / "BCICIV_2a_gdf")
os.environ["EEGBCI_LOCAL_PATH"] = str(ROOT / "datasets" / "MNE-eegbci-data")

RESULTS_DIR = ROOT / "results_optuna_final"

def get_datasets():
    datasets = {}
    try:
        data = load_physionet_eegmmidb(subject=1, run=4)
        data["signals"] = data["signals"][:2000]
        data["info"]["name"] = "physionet"
        datasets["physionet"] = data
    except Exception as e:
        print(f"[WARN] physionet: {e}")
    try:
        data = load_mne_sample_dataset()
        data["signals"] = data["signals"][:2000]
        data["info"]["name"] = "mne_sample"
        datasets["mne_sample"] = data
    except Exception as e:
        print(f"[WARN] mne_sample: {e}")
    try:
        data = load_bci_competition_iv_2a(subject=1)
        data["signals"] = data["signals"][:2000]
        data["info"]["name"] = "bci_iv"
        datasets["bci_iv"] = data
    except Exception as e:
        print(f"[WARN] bci_iv: {e}")
    return datasets

def compute_global_params(df_optuna, ds_name):
    """Compute the median hyperparameters for TRSS across all scenarios for a given dataset."""
    df_ds = df_optuna[(df_optuna["dataset"] == ds_name) & (df_optuna["method"] == "trss")]
    if df_ds.empty:
        return None
    
    all_params = []
    for _, row in df_ds.iterrows():
        try:
            p = ast.literal_eval(row["params"])
            all_params.append(p)
        except Exception:
            continue
    
    if not all_params:
        return None
    
    df_p = pd.DataFrame(all_params)
    # Use median for robustness
    global_params = {
        "k": int(round(df_p["k"].median())),
        "sigma": float(df_p["sigma"].median()),
        "alpha": float(df_p["alpha"].median()),
        "beta": float(df_p["beta"].median()),
    }
    return global_params

def main():
    csv_path = RESULTS_DIR / "optuna_best_results.csv"
    df_optuna = pd.read_csv(csv_path)
    
    SCENARIOS = [
        {"val": 0.1, "type": "ratio"},
        {"val": 0.2, "type": "ratio"},
        {"val": 0.3, "type": "ratio"},
        {"val": 0.4, "type": "ratio"},
        {"val": 1.0, "type": "count"},
        {"val": 2.0, "type": "count"},
        {"val": 3.0, "type": "count"},
    ]
    MODES = ["random", "nearby"]
    
    datasets = get_datasets()
    rows = []
    
    for ds_name, ds in datasets.items():
        signals_clean = ds["signals"]
        positions = ds["positions"]
        sfreq = ds["info"].get("sfreq", 250.0)
        
        # Compute global (fixed) hyperparameters for this dataset
        global_params = compute_global_params(df_optuna, ds_name)
        if global_params is None:
            print(f"[SKIP] No TRSS params for {ds_name}")
            continue
        
        print(f"\n=== {ds_name} ===")
        print(f"  Global params: {global_params}")
        
        # Split with buffer gap (same as optimization script)
        gap_samples = int(2.0 * sfreq)
        n_total = len(signals_clean)
        n_train_end = int(0.7 * n_total)
        n_test_start = min(n_train_end + gap_samples, n_total - 1)
        sig_clean_test = signals_clean[n_test_start:]
        
        # Build graph ONCE with global params
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            graph = build_graph("knng", positions, signals=signals_clean[:n_train_end],
                              k=global_params["k"], sigma=global_params["sigma"])
            adjacency = graph["adjacency"].toarray() if hasattr(graph["adjacency"], "toarray") else np.asarray(graph["adjacency"])
        
        for mode in MODES:
            for scen in SCENARIOS:
                val = scen["val"]
                scen_type = scen["type"]
                
                signals_missing_full = simulate_mask(signals_clean, positions, val, mode, random_state=42)
                sig_missing_test = signals_missing_full[n_test_start:]
                
                # Evaluate with GLOBAL (fixed) hyperparameters
                try:
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        res = interpolate_signals(
                            "trss", sig_missing_test, adjacency=adjacency,
                            alpha=global_params["alpha"], beta=global_params["beta"],
                            lr=0.05, n_iter=80
                        )
                    metrics = evaluate_signals(
                        sig_clean_test, res["reconstructed"],
                        metrics=["mae", "rmse", "snr", "dtw", "lsd", "coherence_mean"],
                        sfreq=sfreq
                    )
                    
                    # Also get per-scenario optimal performance for comparison
                    row_opt = df_optuna[
                        (df_optuna["dataset"] == ds_name) &
                        (df_optuna["method"] == "trss") &
                        (df_optuna["missing_mode"] == mode) &
                        (df_optuna["missing_val"] == val) &
                        (df_optuna["missing_type"] == scen_type)
                    ]
                    opt_mae = float(row_opt["mae"].iloc[0]) if not row_opt.empty else np.nan
                    opt_snr = float(row_opt["snr"].iloc[0]) if not row_opt.empty else np.nan
                    
                    rows.append({
                        "dataset": ds_name,
                        "missing_mode": mode,
                        "missing_type": scen_type,
                        "missing_val": val,
                        "global_mae": metrics["mae"],
                        "global_snr": metrics["snr"],
                        "global_lsd": metrics["lsd"],
                        "optimal_mae": opt_mae,
                        "optimal_snr": opt_snr,
                        "mae_degradation_pct": ((metrics["mae"] - opt_mae) / opt_mae * 100) if opt_mae > 0 else np.nan,
                        "snr_degradation_db": opt_snr - metrics["snr"],
                    })
                    print(f"  {mode}/{scen_type}={val}: global_MAE={metrics['mae']:.2e}, opt_MAE={opt_mae:.2e}, "
                          f"degrad={rows[-1]['mae_degradation_pct']:.1f}%")
                except Exception as e:
                    print(f"  [ERROR] {mode}/{scen_type}={val}: {e}")
    
    df = pd.DataFrame(rows)
    out_csv = RESULTS_DIR / "global_hyperparams_evaluation.csv"
    df.to_csv(out_csv, index=False)
    
    # Print summary
    if not df.empty:
        print(f"\n{'='*60}")
        print(f"SUMMARY: Global vs Per-Scenario Optimal Hyperparameters")
        print(f"{'='*60}")
        print(f"Mean MAE degradation: {df['mae_degradation_pct'].mean():.1f}%")
        print(f"Mean SNR degradation: {df['snr_degradation_db'].mean():.2f} dB")
        print(f"Global MAE (mean): {df['global_mae'].mean():.2e}")
        print(f"Optimal MAE (mean): {df['optimal_mae'].mean():.2e}")
        print(f"\nResults saved to: {out_csv}")

if __name__ == "__main__":
    main()
