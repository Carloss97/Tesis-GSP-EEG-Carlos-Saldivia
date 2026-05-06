"""
plot_erp_time_series.py
=======================
Grafica la serie de tiempo (ERP / reconstrucción temporal) de un canal interpolado vs Ground Truth.
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
    
    ds_name = "mne_sample"
    scenarios_to_plot = [
        {"mode": "nearby", "val": 0.4, "type": "ratio"},
        {"mode": "nearby", "val": 0.1, "type": "ratio"},
        {"mode": "random", "val": 0.4, "type": "ratio"},
        {"mode": "random", "val": 0.1, "type": "ratio"},
    ]
    
    data = load_mne_sample_dataset()
    data["signals"] = data["signals"][:1000]
    signals_clean = data["signals"]
    positions = data["positions"]
    sfreq = data["info"].get("sfreq", 250.0)
    
    # Tomaremos un segmento de 1.5 segundos para visualizar
    N_SAMPLES = int(1.5 * sfreq)
    time_axis = np.arange(N_SAMPLES) / sfreq
    
    for scen in scenarios_to_plot:
        mode = scen["mode"]
        scen_val = scen["val"]
        scen_type = scen["type"]
        
        df_case = df[(df["dataset"] == ds_name) & (df["missing_mode"] == mode) & (df["missing_val"] == scen_val) & (df["missing_type"] == scen_type)]
        if df_case.empty: continue
            
        print(f"Generando ERP/Time Series para {ds_name} | {mode} | ratio={scen_val}...")
        
        # Simular máscara
        signals_missing = simulate_mask(signals_clean, positions, scen_val, mode, random_state=42)
        
        # Identificar un canal que haya sido eliminado (NaN) en la primera época/ventana
        # Elegimos el primer canal que es NaN
        nan_channels = np.where(np.isnan(signals_missing[0, :]))[0]
        if len(nan_channels) == 0:
            print("No se encontraron canales missing.")
            continue
        
        target_ch = nan_channels[0]
        print(f"Graficando canal perdido índice: {target_ch}")
        
        # 1. TRSS
        row_trss = df_case[df_case["method"] == "trss"].iloc[0]
        p_trss = ast.literal_eval(row_trss["params"])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            g = build_graph("knng", positions, signals=signals_clean, k=p_trss["k"], sigma=p_trss["sigma"])
            adj = g["adjacency"].toarray() if hasattr(g["adjacency"], "toarray") else np.asarray(g["adjacency"])
            res_trss = interpolate_signals("trss", signals_missing, adjacency=adj, 
                                         alpha=p_trss["alpha"], beta=p_trss["beta"], lr=0.05, n_iter=80)
        sig_trss = res_trss["reconstructed"]
        
        # 2. Tikhonov
        row_tik = df_case[df_case["method"] == "tikhonov"].iloc[0]
        p_tik = ast.literal_eval(row_tik["params"])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            g = build_graph("knng", positions, signals=signals_clean, k=p_tik["k"], sigma=p_tik["sigma"])
            adj = g["adjacency"].toarray() if hasattr(g["adjacency"], "toarray") else np.asarray(g["adjacency"])
            res_tik = interpolate_signals("tikhonov", signals_missing, adjacency=adj, alpha=p_tik["alpha"])
        sig_tik = res_tik["reconstructed"]
        
        # 3. ICA
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res_ica = interpolate_signals("ica", signals_missing)
        sig_ica = res_ica["reconstructed"]
        
        # 4. ICA (MNE)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res_ica_mne = interpolate_signals(
                "ica_mne",
                signals_missing,
                positions=positions,
                sfreq=sfreq,
                ica_method="picard",
            )
        sig_ica_mne = res_ica_mne["reconstructed"]

        # 5. MNE interpolate_bads
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res_mne = interpolate_signals(
                "mne_bads",
                signals_missing,
                positions=positions,
                sfreq=sfreq,
                interpolate_method="MNE",
            )
        sig_mne = res_mne["reconstructed"]

        # 6. Spherical Spline
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res_ss = interpolate_signals("spherical_spline", signals_missing, positions=positions)
        sig_ss = res_ss["reconstructed"]
        
        # Graficar en Subplots
        methods_data = [
            ("TRSS (GSP)", sig_trss, "blue"),
            ("Tikhonov", sig_tik, "cyan"),
            ("ICA (sklearn FastICA)", sig_ica, "orange"),
            ("ICA (MNE Picard)", sig_ica_mne, "green"),
            ("MNE interpolate_bads", sig_mne, "magenta"),
            ("Spherical Spline", sig_ss, "purple")
        ]
        
        fig, axes = plt.subplots(6, 1, figsize=(14, 14), sharex=True, sharey=True)
        fig.suptitle(f"Temporal Reconstruction (ERP) - Missing Channel #{target_ch}\n{ds_name.upper()} | {mode.capitalize()} | {int(scen_val*100)}% Loss", fontsize=16, fontweight="bold")
        
        gt_signal = signals_clean[:N_SAMPLES, target_ch]
        
        # Calcular limites basados en GT
        gt_min = gt_signal.min()
        gt_max = gt_signal.max()
        margin = (gt_max - gt_min) * 0.3
        
        for ax, (m_name, m_sig, m_color) in zip(axes, methods_data):
            ax.plot(time_axis, gt_signal, label="Ground Truth", color="black", linestyle="--", linewidth=2.5, alpha=0.8, zorder=2)
            ax.plot(time_axis, m_sig[:N_SAMPLES, target_ch], label=m_name, color=m_color, linestyle="-", linewidth=2.5, alpha=0.9, zorder=1)
            ax.set_ylabel("Amplitude (µV)", fontsize=10)
            ax.grid(True, linestyle=":", alpha=0.7)
            ax.legend(fontsize=10, loc="upper right")
            ax.set_ylim(gt_min - margin, gt_max + margin) # Fix the Y limit here!
        
        axes[-1].set_xlabel("Time (seconds)", fontsize=14)
        
        plt.xlim(0, 1.5)
        plt.tight_layout()
        
        out_path = ROOT / "results_optuna_final" / f"erp_timeseries_{ds_name}_{mode}_{scen_val}.png"
        plt.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"Generado: {out_path.name}")

if __name__ == "__main__":
    main()
