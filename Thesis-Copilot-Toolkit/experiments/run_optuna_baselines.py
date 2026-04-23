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

def objective(trial, method, signals_clean, signals_missing, positions, sfreq):
    if method == "spherical_spline":
        eps = trial.suggest_float("eps", 1e-8, 1e-2, log=True)
        kwargs = {"positions": positions, "eps": eps}
        
    elif method == "rbfi_tps":
        smooth = trial.suggest_float("smooth", 0.0, 5.0)
        kwargs = {"positions": positions, "smooth": smooth}
        
    elif method == "ica":
        n_ch = signals_clean.shape[1]
        n_components = trial.suggest_int("n_components", 1, n_ch)
        kwargs = {"n_components": n_components, "random_state": 42}
        
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            res = interpolate_signals(method, signals_missing, **kwargs)
            sig_rec = res["reconstructed"]
            metrics = evaluate_signals(signals_clean, sig_rec, sfreq=sfreq)
            if np.isnan(metrics["mae"]) or np.isinf(metrics["mae"]):
                return float("inf"), float("inf")
            return metrics["mae"], metrics["lsd"]
        except Exception:
            return float("inf"), float("inf")

def optimize_case(ds_name, data, mode, stype, val):
    print(f"\n>> {ds_name} | {mode} | {stype}={val}")
    
    sfreq = data["info"].get("sfreq", 250.0)
    signals_clean = data["signals"][:500] # 500 muestras para agilizar
    positions = data["positions"]
    
    signals_missing = simulate_mask(signals_clean, positions, val, mode, random_state=42)
    
    methods = ["spherical_spline", "rbfi_tps"]
    results = []
    
    for m in methods:
        sampler = optuna.samplers.NSGAIISampler(seed=42)
        study = optuna.create_study(directions=["minimize", "minimize"], sampler=sampler)
        
        study.optimize(lambda t: objective(t, m, signals_clean, signals_missing, positions, sfreq),
                       n_trials=10, n_jobs=1, show_progress_bar=False)
        
        try:
            best_t = get_best_pareto_trial(study)
            p = best_t.params
        except ValueError:
            p = {}
            
        # Evaluar mejor modelo completo
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            kwargs = p.copy()
            if m in ["spherical_spline", "rbfi_tps"]:
                kwargs["positions"] = positions
            
            res = interpolate_signals(m, signals_missing, **kwargs)
            final_metrics = evaluate_signals(signals_clean, res["reconstructed"], sfreq=sfreq)
            
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
