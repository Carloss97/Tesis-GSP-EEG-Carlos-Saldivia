"""
run_optuna_optimization.py
==========================
Optimización avanzada de métodos de interpolación GSP usando Optuna.
- Optimiza hiperparámetros continuamente (k, sigma, alpha, beta).
- Reporta granularmente todas las métricas (MAE, RMSE, SNR, DTW, LSD, Coherencia).
- Almacena en results_optuna_final.
"""

import os
import sys
import warnings
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
import optuna

# Suprimir salida excesiva de Optuna
optuna.logging.set_verbosity(optuna.logging.WARNING)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_physionet_eegmmidb, load_bci_competition_iv_2a, simulate_missing_channels, load_mne_sample_dataset
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals

RESULTS_DIR = ROOT / "results_optuna_final"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

os.environ["BCI_IV_2A_PATH"] = str(ROOT / "datasets" / "BCICIV_2a_gdf")
os.environ["EEGBCI_LOCAL_PATH"] = str(ROOT / "datasets" / "MNE-eegbci-data")

# ---------------------------------------------------------------------------
# Datasets
# ---------------------------------------------------------------------------
def get_physionet():
    data = load_physionet_eegmmidb(subject=1, run=4)
    data["signals"] = data["signals"][:1000]
    data["info"]["name"] = "physionet"
    return data

def get_bci_iv():
    data = load_bci_competition_iv_2a(subject=1)
    data["signals"] = data["signals"][:1000]
    data["info"]["name"] = "bci_iv"
    return data

def get_mne_sample():
    data = load_mne_sample_dataset()
    data["signals"] = data["signals"][:1000]
    data["info"]["name"] = "mne_sample"
    return data

DATASETS: Dict[str, Any] = {
    "physionet": get_physionet,
    "mne_sample": get_mne_sample,
}
# Opcional: bci_iv falla a veces por MNE GDF overflow, así que lo manejamos con try-except

# ---------------------------------------------------------------------------
# Missing Channels
# ---------------------------------------------------------------------------
def simulate_mask(signals: np.ndarray, positions: np.ndarray, missing_val: float, mode: str, random_state: int) -> np.ndarray:
    N, D = signals.shape
    if isinstance(missing_val, float) and missing_val < 1.0:
        n_missing = max(1, int(round(D * missing_val)))
    else:
        n_missing = int(missing_val)
    if n_missing >= D: 
        n_missing = D - 1
        
    if mode == "random":
        return simulate_missing_channels(signals, missing_ratio=n_missing, random_state=random_state)
    elif mode == "nearby":
        rng = np.random.default_rng(random_state)
        signals_masked = signals.copy()
        dists = cdist(positions, positions)
        for i in range(N):
            center_idx = rng.choice(D)
            nearest = np.argsort(dists[center_idx])[:n_missing]
            signals_masked[i, nearest] = np.nan
        return signals_masked
    else:
        raise ValueError(f"Unknown mode: {mode}")

# ---------------------------------------------------------------------------
# Optuna Objectives
# ---------------------------------------------------------------------------
def objective_tikhonov(trial: optuna.Trial, signals_clean, positions, signals_missing, sfreq):
    k = trial.suggest_int("k", 3, 10)
    sigma = trial.suggest_float("sigma", 0.1, 3.0, log=True)
    alpha = trial.suggest_float("alpha", 0.001, 10.0, log=True)
    
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            graph = build_graph("knng", positions, signals=signals_clean, k=k, sigma=sigma)
            adjacency = graph["adjacency"].toarray() if hasattr(graph["adjacency"], "toarray") else np.asarray(graph["adjacency"])
            result = interpolate_signals("tikhonov", signals_missing, adjacency=adjacency, alpha=alpha)
            
        metrics = evaluate_signals(signals_clean, result["reconstructed"], 
                                   metrics=["mae", "rmse", "snr", "dtw", "lsd", "coherence_mean"], sfreq=sfreq)
        
        for m, v in metrics.items():
            trial.set_user_attr(m, v)
        
        # Objetivo multi-criterio: minimizar MAE y LSD
        mae = metrics.get("mae", float('inf'))
        lsd = metrics.get("lsd", float('inf'))
        if np.isnan(mae): mae = float('inf')
        if np.isnan(lsd): lsd = float('inf')
        return mae, lsd
    except Exception:
        raise optuna.TrialPruned()

def objective_trss(trial: optuna.Trial, signals_clean, positions, signals_missing, sfreq):
    k = trial.suggest_int("k", 3, 10)
    sigma = trial.suggest_float("sigma", 0.1, 3.0, log=True)
    alpha = trial.suggest_float("alpha", 0.01, 5.0, log=True)
    beta = trial.suggest_float("beta", 0.01, 1.0, log=True)
    
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            graph = build_graph("knng", positions, signals=signals_clean, k=k, sigma=sigma)
            adjacency = graph["adjacency"].toarray() if hasattr(graph["adjacency"], "toarray") else np.asarray(graph["adjacency"])
            result = interpolate_signals("trss", signals_missing, adjacency=adjacency, 
                                         alpha=alpha, beta=beta, lr=0.05, n_iter=80)
            
        metrics = evaluate_signals(signals_clean, result["reconstructed"], 
                                   metrics=["mae", "rmse", "snr", "dtw", "lsd", "coherence_mean"], sfreq=sfreq)
        
        for m, v in metrics.items():
            trial.set_user_attr(m, v)
            
        # Objetivo multi-criterio: minimizar MAE y LSD
        mae = metrics.get("mae", float('inf'))
        lsd = metrics.get("lsd", float('inf'))
        if np.isnan(mae): mae = float('inf')
        if np.isnan(lsd): lsd = float('inf')
        return mae, lsd
    except Exception:
        raise optuna.TrialPruned()

# ---------------------------------------------------------------------------
# Main Routine
# ---------------------------------------------------------------------------
def run_optuna_benchmark() -> pd.DataFrame:
    rows = []
    
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
    BASELINES = ["spherical_spline", "rbfi_tps", "ica"]
    N_TRIALS = 30
    
    def get_best_pareto_trial(study):
        best_trials = study.best_trials
        if not best_trials: return None
        maes = np.array([t.values[0] for t in best_trials])
        lsds = np.array([t.values[1] for t in best_trials])
        if np.max(maes) == np.min(maes):
            return best_trials[0]
        maes_n = (maes - np.min(maes)) / (np.max(maes) - np.min(maes) + 1e-12)
        lsds_n = (lsds - np.min(lsds)) / (np.max(lsds) - np.min(lsds) + 1e-12)
        dists = maes_n**2 + lsds_n**2
        return best_trials[np.argmin(dists)]

    for ds_name, ds_fn in DATASETS.items():
        try:
            ds = ds_fn()
        except Exception as e:
            print(f"[WARN] No se cargó {ds_name}: {e}")
            continue
            
        signals_clean = ds["signals"]
        positions = ds["positions"]
        sfreq = ds["info"].get("sfreq", 250.0)

        for mode in MODES:
            for scen in SCENARIOS:
                val = scen["val"]
                scen_type = scen["type"]
                print(f"\n>> {ds_name} | {mode} | {scen_type}={val}")
                
                signals_missing = simulate_mask(signals_clean, positions, val, mode, random_state=42)

                # 1. BASELINES
                for method in BASELINES:
                    try:
                        with warnings.catch_warnings():
                            warnings.simplefilter("ignore")
                            kwargs = {}
                            if method in ["spherical_spline", "rbfi_tps"]:
                                kwargs["positions"] = positions
                            result = interpolate_signals(method, signals_missing, **kwargs)
                        
                        metrics = evaluate_signals(signals_clean, result["reconstructed"], 
                                                   metrics=["mae", "rmse", "snr", "dtw", "lsd", "coherence_mean"], sfreq=sfreq)
                        if metrics:
                            rows.append({
                                "dataset": ds_name,
                                "missing_mode": mode,
                                "missing_type": scen_type,
                                "missing_val": val,
                                "method": method,
                                "family": "baseline",
                                "params": "default",
                                **metrics
                            })
                    except Exception as e:
                        pass

                # 2. OPTUNA TIKHONOV
                study_tik = optuna.create_study(directions=["minimize", "minimize"])
                study_tik.optimize(lambda t: objective_tikhonov(t, signals_clean, positions, signals_missing, sfreq), 
                                   n_trials=N_TRIALS)
                bt_tik = get_best_pareto_trial(study_tik)
                if bt_tik is not None:
                    rows.append({
                        "dataset": ds_name,
                        "missing_mode": mode,
                        "missing_type": scen_type,
                        "missing_val": val,
                        "method": "tikhonov",
                        "family": "tikhonov",
                        "params": str(bt_tik.params),
                        "mae": bt_tik.user_attrs.get("mae", np.nan),
                        "rmse": bt_tik.user_attrs.get("rmse", np.nan),
                        "snr": bt_tik.user_attrs.get("snr", np.nan),
                        "dtw": bt_tik.user_attrs.get("dtw", np.nan),
                        "lsd": bt_tik.user_attrs.get("lsd", np.nan),
                        "coherence_mean": bt_tik.user_attrs.get("coherence_mean", np.nan),
                    })

                # 3. OPTUNA TRSS
                study_trss = optuna.create_study(directions=["minimize", "minimize"])
                study_trss.optimize(lambda t: objective_trss(t, signals_clean, positions, signals_missing, sfreq), 
                                    n_trials=N_TRIALS)
                bt_trss = get_best_pareto_trial(study_trss)
                if bt_trss is not None:
                    rows.append({
                        "dataset": ds_name,
                        "missing_mode": mode,
                        "missing_type": scen_type,
                        "missing_val": val,
                        "method": "trss",
                        "family": "trss",
                        "params": str(bt_trss.params),
                        "mae": bt_trss.user_attrs.get("mae", np.nan),
                        "rmse": bt_trss.user_attrs.get("rmse", np.nan),
                        "snr": bt_trss.user_attrs.get("snr", np.nan),
                        "dtw": bt_trss.user_attrs.get("dtw", np.nan),
                        "lsd": bt_trss.user_attrs.get("lsd", np.nan),
                        "coherence_mean": bt_trss.user_attrs.get("coherence_mean", np.nan),
                    })
                    
    df = pd.DataFrame(rows)
    return df

def main():
    print("Iniciando Optimización con Optuna...")
    df = run_optuna_benchmark()
    
    if df.empty:
        print("No se generaron resultados.")
        return
        
    out_csv = RESULTS_DIR / "optuna_best_results.csv"
    
    # Ordenar por el MAE (el que optimizamos)
    df = df.sort_values(["dataset", "missing_mode", "missing_type", "missing_val", "mae"])
    df.to_csv(out_csv, index=False)
    print(f"\nResultados óptimos exportados a: {out_csv}")

if __name__ == "__main__":
    main()
