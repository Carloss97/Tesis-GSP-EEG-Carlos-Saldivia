"""
plot_psd_extreme.py
===================
Plots the PSD comparison for the worst-case extreme scenario (e.g. nearby 40%).
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

from src.data.data_loader import load_mne_sample_dataset
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
    
    # EXTREME CASE: mne_sample, nearby, ratio 0.4
    ds_name = "mne_sample"
    mode = "nearby"
    scen_val = 0.4
    scen_type = "ratio"
    
    df_case = df[(df["dataset"] == ds_name) & (df["missing_mode"] == mode) & (df["missing_val"] == scen_val) & (df["missing_type"] == scen_type)]
    
    if df_case.empty:
        print("[ERROR] No se encontró el caso extremo en CSV.")
        return
        
    print(f"Generando PSD Extremo para {ds_name} | {mode} | ratio={scen_val}...")
    
    data = load_mne_sample_dataset()
    data["signals"] = data["signals"][:1000]
    signals_clean = data["signals"]
    positions = data["positions"]
    sfreq = data["info"].get("sfreq", 250.0)
    
    # Simulate mask exactly as in the optuna script
    signals_missing = simulate_mask(signals_clean, positions, scen_val, mode, random_state=42)
    
    # 1. Extract TRSS Params
    row_trss = df_case[df_case["method"] == "trss"].iloc[0]
    p_trss = ast.literal_eval(row_trss["params"])
    
    # Interpolate TRSS
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        g = build_graph("knng", positions, signals=signals_clean, k=p_trss["k"], sigma=p_trss["sigma"])
        adj = g["adjacency"].toarray() if hasattr(g["adjacency"], "toarray") else np.asarray(g["adjacency"])
        res_trss = interpolate_signals("trss", signals_missing, adjacency=adj, 
                                     alpha=p_trss["alpha"], beta=p_trss["beta"], lr=0.05, n_iter=80)
    sig_trss = res_trss["reconstructed"]
    
    # Interpolate ICA
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res_ica = interpolate_signals("ica", signals_missing)
    sig_ica = res_ica["reconstructed"]
    
    # Interpolate Spherical Spline
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res_ss = interpolate_signals("spherical_spline", signals_missing, positions=positions)
    sig_ss = res_ss["reconstructed"]

    N, D = signals_clean.shape
    def get_avg_psd(sigs):
        psds = []
        freqs = None
        for d in range(D):
            mask = ~np.isnan(sigs[:, d])
            if np.sum(mask) < 64: continue
            f, pxx = welch(sigs[mask, d], fs=sfreq, nperseg=256)
            freqs = f
            psds.append(pxx)
        if not psds: return None, None
        return freqs, np.mean(psds, axis=0)

    f_c, p_c = get_avg_psd(signals_clean)
    f_trss, p_trss_v = get_avg_psd(sig_trss)
    f_ica, p_ica = get_avg_psd(sig_ica)
    f_ss, p_ss = get_avg_psd(sig_ss)
    
    plt.figure(figsize=(12, 7))
    if f_c is not None:
        plt.semilogy(f_c, p_c, label='Ground Truth', color='black', linewidth=3)
    if f_ss is not None:
        plt.semilogy(f_ss, p_ss, label='Spherical Spline', color='magenta', linestyle='--', alpha=0.8, linewidth=2)
    if f_ica is not None:
        plt.semilogy(f_ica, p_ica, label='ICA', color='orange', linestyle=':', alpha=0.8, linewidth=2)
    if f_trss is not None:
        plt.semilogy(f_trss, p_trss_v, label='TRSS (GSP)', color='blue', linestyle='-.', alpha=1.0, linewidth=2.5)
        
    plt.title(f'Comparación Extrema PSD - {ds_name.upper()} | {mode.capitalize()} | Pérdida {int(scen_val*100)}%', fontsize=15, fontweight='bold')
    plt.xlabel('Frecuencia (Hz)', fontsize=12)
    plt.ylabel('Densidad Espectral de Potencia (V^2/Hz)', fontsize=12)
    plt.xlim(0.5, 45.0)
    
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend(fontsize=12, loc='upper right')
    
    out_path = ROOT / "results_optuna_final" / "extreme_psd_multimethod.png"
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"PSD Extremo guardado en {out_path}")

if __name__ == "__main__":
    main()
