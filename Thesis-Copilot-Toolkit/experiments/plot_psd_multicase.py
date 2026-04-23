"""
plot_psd_multicase.py
=====================
Plots PSD comparisons for multiple cases (e.g. extreme and low loss) to show degradation.
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
    
    # We will test MNE Sample under nearby and random with 0.1 (low loss) and 0.4 (extreme loss)
    ds_name = "mne_sample"
    scenarios_to_plot = [
        {"mode": "nearby", "val": 0.4, "type": "ratio"},
        {"mode": "nearby", "val": 0.1, "type": "ratio"},
        {"mode": "random", "val": 0.4, "type": "ratio"},
        {"mode": "random", "val": 0.1, "type": "ratio"}
    ]
    
    data = load_mne_sample_dataset()
    data["signals"] = data["signals"][:1000]
    signals_clean = data["signals"]
    positions = data["positions"]
    sfreq = data["info"].get("sfreq", 250.0)
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

    for scen in scenarios_to_plot:
        mode = scen["mode"]
        scen_val = scen["val"]
        scen_type = scen["type"]
        
        df_case = df[(df["dataset"] == ds_name) & (df["missing_mode"] == mode) & (df["missing_val"] == scen_val) & (df["missing_type"] == scen_type)]
        if df_case.empty: continue
            
        print(f"Generando PSD para {ds_name} | {mode} | ratio={scen_val}...")
        
        signals_missing = simulate_mask(signals_clean, positions, scen_val, mode, random_state=42)
        
        # 1. Extract TRSS
        row_trss = df_case[df_case["method"] == "trss"].iloc[0]
        p_trss = ast.literal_eval(row_trss["params"])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            g = build_graph("knng", positions, signals=signals_clean, k=p_trss["k"], sigma=p_trss["sigma"])
            adj = g["adjacency"].toarray() if hasattr(g["adjacency"], "toarray") else np.asarray(g["adjacency"])
            res_trss = interpolate_signals("trss", signals_missing, adjacency=adj, 
                                         alpha=p_trss["alpha"], beta=p_trss["beta"], lr=0.05, n_iter=80)
        sig_trss = res_trss["reconstructed"]
        
        # 2. Extract Tikhonov
        row_tik = df_case[df_case["method"] == "tikhonov"].iloc[0]
        p_tik = ast.literal_eval(row_tik["params"])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            g = build_graph("knng", positions, signals=signals_clean, k=p_tik["k"], sigma=p_tik["sigma"])
            adj = g["adjacency"].toarray() if hasattr(g["adjacency"], "toarray") else np.asarray(g["adjacency"])
            res_tik = interpolate_signals("tikhonov", signals_missing, adjacency=adj, alpha=p_tik["alpha"])
        sig_tik = res_tik["reconstructed"]
        
        # 3. ICA & Spline
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res_ica = interpolate_signals("ica", signals_missing)
            res_ss = interpolate_signals("spherical_spline", signals_missing, positions=positions)
            
        sig_ica = res_ica["reconstructed"]
        sig_ss = res_ss["reconstructed"]

        f_trss, p_trss_v = get_avg_psd(sig_trss)
        f_tik, p_tik_v = get_avg_psd(sig_tik)
        f_ica, p_ica_v = get_avg_psd(sig_ica)
        f_ss, p_ss_v = get_avg_psd(sig_ss)
        
        plt.figure(figsize=(12, 7))
        if f_c is not None:
            plt.semilogy(f_c, p_c, label='Ground Truth', color='black', linewidth=3)
        if f_ss is not None:
            plt.semilogy(f_ss, p_ss_v, label='Spherical Spline', color='magenta', linestyle='--', alpha=0.8, linewidth=2)
        if f_ica is not None:
            plt.semilogy(f_ica, p_ica_v, label='ICA', color='orange', linestyle=':', alpha=0.8, linewidth=2)
        if f_tik is not None:
            plt.semilogy(f_tik, p_tik_v, label='Tikhonov', color='cyan', linestyle='-', alpha=0.7, linewidth=2)
        if f_trss is not None:
            plt.semilogy(f_trss, p_trss_v, label='TRSS (GSP)', color='blue', linestyle='-.', alpha=1.0, linewidth=2.5)
            
        plt.title(f'PSD Comparison - {ds_name.upper()} | {mode.capitalize()} | Pérdida {int(scen_val*100)}%', fontsize=15, fontweight='bold')
        plt.xlabel('Frecuencia (Hz)', fontsize=12)
        plt.ylabel('Densidad Espectral de Potencia (V^2/Hz)', fontsize=12)
        plt.xlim(0.5, 45.0)
        
        plt.grid(True, which="both", ls="-", alpha=0.2)
        plt.legend(fontsize=12, loc='upper right')
        
        out_path = ROOT / "results_optuna_final" / f"psd_comparison_{ds_name}_{mode}_{scen_val}.png"
        plt.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"PSD Multicase guardado en {out_path.name}")

if __name__ == "__main__":
    main()
