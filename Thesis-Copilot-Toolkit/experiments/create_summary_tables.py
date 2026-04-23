"""
create_summary_tables.py
========================
Generates a consolidated Pivot Table CSV summarizing average performance across datasets.
"""

import os
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results_optuna_final"

def main():
    csv_path = RESULTS_DIR / "optuna_best_results.csv"
    if not csv_path.exists(): return
        
    df = pd.read_csv(csv_path)
    
    # 1. Pivot por Dataset, Métrica y Método
    metrics = ["mae", "rmse", "snr", "dtw", "lsd", "coherence_mean"]
    
    # Group by method and dataset, and take the mean of each metric across all scenarios
    agg_df = df.groupby(["dataset", "method"])[metrics].mean().reset_index()
    
    # Pivot to make it easy to read: Rows = Method, Cols = (Dataset, Metric)
    pivot_df = agg_df.pivot(index="method", columns="dataset", values=metrics)
    
    # Flatten multi-index columns for CSV export
    pivot_df.columns = [f"{col[1]}_{col[0]}" for col in pivot_df.columns.values]
    pivot_df.reset_index(inplace=True)
    
    out_path = RESULTS_DIR / "optuna_summary_pivot.csv"
    pivot_df.to_csv(out_path, index=False)
    print(f"Pivot table guardada en: {out_path.name}")

if __name__ == "__main__":
    main()
