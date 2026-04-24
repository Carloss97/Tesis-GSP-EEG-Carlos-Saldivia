"""
run_optuna_baselines.py
=======================
Optimiza los hiperparámetros de los métodos baseline (Spherical Spline, RBFI, ICA)
usando Optuna (Multi-Objetivo: MAE y LSD) de forma análoga a TRSS/Tikhonov.
"""

import os
import sys
import warnings
from pathlib import Path
import logging

import numpy as np
import pandas as pd
import optuna

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.data_loader import (
    load_mne_sample_dataset,
    load_physionet_eegmmidb,
    load_bci_competition_iv_2a
)
from src.evaluation import evaluate_signals
from src.interpolation_methods import interpolate_signals

# Desactivar logs innecesarios
optuna.logging.set_verbosity(optuna.logging.WARNING)
logging.getLogger('mne').setLevel(logging.ERROR)

os.environ["BCI_IV_2A_PATH"] = str(ROOT / "datasets" / "BCICIV_2a_gdf")
os.environ["EEGBCI_LOCAL_PATH"] = str(ROOT / "datasets" / "MNE-eegbci-data")

RESULTS_DIR = ROOT / "results_optuna_baselines"
RESULTS_DIR.mkdir(exist_ok=True)

CSV_PATH = RESULTS_DIR / "optuna_best_results_baselines.csv"

def simulate_mask(signals, positions, val, mode, random_state=42):
    rng = np.random.default_rng(random_state)
    n_ch = signals.shape[1]
    
    if mode == "random":
        missing_count = int(np.round(n_ch * val)) if val < 1.0 else int(val)
        missing_count = min(missing_count, n_ch - 2)
        missing_idx = rng.choice(n_ch, size=missing_count, replace=False)
    else: # nearby
        missing_count = int(np.round(n_ch * val)) if val < 1.0 else int(val)
        missing_count = min(missing_count, n_ch - 2)
        start_idx = rng.integers(0, n_ch)
        dists = np.linalg.norm(positions - positions[start_idx], axis=1)
        missing_idx = np.argsort(dists)[:missing_count]
        
    s_miss = signals.copy()
    s_miss[:, missing_idx] = np.nan
    return s_miss

def get_best_pareto_trial(study: optuna.study.Study) -> optuna.trial.FrozenTrial:
    best_trials = study.best_trials
    if not best_trials:
        raise ValueError("No Pareto optimal trials found.")
        
    if len(best_trials) == 1:
        return best_trials[0]
        
    vals = np.array([t.values for t in best_trials])
    min_vals = vals.min(axis=0)
    max_vals = vals.max(axis=0)
    den = np.where(max_vals - min_vals == 0, 1e-6, max_vals - min_vals)
    norm_vals = (vals - min_vals) / den
    
    dists = np.linalg.norm(norm_vals, axis=1)
    best_idx = np.argmin(dists)
    return best_trials[best_idx]

def objective(trial, method, sig_clean_train, sig_clean_test, sig_missing_train, sig_missing_test, positions, sfreq):
    if method == "spherical_spline":
        eps = trial.suggest_float("eps", 1e-8, 1e-2, log=True)
        kwargs = {"positions": positions, "eps": eps}
        
    elif method == "rbfi_tps":
        smooth = trial.suggest_float("smooth", 0.0, 5.0)
        kwargs = {"positions": positions, "smooth": smooth}
        
    elif method == "ica":
        n_ch = sig_clean_train.shape[1]
        n_components = trial.suggest_int("n_components", 1, n_ch)
        kwargs = {"n_components": n_components, "random_state": 42}
        
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            # Optimize on TRAIN slice
            res_train = interpolate_signals(method, sig_missing_train, **kwargs)
            metrics_train = evaluate_signals(sig_clean_train, res_train["reconstructed"], sfreq=sfreq, metrics=["mae", "lsd"])
            
            # Record performance on TEST slice (will be used for final CSV attributes if needed)
            res_test = interpolate_signals(method, sig_missing_test, **kwargs)
            metrics_test = evaluate_signals(sig_clean_test, res_test["reconstructed"], sfreq=sfreq)
            
            trial.set_user_attr("test_mae", metrics_test["mae"])
            trial.set_user_attr("test_lsd", metrics_test["lsd"])
            trial.set_user_attr("test_snr", metrics_test["snr"])
            trial.set_user_attr("test_rmse", metrics_test["rmse"])
            trial.set_user_attr("test_dtw", metrics_test["dtw"])
            trial.set_user_attr("test_coherence_mean", metrics_test["coherence_mean"])

            if np.isnan(metrics_train["mae"]) or np.isinf(metrics_train["mae"]):
                return float("inf"), float("inf")
            return metrics_train["mae"], metrics_train["lsd"]
        except Exception:
            return float("inf"), float("inf")

def optimize_case(ds_name, data, mode, stype, val):
    print(f"\n>> {ds_name} | {mode} | {stype}={val}")
    
    sfreq = data["info"].get("sfreq", 250.0)
    signals_full = data["signals"][:1000] # Use 1000 samples for better split
    positions = data["positions"]
    
    # Split temporal data (70% train for optimization, 30% test for reporting)
    n_split = int(0.7 * len(signals_full))
    sig_clean_train = signals_full[:n_split]
    sig_clean_test = signals_full[n_split:]

    # Simulate mask on full and split
    signals_missing_full = simulate_mask(signals_full, positions, val, mode, random_state=42)
    sig_missing_train = signals_missing_full[:n_split]
    sig_missing_test = signals_missing_full[n_split:]
    
    methods = ["spherical_spline", "rbfi_tps"]
    results = []
    
    for m in methods:
        sampler = optuna.samplers.NSGAIISampler(seed=42)
        study = optuna.create_study(directions=["minimize", "minimize"], sampler=sampler)
        
        study.optimize(lambda t: objective(t, m, sig_clean_train, sig_clean_test, sig_missing_train, sig_missing_test, positions, sfreq),
                       n_trials=10, n_jobs=1, show_progress_bar=False)
        
        try:
            best_t = get_best_pareto_trial(study)
            # Fetch the TEST metrics stored in the best trial
            final_metrics = {
                "mae": best_t.user_attrs["test_mae"],
                "lsd": best_t.user_attrs["test_lsd"],
                "snr": best_t.user_attrs["test_snr"],
                "rmse": best_t.user_attrs["test_rmse"],
                "dtw": best_t.user_attrs["test_dtw"],
                "coherence_mean": best_t.user_attrs["test_coherence_mean"]
            }
            p = best_t.params
        except (ValueError, KeyError):
            p = {}
            final_metrics = {"mae": np.nan, "lsd": np.nan, "snr": np.nan, "rmse": np.nan, "dtw": np.nan, "coherence_mean": np.nan}
            
        results.append({
            "dataset": ds_name,
            "missing_mode": mode,
            "missing_type": stype,
            "missing_val": val,
            "method": m,
            "params": str(p),
            **final_metrics
        })
        
    return results

def main():
    datasets = {
        "mne_sample": load_mne_sample_dataset,
        "physionet": load_physionet_eegmmidb,
        "bci_iv": load_bci_competition_iv_2a
    }
    
    scenarios = []
    for mode in ["random", "nearby"]:
        for r in [0.1, 0.2, 0.3, 0.4]:
            scenarios.append((mode, "ratio", r))
        for c in [1.0, 2.0, 3.0]:
            scenarios.append((mode, "count", c))
            
    all_res = []
    for ds_name, loader in datasets.items():
        print(f"Loading {ds_name}...")
        data = loader()
        for (mode, stype, val) in scenarios:
            res = optimize_case(ds_name, data, mode, stype, val)
            all_res.extend(res)
            
    df = pd.DataFrame(all_res)
    df.to_csv(CSV_PATH, index=False)
    print(f"\nResultados Baselines Optimizados guardados en {CSV_PATH.name}")

if __name__ == "__main__":
    main()
