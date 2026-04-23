import os
import sys
import warnings
from pathlib import Path
from typing import Any, Dict

import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
import optuna

optuna.logging.set_verbosity(optuna.logging.WARNING)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_bci_competition_iv_2a
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from experiments.run_optuna_optimization import objective_tikhonov, objective_trss, simulate_mask

RESULTS_DIR = ROOT / "results_optuna_final"
os.environ["BCI_IV_2A_PATH"] = str(ROOT / "datasets" / "BCICIV_2a_gdf")

def get_bci_iv():
    data = load_bci_competition_iv_2a(subject=1)
    data["signals"] = data["signals"][:1000]
    data["info"]["name"] = "bci_iv"
    return data

def run_bci_only():
    rows = []
    SCENARIOS = [
        {"val": 0.1, "type": "ratio"}, {"val": 0.2, "type": "ratio"},
        {"val": 0.3, "type": "ratio"}, {"val": 0.4, "type": "ratio"},
        {"val": 1.0, "type": "count"}, {"val": 2.0, "type": "count"}, {"val": 3.0, "type": "count"}
    ]
    MODES = ["random", "nearby"]
    BASELINES = ["spherical_spline", "rbfi_tps", "ica"]
    N_TRIALS = 30
    
    def get_best_pareto_trial(study):
        best_trials = study.best_trials
        if not best_trials: return None
        maes = np.array([t.values[0] for t in best_trials])
        lsds = np.array([t.values[1] for t in best_trials])
        if np.max(maes) == np.min(maes): return best_trials[0]
        maes_n = (maes - np.min(maes)) / (np.max(maes) - np.min(maes) + 1e-12)
        lsds_n = (lsds - np.min(lsds)) / (np.max(lsds) - np.min(lsds) + 1e-12)
        dists = maes_n**2 + lsds_n**2
        return best_trials[np.argmin(dists)]

    try:
        ds = get_bci_iv()
    except Exception as e:
        print(f"[ERROR] Failed to load bci_iv: {e}")
        return
        
    ds_name = "bci_iv"
    signals_clean = ds["signals"]
    positions = ds["positions"]
    sfreq = ds["info"].get("sfreq", 250.0)

    for mode in MODES:
        for scen in SCENARIOS:
            val = scen["val"]
            scen_type = scen["type"]
            print(f">> {ds_name} | {mode} | {scen_type}={val}")
            
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
                        rows.append({"dataset": ds_name, "missing_mode": mode, "missing_type": scen_type, 
                                     "missing_val": val, "method": method, "family": "baseline", "params": "default", **metrics})
                except Exception: pass

            # 2. TIKHONOV
            study_tik = optuna.create_study(directions=["minimize", "minimize"])
            study_tik.optimize(lambda t: objective_tikhonov(t, signals_clean, positions, signals_missing, sfreq), n_trials=N_TRIALS)
            bt_tik = get_best_pareto_trial(study_tik)
            if bt_tik:
                rows.append({"dataset": ds_name, "missing_mode": mode, "missing_type": scen_type, "missing_val": val,
                             "method": "tikhonov", "family": "tikhonov", "params": str(bt_tik.params),
                             "mae": bt_tik.user_attrs.get("mae", np.nan), "rmse": bt_tik.user_attrs.get("rmse", np.nan),
                             "snr": bt_tik.user_attrs.get("snr", np.nan), "dtw": bt_tik.user_attrs.get("dtw", np.nan),
                             "lsd": bt_tik.user_attrs.get("lsd", np.nan), "coherence_mean": bt_tik.user_attrs.get("coherence_mean", np.nan)})

            # 3. TRSS
            study_trss = optuna.create_study(directions=["minimize", "minimize"])
            study_trss.optimize(lambda t: objective_trss(t, signals_clean, positions, signals_missing, sfreq), n_trials=N_TRIALS)
            bt_trss = get_best_pareto_trial(study_trss)
            if bt_trss:
                rows.append({"dataset": ds_name, "missing_mode": mode, "missing_type": scen_type, "missing_val": val,
                             "method": "trss", "family": "trss", "params": str(bt_trss.params),
                             "mae": bt_trss.user_attrs.get("mae", np.nan), "rmse": bt_trss.user_attrs.get("rmse", np.nan),
                             "snr": bt_trss.user_attrs.get("snr", np.nan), "dtw": bt_trss.user_attrs.get("dtw", np.nan),
                             "lsd": bt_trss.user_attrs.get("lsd", np.nan), "coherence_mean": bt_trss.user_attrs.get("coherence_mean", np.nan)})
                
    df_new = pd.DataFrame(rows)
    csv_path = RESULTS_DIR / "optuna_best_results.csv"
    if csv_path.exists():
        df_old = pd.read_csv(csv_path)
        df_old = df_old[df_old["dataset"] != "bci_iv"]
        df_final = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df_final = df_new
        
    df_final = df_final.sort_values(["dataset", "missing_mode", "missing_type", "missing_val", "mae"])
    df_final.to_csv(csv_path, index=False)
    print("BCI dataset agregado y resultados consolidados en optuna_best_results.csv")

if __name__ == "__main__":
    run_bci_only()
