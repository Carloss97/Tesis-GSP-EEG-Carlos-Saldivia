"""
plot_radar_charts.py
====================
Generates Radar Charts comparing all 6 metrics for TRSS vs Baselines in extreme scenarios.
"""

import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results_optuna_final"

def main():
    csv_path = RESULTS_DIR / "optuna_best_results.csv"
    if not csv_path.exists(): return
        
    df = pd.read_csv(csv_path)
    datasets = df["dataset"].unique()
    
    # Let's plot for some extreme and less extreme scenarios
    scenarios = [
        {"mode": "nearby", "type": "ratio", "val": 0.4},
        {"mode": "random", "type": "ratio", "val": 0.4},
        {"mode": "nearby", "type": "ratio", "val": 0.1},
        {"mode": "random", "type": "ratio", "val": 0.1}
    ]
    
    methods = ["trss", "tikhonov", "ica", "spherical_spline", "rbfi_tps"]
    metrics = ["mae", "rmse", "snr", "dtw", "lsd", "coherence_mean"]
    colors = {"trss": "blue", "tikhonov": "cyan", "ica": "orange", "spherical_spline": "magenta", "rbfi_tps": "green"}
    
    for ds_name in datasets:
        for scen in scenarios:
            mode = scen["mode"]
            stype = scen["type"]
            val = scen["val"]
            
            df_case = df[(df["dataset"] == ds_name) & (df["missing_mode"] == mode) & (df["missing_type"] == stype) & (df["missing_val"] == val)]
            if df_case.empty: continue
            
            df_plot = df_case[df_case["method"].isin(methods)].copy()
            df_plot.set_index("method", inplace=True)
            
            norm_data = {}
            for m in metrics:
                vals = df_plot[m].values
                mx = np.max(vals)
                mn = np.min(vals)
                # Scale between 0.1 and 1.0 so the worst method is visible (0.1) instead of 0.0
                if mx == mn: 
                    norm_data[m] = np.ones_like(vals)
                else:
                    if m in ["mae", "rmse", "dtw", "lsd"]:
                        # Lower is better -> Best is 1.0, Worst is 0.1
                        norm_data[m] = 0.1 + 0.9 * (1.0 - (vals - mn) / (mx - mn))
                    else:
                        # Higher is better -> Best is 1.0, Worst is 0.1
                        norm_data[m] = 0.1 + 0.9 * ((vals - mn) / (mx - mn))
                    
            df_norm = pd.DataFrame(norm_data, index=df_plot.index)
            
            angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
            angles += angles[:1]
            
            fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
            
            for method in methods:
                if method not in df_norm.index: continue
                values = df_norm.loc[method].tolist()
                values += values[:1]
                ax.plot(angles, values, color=colors.get(method, "black"), linewidth=2, label=method.upper())
                ax.fill(angles, values, color=colors.get(method, "black"), alpha=0.1)
                
            ax.set_theta_offset(np.pi / 2)
            ax.set_theta_direction(-1)
            ax.set_thetagrids(np.degrees(angles[:-1]), [m.upper() for m in metrics], fontsize=11, fontweight="bold")
            # Set fixed radial limits to maintain scale
            ax.set_ylim(0, 1.05)
            ax.set_yticklabels([])
            
            plt.title(f"Radar Chart Multimétrica (Borde Exterior = Mejor)\n{ds_name.upper()} | {mode.capitalize()} {val}", fontsize=14, fontweight="bold", y=1.08)
            plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
            
            out_path = RESULTS_DIR / f"radar_multimetric_{ds_name}_{mode}_{val}.png"
            plt.savefig(out_path, dpi=150, bbox_inches="tight")
            plt.close()
            print(f"Radar Chart generado: {out_path.name}")

if __name__ == "__main__":
    main()
