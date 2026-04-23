"""
run_final_grid_search.py
========================
Iteración final exhaustiva: 
- Datasets reales (PhysioNet y BCI Competition IV 2a).
- Optimización de creación de grafo (K-NN Gaussiano: k y sigma).
- Modos de enmascaramiento: random vs nearby (cercanos).
- Escenarios de faltantes: Ratios (10%, 20%, 30%, 40%) y Counts (1, 2, 3 canales).
- Métodos: Tikhonov y TRSS vs Baselines.
"""

from __future__ import annotations

import os
import sys
import warnings
from pathlib import Path
from typing import Any, Dict, List

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_physionet_eegmmidb, load_bci_competition_iv_2a, simulate_missing_channels, load_mne_sample_dataset
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals

RESULTS_DIR = ROOT / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

os.environ["BCI_IV_2A_PATH"] = str(ROOT / "datasets" / "BCICIV_2a_gdf")
os.environ["EEGBCI_LOCAL_PATH"] = str(ROOT / "datasets" / "MNE-eegbci-data")

# ---------------------------------------------------------------------------
# Dataset Loading
# ---------------------------------------------------------------------------
def get_physionet():
    data = load_physionet_eegmmidb(subject=1, run=4)
    data["signals"] = data["signals"][:300]  # Subsample for feasibility
    data["info"]["name"] = "physionet_s1_r4"
    return data

def get_bci_iv():
    data = load_bci_competition_iv_2a(subject=1)
    data["signals"] = data["signals"][:300]  # Subsample for feasibility
    data["info"]["name"] = "bci_iv_2a_s1"
    return data

def get_mne_sample():
    data = load_mne_sample_dataset()
    data["signals"] = data["signals"][:300]  # Subsample for feasibility
    data["info"]["name"] = "mne_sample"
    return data

DATASETS: Dict[str, Any] = {
    "physionet_s1_r4": get_physionet,
    "bci_iv_2a_s1": get_bci_iv,
    "mne_sample": get_mne_sample,
}

# ---------------------------------------------------------------------------
# Missing Channel Simulation
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
# Grids
# ---------------------------------------------------------------------------
GRID_GRAPH = [{"k": k, "sigma": s} for k in [3, 5] for s in [1.0, 2.0]]

BASELINES = [
    ("spherical_spline", {}),
    ("rbfi_tps", {}),
    ("ica", {}),
]

GRID_TIKHONOV = [{"alpha": a} for a in [0.01, 0.1, 1.0]]
GRID_TRSS = [{"alpha": a, "beta": b, "n_iter": 120, "lr": 0.05} 
             for a in [0.1, 1.0] for b in [0.1, 0.5]]

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

def _method_label(method: str, params: Dict) -> str:
    if not params: return method
    parts = []
    for k in sorted(params):
        v = params[k]
        if isinstance(v, float):
            parts.append(f"{k}{v:.2g}".replace(".", "_"))
        else:
            parts.append(f"{k}{v}")
    return f"{method}__" + "_".join(parts)

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
def run_benchmark() -> pd.DataFrame:
    rows: List[Dict] = []
    
    gsp_methods = [("tikhonov", p) for p in GRID_TIKHONOV] + [("trss", p) for p in GRID_TRSS]
    
    total_iterations = 0
    print("[Grid Search] Inicializando...")

    for ds_name, ds_fn in DATASETS.items():
        try:
            ds = ds_fn()
        except Exception as e:
            print(f"[WARN] Error cargando {ds_name}: {e}")
            continue
            
        signals_clean: np.ndarray = ds["signals"]
        positions: np.ndarray = ds["positions"]

        sfreq = ds["info"].get("sfreq", 250.0)

        for mode in MODES:
            for scen in SCENARIOS:
                val = scen["val"]
                scen_type = scen["type"]
                signals_missing = simulate_mask(signals_clean, positions, val, mode, random_state=42)

                # 1. Run Baselines (do not depend on Graph)
                for method, extra in BASELINES:
                    label = _method_label(method, extra)
                    try:
                        with warnings.catch_warnings():
                            warnings.simplefilter("ignore")
                            kwargs = {}
                            if method in ["spherical_spline", "rbfi_tps"]:
                                kwargs["positions"] = positions
                            kwargs.update(extra)
                            result = interpolate_signals(method, signals_missing, **kwargs)
                        metrics_list = ["mae", "rmse", "snr", "dtw", "lsd", "coherence_mean"]
                        metrics = evaluate_signals(signals_clean, result["reconstructed"], metrics=metrics_list, sfreq=sfreq)
                        if metrics:
                            rows.append({
                                "dataset": ds_name,
                                "missing_mode": mode,
                                "missing_type": scen_type,
                                "missing_val": val,
                                "interp_label": label,
                                "method": method,
                                "family": "baseline",
                                "graph_k": np.nan,
                                "graph_sigma": np.nan,
                                "mae": metrics.get("mae", np.nan),
                                "rmse": metrics.get("rmse", np.nan),
                                "snr": metrics.get("snr", np.nan),
                                "dtw": metrics.get("dtw", np.nan),
                                "lsd": metrics.get("lsd", np.nan),
                                "coherence_mean": metrics.get("coherence_mean", np.nan),
                                **extra
                            })
                    except Exception:
                        pass
                
                # 2. Run GSP Methods with Graph Grid
                for g_params in GRID_GRAPH:
                    try:
                        with warnings.catch_warnings():
                            warnings.simplefilter("ignore")
                            graph = build_graph("knng", positions, signals=signals_clean, **g_params)
                            adjacency = graph["adjacency"].toarray() if hasattr(graph["adjacency"], "toarray") else np.asarray(graph["adjacency"])
                    except Exception:
                        continue
                        
                    for method, extra in gsp_methods:
                        label = _method_label(method, extra)
                        total_iterations += 1
                        if total_iterations % 50 == 0:
                            print(f"  [{total_iterations}] {ds_name} / {mode} / {scen_type}={val} / Graph {g_params} / {label}", flush=True)
                        
                        try:
                            with warnings.catch_warnings():
                                warnings.simplefilter("ignore")
                                kwargs = {"adjacency": adjacency, **extra}
                                result = interpolate_signals(method, signals_missing, **kwargs)
                            metrics_list = ["mae", "rmse", "snr", "dtw", "lsd", "coherence_mean"]
                            metrics = evaluate_signals(signals_clean, result["reconstructed"], metrics=metrics_list, sfreq=sfreq)
                            if metrics:
                                family = "tikhonov" if method == "tikhonov" else "trss"
                                rows.append({
                                    "dataset": ds_name,
                                    "missing_mode": mode,
                                    "missing_type": scen_type,
                                    "missing_val": val,
                                    "interp_label": label,
                                    "method": method,
                                    "family": family,
                                    "graph_k": g_params["k"],
                                    "graph_sigma": g_params["sigma"],
                                    "mae": metrics.get("mae", np.nan),
                                    "rmse": metrics.get("rmse", np.nan),
                                    "snr": metrics.get("snr", np.nan),
                                    "dtw": metrics.get("dtw", np.nan),
                                    "lsd": metrics.get("lsd", np.nan),
                                    "coherence_mean": metrics.get("coherence_mean", np.nan),
                                    **extra
                                })
                        except Exception:
                            pass

    print(f"[Grid Search] Completado. Filas: {len(rows)}")
    return pd.DataFrame(rows)

def _savefig(fig: plt.Figure, name: str) -> None:
    path = RESULTS_DIR / name
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  [fig] {path.name}")

def main() -> None:
    print("=" * 60)
    print("  Grid Search Final Exhaustivo — EEG-GSP (Real Datasets)")
    print("=" * 60)

    df = run_benchmark()
    if df.empty:
        print("[ERROR] No se generaron resultados.")
        return

    # Save full results
    raw_path = RESULTS_DIR / "final_grid_search_raw.csv"
    df.to_csv(raw_path, index=False)
    print(f"  [csv] {raw_path.name}")

    # Aggregated ranking per method and missing mode
    # For GSP methods, we first want to find the best configuration per scenario or overall.
    # To keep it simple, we rank by the overall average across all graph parameters as a general measure,
    # or we can pick the absolute best hyperparameter combo.
    
    ranking = df.groupby(["interp_label", "family", "method", "missing_mode", "missing_type"]).agg(
        mae_mean=("mae", "mean"),
        mae_std=("mae", "std"),
        rmse_mean=("rmse", "mean"),
        snr_mean=("snr", "mean"),
        dtw_mean=("dtw", "mean"),
        lsd_mean=("lsd", "mean"),
        coherence_mean=("coherence_mean", "mean")
    ).reset_index().sort_values(["missing_mode", "missing_type", "mae_mean"])
    
    rank_path = RESULTS_DIR / "final_grid_search_ranking.csv"
    ranking.to_csv(rank_path, index=False)
    print(f"  [csv] {rank_path.name}")

    # Plot comparisons: Overall Best GSP vs Baseline by Mode
    for mode in MODES:
        sub_df = df[df["missing_mode"] == mode]
        if sub_df.empty: continue
        
        # Find best method configurations
        best_labels = []
        for fam in ["tikhonov", "trss"]:
            fam_df = sub_df[sub_df["family"] == fam]
            if not fam_df.empty:
                # Group by method label AND graph params to find the absolute best combination
                group_mae = fam_df.groupby(["interp_label", "graph_k", "graph_sigma"])["mae"].mean()
                if not group_mae.empty:
                    best_combo = group_mae.idxmin()
                    best_labels.append(best_combo[0]) # just the interp_label
                    print(f"Mejor {fam} ({mode}): {best_combo[0]} con Grafo k={best_combo[1]}, sigma={best_combo[2]} (MAE={group_mae[best_combo]:.4e})")

        baseline_labels = [m for m, _ in BASELINES]
        selected_labels = best_labels + baseline_labels
        
        plot_df = sub_df[sub_df["interp_label"].isin(selected_labels)]
        agg = plot_df.groupby(["interp_label", "family"])["mae"].mean().reset_index().sort_values("mae")
        
        colors = ["#DD8452" if f in ["tikhonov", "trss"] else "#4C72B0" for f in agg["family"]]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(agg["interp_label"][::-1], agg["mae"][::-1], color=colors[::-1])
        ax.set_xlabel(f"MAE Medio ({mode.upper()})")
        ax.set_title(f"Mejor Configuración GSP vs Baselines - Modo: {mode.upper()}")
        ax.grid(axis="x", alpha=0.4)
        plt.tight_layout()
        _savefig(fig, f"final_grid_search_mae_bar_{mode}.png")

    print("\n[done] Resultados en:", RESULTS_DIR)

if __name__ == "__main__":
    main()
