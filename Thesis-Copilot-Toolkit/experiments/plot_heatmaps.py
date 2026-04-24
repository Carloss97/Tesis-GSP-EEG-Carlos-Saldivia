"""
plot_heatmaps.py
================
Generates Seaborn heatmaps (Method vs Scenario) for MAE and LSD to replace short line charts.
"""

import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results_optuna_final"

def main():
    csv_path = RESULTS_DIR / "optuna_best_results.csv"
    if not csv_path.exists(): return
        
    df = pd.read_csv(csv_path)
    df["scenario"] = df["missing_mode"] + "\n" + df["missing_type"] + "=" + df["missing_val"].astype(str)
    
    methods = ["trss", "tikhonov", "ica", "spherical_spline", "rbfi_tps"]
    
    for ds in df["dataset"].unique():
        df_ds = df[df["dataset"] == ds].copy()
        
        # Pivot tables
        pivot_mae = df_ds.pivot(index="method", columns="scenario", values="mae").reindex(methods)
        pivot_lsd = df_ds.pivot(index="method", columns="scenario", values="lsd").reindex(methods)
        
        fig, axes = plt.subplots(2, 1, figsize=(14, 10))
        fig.suptitle(f"Performance Heatmap - {ds.upper()}", fontsize=16, fontweight='bold')
        
        sns.heatmap(pivot_mae, annot=True, fmt=".2e", cmap="YlOrRd", ax=axes[0], cbar_kws={'label': 'MAE'})
        axes[0].set_title("Mean Absolute Error (MAE) - Lower is Better")
        axes[0].set_ylabel("Method")
        axes[0].set_xlabel("")
        
        sns.heatmap(pivot_lsd, annot=True, fmt=".3f", cmap="YlGnBu", ax=axes[1], cbar_kws={'label': 'LSD'})
        axes[1].set_title("Log Spectral Distance (LSD) - Lower is Better")
        axes[1].set_ylabel("Method")
        axes[1].set_xlabel("Scenario")
        
        plt.tight_layout()
        out_path = RESULTS_DIR / f"heatmap_performance_{ds}.png"
        plt.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"Heatmap generado: {out_path.name}")

if __name__ == "__main__":
    main()
