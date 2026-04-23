"""
plot_psd_best.py
================
Plots the PSD comparison for the best overall Optuna configuration.
"""

import os
import sys
import warnings
from pathlib import Path
import ast

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import welch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_physionet_eegmmidb, load_bci_competition_iv_2a, load_mne_sample_dataset
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from experiments.run_optuna_optimization import simulate_mask

os.environ["BCI_IV_2A_PATH"] = str(ROOT / "datasets" / "BCICIV_2a_gdf")
os.environ["EEGBCI_LOCAL_PATH"] = str(ROOT / "datasets" / "MNE-eegbci-data")

def main():
    csv_path = ROOT / "results_optuna_final" / "optuna_best_results.csv"
    if not csv_path.exists():
        print("[ERROR] No se encontró optuna_best_results.csv")
        return
        
    df = pd.read_csv(csv_path)
    # Filter only TRSS
    df_trss = df[df["family"] == "trss"]
    if df_trss.empty:
        print("[ERROR] No hay resultados TRSS.")
        return
        
    # Get the best overall based on lowest MAE
    best_row = df_trss.loc[df_trss["mae"].idxmin()]
    
    ds_name = best_row["dataset"]
    mode = best_row["missing_mode"]
    scen_val = best_row["missing_val"]
    
    print(f"Mejor configuración TRSS encontrada en: {ds_name} | {mode} | val={scen_val}")
    
    # Reload dataset
    if ds_name == "physionet":
        data = load_physionet_eegmmidb(subject=1, run=4)
        data["signals"] = data["signals"][:1000]
    elif ds_name == "bci_iv":
        data = load_bci_competition_iv_2a(subject=1)
        data["signals"] = data["signals"][:1000]
    else:
        data = load_mne_sample_dataset()
        data["signals"] = data["signals"][:1000]
        
    signals_clean = data["signals"]
    positions = data["positions"]
    sfreq = data["info"].get("sfreq", 250.0)
    
    # Simulate mask
    signals_missing = simulate_mask(signals_clean, positions, scen_val, mode, random_state=42)
    
    # Parse params
    params = ast.literal_eval(best_row["params"])
    k = params["k"]
    sigma = params["sigma"]
    alpha = params["alpha"]
    beta = params["beta"]
    
    # Interpolate
    print("Interpolando con los mejores parámetros...")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        graph = build_graph("knng", positions, signals=signals_clean, k=k, sigma=sigma)
        adjacency = graph["adjacency"].toarray() if hasattr(graph["adjacency"], "toarray") else np.asarray(graph["adjacency"])
        result = interpolate_signals("trss", signals_missing, adjacency=adjacency, 
                                     alpha=alpha, beta=beta, lr=0.05, n_iter=80)
                                     
    signals_reconstructed = result["reconstructed"]
    
    # Let's compute average PSD across all channels
    N, D = signals_clean.shape
    def get_avg_psd(sigs):
        psds = []
        freqs = None
        for d in range(D):
            mask = ~np.isnan(sigs[:, d])
            if np.sum(mask) < 64: continue
            f, pxx = welch(sigs[mask, d], fs=sfreq, nperseg=128)
            freqs = f
            psds.append(pxx)
        if not psds: return None, None
        return freqs, np.mean(psds, axis=0)

    print("Calculando PSD...")
    f_c, p_c = get_avg_psd(signals_clean)
    f_m, p_m = get_avg_psd(signals_missing)
    f_r, p_r = get_avg_psd(signals_reconstructed)
    
    plt.figure(figsize=(10, 6))
    if f_c is not None:
        plt.semilogy(f_c, p_c, label='Ground Truth', color='black', linewidth=2)
    if f_m is not None:
        plt.semilogy(f_m, p_m, label='Missing (Canales Restantes)', color='red', linestyle='--', alpha=0.7)
    if f_r is not None:
        plt.semilogy(f_r, p_r, label='Reconstruido (TRSS)', color='blue', linestyle='-.', alpha=0.9)
        
    plt.title(f'PSD Promedio - Dataset: {ds_name} | Modo: {mode} | Faltantes: {scen_val}\nTRSS alpha={alpha:.2f}, beta={beta:.2f}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Densidad Espectral de Potencia (V^2/Hz)')
    plt.xlim(0.5, 45.0)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    
    out_path = ROOT / "results_optuna_final" / "best_psd_comparison.png"
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"PSD guardado en {out_path}")

if __name__ == "__main__":
    main()
