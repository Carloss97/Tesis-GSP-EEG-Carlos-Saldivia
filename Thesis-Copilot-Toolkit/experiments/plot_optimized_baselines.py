"""
plot_optimized_baselines.py
===========================
Genera PSD y ERP para mne_sample | nearby | 0.4 utilizando
TRSS/Tikhonov optimizados (optuna_best_results.csv) y
Spline/RBFI optimizados (optuna_best_results_baselines.csv).
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
    csv_gsp = ROOT / "results_optuna_final" / "optuna_best_results.csv"
    csv_base = ROOT / "results_optuna_baselines" / "optuna_best_results_baselines.csv"
    
    df_gsp = pd.read_csv(csv_gsp)
    df_base = pd.read_csv(csv_base)
    
    ds_name = "mne_sample"
    scenarios = [
        {"mode": "nearby", "val": 0.4, "type": "ratio"},
        {"mode": "nearby", "val": 0.1, "type": "ratio"},
        {"mode": "nearby", "val": 1.0, "type": "count"},
    ]
    
    data = load_mne_sample_dataset()
    data["signals"] = data["signals"][:1000]
    signals_clean = data["signals"]
    positions = data["positions"]
    sfreq = data["info"].get("sfreq", 250.0)
    
    for scen in scenarios:
        mode = scen["mode"]
        scen_val = scen["val"]
        scen_type = scen["type"]
        
        signals_missing = simulate_mask(signals_clean, positions, scen_val, mode, random_state=42)
        
        # Extraer parámetros TRSS
        df_gsp_case = df_gsp[(df_gsp["dataset"] == ds_name) & (df_gsp["missing_mode"] == mode) & (df_gsp["missing_val"] == scen_val) & (df_gsp["missing_type"] == scen_type)]
        
        row_trss = df_gsp_case[df_gsp_case["method"] == "trss"].iloc[0]
        p_trss = ast.literal_eval(row_trss["params"])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            g = build_graph("knng", positions, signals=signals_clean, k=p_trss["k"], sigma=p_trss["sigma"])
            adj = g["adjacency"].toarray() if hasattr(g["adjacency"], "toarray") else np.asarray(g["adjacency"])
            res_trss = interpolate_signals("trss", signals_missing, adjacency=adj, alpha=p_trss["alpha"], beta=p_trss["beta"], lr=0.05, n_iter=80)
        sig_trss = res_trss["reconstructed"]

        # Extraer Baselines Optimizados
        df_base_case = df_base[(df_base["dataset"] == ds_name) & (df_base["missing_mode"] == mode) & (df_base["missing_val"] == scen_val) & (df_base["missing_type"] == scen_type)]
        
        row_ss = df_base_case[df_base_case["method"] == "spherical_spline"].iloc[0]
        p_ss = ast.literal_eval(row_ss["params"])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res_ss = interpolate_signals("spherical_spline", signals_missing, positions=positions, eps=p_ss["eps"])
        sig_ss = res_ss["reconstructed"]
        
        row_rbfi = df_base_case[df_base_case["method"] == "rbfi_tps"].iloc[0]
        p_rbfi = ast.literal_eval(row_rbfi["params"])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res_rbfi = interpolate_signals("rbfi_tps", signals_missing, positions=positions, smooth=p_rbfi["smooth"])
        sig_rbfi = res_rbfi["reconstructed"]

        # ================= PSD PLOT =================
        def get_avg_psd(sigs):
            psds = []
            freqs = None
            for d in range(sigs.shape[1]):
                mask = ~np.isnan(sigs[:, d])
                if np.sum(mask) < 64: continue
                f, pxx = welch(sigs[mask, d], fs=sfreq, nperseg=256)
                freqs = f
                psds.append(pxx)
            if not psds: return None, None
            return freqs, np.mean(psds, axis=0)

        f_c, p_c = get_avg_psd(signals_clean)
        f_trss, p_trss_v = get_avg_psd(sig_trss)
        f_ss, p_ss_v = get_avg_psd(sig_ss)
        f_rbfi, p_rbfi_v = get_avg_psd(sig_rbfi)
        
        plt.figure(figsize=(12, 7))
        plt.semilogy(f_c, p_c, label='Ground Truth', color='black', linewidth=3)
        plt.semilogy(f_ss, p_ss_v, label=f'Spherical Spline (Opt, eps={p_ss["eps"]:.1e})', color='magenta', linestyle='--', alpha=0.8, linewidth=2)
        plt.semilogy(f_rbfi, p_rbfi_v, label=f'RBFI TPS (Opt, smooth={p_rbfi["smooth"]:.2f})', color='orange', linestyle=':', alpha=0.8, linewidth=2)
        plt.semilogy(f_trss, p_trss_v, label='TRSS (GSP Opt)', color='blue', linestyle='-.', alpha=1.0, linewidth=2.5)
            
        plt.title(f'PSD Comparison with Optimized Baselines ({mode.capitalize()} {scen_val} {scen_type})', fontsize=15, fontweight='bold')
        plt.xlabel('Frequency (Hz)', fontsize=12)
        plt.ylabel('Power Spectral Density (V^2/Hz)', fontsize=12)
        plt.xlim(0.5, 45.0)
        plt.grid(True, which="both", ls="-", alpha=0.2)
        plt.legend(fontsize=12, loc='upper right')
        
        val_str = str(scen_val).replace('.','_')
        out_psd = ROOT / "results_optuna_baselines" / f"psd_optimized_baselines_{mode}_{val_str}_{scen_type}.png"
        plt.savefig(out_psd, dpi=150, bbox_inches="tight")
        plt.close()
        
        # ================= ERP PLOT =================
        N_SAMPLES = int(1.5 * sfreq)
        time_axis = np.arange(N_SAMPLES) / sfreq
        nan_channels = np.where(np.isnan(signals_missing[0, :]))[0]
        target_ch = nan_channels[0] if len(nan_channels)>0 else 0
        
        methods_data = [
            ("TRSS (GSP Opt)", sig_trss, "blue"),
            (f"Spherical Spline (Opt, eps={p_ss['eps']:.1e})", sig_ss, "magenta"),
            (f"RBFI TPS (Opt, smooth={p_rbfi['smooth']:.2f})", sig_rbfi, "orange")
        ]
        
        fig, axes = plt.subplots(3, 1, figsize=(14, 8), sharex=True, sharey=True)
        fig.suptitle(f"ERP / Time Series (Missing Channel #{target_ch}) with Optimized Baselines", fontsize=16, fontweight="bold")
        gt_signal = signals_clean[:N_SAMPLES, target_ch]
        
        for ax, (m_name, m_sig, m_color) in zip(axes, methods_data):
            ax.plot(time_axis, gt_signal, label="Ground Truth", color="black", linestyle="--", linewidth=2.5, alpha=0.8, zorder=2)
            ax.plot(time_axis, m_sig[:N_SAMPLES, target_ch], label=m_name, color=m_color, linestyle="-", linewidth=2.5, alpha=0.9, zorder=1)
            ax.set_ylabel("Amplitude (µV)", fontsize=10)
            ax.grid(True, linestyle=":", alpha=0.7)
            ax.legend(fontsize=10, loc="upper right")
        axes[-1].set_xlabel("Time (seconds)", fontsize=14)
        plt.xlim(0, 1.5)
        plt.tight_layout()
        
        out_erp = ROOT / "results_optuna_baselines" / f"erp_optimized_baselines_{mode}_{val_str}_{scen_type}.png"
        plt.savefig(out_erp, dpi=150, bbox_inches="tight")
        plt.close()
        
    print("Graficos generados exitosamente en results_optuna_baselines/")
    
    print("Graficos generados exitosamente en results_optuna_baselines/")

if __name__ == "__main__":
    main()
