"""
plot_degradation_curves.py
==========================
Generates line plots showing progressive degradation (MAE/LSD) and Trade-off scatterplots.
"""

import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results_optuna_final"

def main():
    csv_path = RESULTS_DIR / "optuna_best_results.csv"
    if not csv_path.exists():
        print(f"[ERROR] No se encontró {csv_path}")
        return
        
    df = pd.read_csv(csv_path)
    # Ensure missing_val is sorted
    df = df.sort_values(by="missing_val")
    
    datasets = df["dataset"].unique()
    modes = df["missing_mode"].unique()
    types = df["missing_type"].unique()
    
    method_order = ["trss", "tikhonov", "ica", "spherical_spline", "rbfi_tps"]
    colors = sns.color_palette("Set1", n_colors=len(method_order))
    palette = dict(zip(method_order, colors))

    # 1. Line plots (Degradation Curves)
    for ds in datasets:
        for mode in modes:
            for t in types:
                df_sub = df[(df["dataset"] == ds) & (df["missing_mode"] == mode) & (df["missing_type"] == t)].copy()
                if df_sub.empty: continue
                
                fig, axes = plt.subplots(1, 2, figsize=(16, 6))
                title_suffix = f"({ds.upper()}) | Mode: {mode.capitalize()} | Type: {t.capitalize()}"
                fig.suptitle(f"Progressive Degradation Curves {title_suffix}", fontsize=16, fontweight='bold')
                
                # MAE
                sns.lineplot(data=df_sub, x="missing_val", y="mae", hue="method", hue_order=method_order,
                             style="method", markers=True, dashes=False, ax=axes[0], palette=palette, linewidth=2.5, markersize=10)
                axes[0].set_title("Mean Absolute Error (MAE)")
                axes[0].set_xlabel(f"Missing {t.capitalize()}")
                axes[0].set_ylabel("MAE")
                axes[0].grid(True, linestyle='--', alpha=0.7)
                
                # LSD
                sns.lineplot(data=df_sub, x="missing_val", y="lsd", hue="method", hue_order=method_order,
                             style="method", markers=True, dashes=False, ax=axes[1], palette=palette, linewidth=2.5, markersize=10)
                axes[1].set_title("Log Spectral Distance (LSD) [0.5 - 45 Hz]")
                axes[1].set_xlabel(f"Missing {t.capitalize()}")
                axes[1].set_ylabel("LSD")
                axes[1].grid(True, linestyle='--', alpha=0.7)
                if axes[1].get_legend() is not None:
                    axes[1].get_legend().remove()
                
                out_path = RESULTS_DIR / f"degradation_{ds}_{mode}_{t}.png"
                plt.tight_layout()
                plt.savefig(out_path, dpi=150, bbox_inches="tight")
                plt.close()
                print(f"Generado: {out_path.name}")
                
    # 2. Scatterplot Trade-off (MAE vs LSD)
    for ds in datasets:
        df_ds = df[df["dataset"] == ds]
        plt.figure(figsize=(10, 8))
        sns.scatterplot(data=df_ds, x="mae", y="lsd", hue="method", style="missing_mode", 
                        palette=palette, s=150, alpha=0.8, edgecolor='k')
        plt.title(f"Multi-Objective Trade-off (MAE vs LSD) - {ds.upper()}", fontsize=14, fontweight='bold')
        plt.xlabel("MAE (Temporal Error) -> Lower is Better")
        plt.ylabel("LSD (Spectral Error) -> Lower is Better")
        plt.grid(True, linestyle='--', alpha=0.5)
        
        # Add an annotation for Pareto Front ideally
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        out_path = RESULTS_DIR / f"tradeoff_scatter_{ds}.png"
        plt.tight_layout()
        plt.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"Generado: {out_path.name}")

if __name__ == "__main__":
    main()
