"""
plot_global_comparison.py
=========================
Generates global visualization dashboards to compare MAE and LSD across methods, datasets, and scenarios.
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
    
    # Create a clean scenario label
    df["scenario_label"] = df["missing_mode"] + "_" + df["missing_type"] + "_" + df["missing_val"].astype(str)
    
    # We want to plot MAE and LSD for each dataset
    datasets = df["dataset"].unique()
    
    for ds in datasets:
        df_ds = df[df["dataset"] == ds].copy()
        
        # Filter methods if needed, or just sort them
        method_order = ["trss", "tikhonov", "ica", "spherical_spline", "rbfi_tps"]
        
        fig, axes = plt.subplots(2, 1, figsize=(16, 12), sharex=True)
        fig.suptitle(f'Comparación Global de Métodos - Dataset: {ds}', fontsize=16, fontweight='bold')
        
        # Subplot 1: MAE
        sns.barplot(data=df_ds, x="scenario_label", y="mae", hue="method", hue_order=method_order, ax=axes[0], palette="Set2")
        axes[0].set_title('Mean Absolute Error (MAE) - Menor es Mejor')
        axes[0].set_ylabel('MAE')
        axes[0].grid(axis='y', linestyle='--', alpha=0.7)
        axes[0].legend(title='Método', bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # Subplot 2: LSD
        sns.barplot(data=df_ds, x="scenario_label", y="lsd", hue="method", hue_order=method_order, ax=axes[1], palette="Set2")
        axes[1].set_title('Log Spectral Distance (LSD) [0.5 - 45 Hz] - Menor es Mejor')
        axes[1].set_ylabel('LSD')
        axes[1].grid(axis='y', linestyle='--', alpha=0.7)
        if axes[1].get_legend() is not None:
            axes[1].get_legend().remove() # only need one legend
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        out_path = RESULTS_DIR / f"global_comparison_{ds}.png"
        plt.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"Gráfico global guardado en {out_path}")

if __name__ == "__main__":
    main()
