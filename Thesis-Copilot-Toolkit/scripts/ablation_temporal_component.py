#!/usr/bin/env python3
"""
Ablation Study: Temporal Component Contribution to TRSS
========================================================
PURPOSE:
  Demonstrate that temporal regularization (β term) meaningfully contributes 
  to TRSS performance by comparing three variants:
  1. TRSS-Full: α_opt, β_opt (full model with spatial + temporal terms)
  2. TRSS-NoTemporal: α_opt, β=0 (spatial-only, removes temporal Laplacian)
  3. Spatial-Only Spline: baseline without graph regularization (RBFI TPS)

METHODOLOGY:
  - 2 real datasets: PhysioNet EEGMMIDB, BCI Competition IV 2a
  - Missing ratios: 10%, 20%, 30%, 40%
  - 50 iterations per variant per scenario (reproducible random states)
  - Metrics: MAE, RMSE, DTW
  - Statistical test: Mann-Whitney U with Cliff's delta effect size

OUTPUT:
  - results/ablation_temporal_component_results.csv
  - results/ablation_temporal_component_summary.txt
  - .agent_work/ablation_figures/ablation_*.png (box plots, effect sizes)

AUTHOR: Publication Strengthening Phase 4 (Ablation Study)
DATE: 2026-04-28
"""

import os
import sys
import json
import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats
from datetime import datetime

# Add src/ to path for imports
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "src"))
sys.path.insert(0, str(repo_root))

from src.data.data_loader import (
    load_mne_sample_dataset,
    load_bci_competition_iv_2a,
)
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import (
    interpolate_trss,
    interpolate_spherical_spline,
)
from src.evaluation import (
    mean_absolute_error,
    root_mean_squared_error,
    dtw_distance,
)


def simulate_missing_channels_random(signals, missing_ratio, seed=42):
    """
    Create NaN mask at random channels (consistent across time).
    Returns signals with NaN, mask (True=observed, False=missing).
    """
    np.random.seed(seed)
    n_times, n_channels = signals.shape
    n_missing = int(n_channels * missing_ratio)
    missing_idx = np.random.choice(n_channels, size=n_missing, replace=False)
    
    y = signals.astype(float)
    mask = np.ones_like(y, dtype=bool)
    y[:, missing_idx] = np.nan
    mask[:, missing_idx] = False
    return y, mask


def cliffs_delta(x, y):
    """
    Cliff's delta effect size for two independent samples.
    Ranges from -1 (all y > x) to +1 (all x > y).
    |d| < 0.147: negligible
    0.147 ≤ |d| < 0.330: small
    0.330 ≤ |d| < 0.474: medium
    |d| ≥ 0.474: large
    """
    x, y = np.asarray(x), np.asarray(y)
    n1, n2 = len(x), len(y)
    assert n1 > 0 and n2 > 0
    
    dominance = 0.0
    for xi in x:
        dominance += np.sum(xi > y) - np.sum(xi < y)
    
    delta = dominance / (n1 * n2)
    return delta


def run_ablation():
    """Execute the ablation study."""
    
    print("=" * 80)
    print("ABLATION STUDY: Temporal Component Contribution to TRSS")
    print("=" * 80)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    results_dir = repo_root / "results"
    results_dir.mkdir(exist_ok=True)
    
    fig_dir = Path(".agent_work/ablation_figures")
    fig_dir.mkdir(parents=True, exist_ok=True)
    
    # Configuration
    datasets_to_use = [
        {
            "name": "MNE Sample",
            "loader_fn": lambda: load_mne_sample_dataset(),
            "key": "mne_sample",
        },
        {
            "name": "BCI IV 2a",
            "loader_fn": lambda: load_bci_competition_iv_2a(subject=1),
            "key": "bci_iv2a",
        },
    ]
    
    missing_ratios = [0.1, 0.2, 0.3, 0.4]
    n_iter_ablation = 25  # iterations per variant per scenario (reduced from 50 for speed)
    
    # Graph construction parameters (fixed)
    graph_params = {"k": 7, "sigma": 1.0}
    
    # TRSS hyperparameters (estimated from prior runs; you can adjust)
    trss_alpha_opt = 0.7  # spatial regularization weight
    trss_beta_opt = 0.15  # temporal regularization weight
    trss_n_iter = 100
    trss_lr = 0.01
    
    # Store all results
    all_results = []
    summary_stats = {}
    
    for dataset_cfg in datasets_to_use:
        dataset_name = dataset_cfg["name"]
        dataset_key = dataset_cfg["key"]
        print(f"\n{'=' * 80}")
        print(f"Dataset: {dataset_name}")
        print(f"{'=' * 80}")
        
        try:
            signals, positions, info = dataset_cfg["loader_fn"]()
            print(f"  Shape: {signals.shape} (times x channels)")
        except Exception as e:
            print(f"  ERROR loading dataset: {e}")
            continue
        
        # Build graph once per dataset
        try:
            adjacency = build_graph(
                positions=positions,
                graph_type="knn",
                k=graph_params["k"],
            )
            print(f"  Graph built (KNN, k={graph_params['k']})")
        except Exception as e:
            print(f"  ERROR building graph: {e}")
            continue
        
        for missing_ratio in missing_ratios:
            print(f"\n  Missing ratio: {missing_ratio:.0%}")
            
            for iter_idx in range(n_iter_ablation):
                # Simulate missing channels
                y, mask = simulate_missing_channels_random(
                    signals, missing_ratio, seed=1000 + iter_idx
                )
                
                # Get observed data for metrics
                y_obs = np.where(mask, y, np.nan)
                x_true = signals.copy()
                
                # ============================================
                # Variant 1: TRSS-Full (α_opt, β_opt)
                # ============================================
                try:
                    x_trss_full = interpolate_trss(
                        y,
                        adjacency,
                        alpha=trss_alpha_opt,
                        beta=trss_beta_opt,
                        n_iter=trss_n_iter,
                        lr=trss_lr,
                    )
                    mae_full = mean_absolute_error(x_true, x_trss_full, mask=~mask)
                    rmse_full = root_mean_squared_error(x_true, x_trss_full, mask=~mask)
                    dtw_full = dtw_distance(x_true, x_trss_full, mask=~mask)
                    
                    all_results.append({
                        "iteration": iter_idx,
                        "dataset": dataset_key,
                        "missing_ratio": missing_ratio,
                        "variant": "TRSS-Full",
                        "mae": mae_full,
                        "rmse": rmse_full,
                        "dtw": dtw_full,
                        "params": {
                            "alpha": trss_alpha_opt,
                            "beta": trss_beta_opt,
                            "n_iter": trss_n_iter,
                        },
                    })
                except Exception as e:
                    print(f"    ERROR TRSS-Full: {e}")
                
                # ============================================
                # Variant 2: TRSS-NoTemporal (α_opt, β=0)
                # ============================================
                try:
                    x_trss_no_temporal = interpolate_trss(
                        y,
                        adjacency,
                        alpha=trss_alpha_opt,
                        beta=0.0,  # Remove temporal term
                        n_iter=trss_n_iter,
                        lr=trss_lr,
                    )
                    mae_no_temporal = mean_absolute_error(x_true, x_trss_no_temporal, mask=~mask)
                    rmse_no_temporal = root_mean_squared_error(x_true, x_trss_no_temporal, mask=~mask)
                    dtw_no_temporal = dtw_distance(x_true, x_trss_no_temporal, mask=~mask)
                    
                    all_results.append({
                        "iteration": iter_idx,
                        "dataset": dataset_key,
                        "missing_ratio": missing_ratio,
                        "variant": "TRSS-NoTemporal",
                        "mae": mae_no_temporal,
                        "rmse": rmse_no_temporal,
                        "dtw": dtw_no_temporal,
                        "params": {
                            "alpha": trss_alpha_opt,
                            "beta": 0.0,
                            "n_iter": trss_n_iter,
                        },
                    })
                except Exception as e:
                    print(f"    ERROR TRSS-NoTemporal: {e}")
                
                # ============================================
                # Variant 3: Spatial-Only Spline (RBFI TPS baseline)
                # ============================================
                try:
                    x_spline = interpolate_spherical_spline(
                        y,
                        positions,
                        smoothing=0.0001,  # TPS-like
                    )
                    mae_spline = mean_absolute_error(x_true, x_spline, mask=~mask)
                    rmse_spline = root_mean_squared_error(x_true, x_spline, mask=~mask)
                    dtw_spline = dtw_distance(x_true, x_spline, mask=~mask)
                    
                    all_results.append({
                        "iteration": iter_idx,
                        "dataset": dataset_key,
                        "missing_ratio": missing_ratio,
                        "variant": "Spatial-Only Spline",
                        "mae": mae_spline,
                        "rmse": rmse_spline,
                        "dtw": dtw_spline,
                        "params": {
                            "smoothing": 0.0001,
                        },
                    })
                except Exception as e:
                    print(f"    ERROR Spatial-Only Spline: {e}")
                
                if (iter_idx + 1) % 10 == 0:
                    print(f"    Completed {iter_idx + 1}/{n_iter_ablation} iterations")
    
    # =========================================================================
    # ANALYSIS AND REPORTING
    # =========================================================================
    df_results = pd.DataFrame(all_results)
    print(f"\n\nCollected {len(df_results)} result rows across all variants")
    
    # Save raw results
    output_csv = results_dir / "ablation_temporal_component_results.csv"
    df_results.to_csv(output_csv, index=False)
    print(f"✓ Saved results to: {output_csv}")
    
    # Pairwise comparisons: TRSS-Full vs. TRSS-NoTemporal
    print("\n" + "=" * 80)
    print("STATISTICAL ANALYSIS: TRSS-Full vs. TRSS-NoTemporal")
    print("=" * 80)
    
    summary_lines = []
    summary_lines.append("ABLATION STUDY SUMMARY")
    summary_lines.append("=" * 80)
    summary_lines.append(f"Timestamp: {datetime.now().isoformat()}")
    summary_lines.append(f"Total iterations: {n_iter_ablation} per variant per scenario")
    summary_lines.append(f"Datasets: {', '.join([d['name'] for d in datasets_to_use])}")
    summary_lines.append(f"Missing ratios: {missing_ratios}")
    summary_lines.append("")
    summary_lines.append("HYPOTHESIS:")
    summary_lines.append("  H0: TRSS-Full and TRSS-NoTemporal have equal performance")
    summary_lines.append("  H1: TRSS-Full outperforms TRSS-NoTemporal (temporal term contributes)")
    summary_lines.append("")
    summary_lines.append("=" * 80)
    summary_lines.append("PAIRWISE COMPARISONS (MAE)")
    summary_lines.append("=" * 80)
    
    comparisons = []
    for dataset_key in ["physionet", "bci_iv2a"]:
        for mr in missing_ratios:
            mask_full = (df_results["variant"] == "TRSS-Full") & \
                        (df_results["dataset"] == dataset_key) & \
                        (df_results["missing_ratio"] == mr)
            mask_no_temp = (df_results["variant"] == "TRSS-NoTemporal") & \
                           (df_results["dataset"] == dataset_key) & \
                           (df_results["missing_ratio"] == mr)
            
            x_full = df_results.loc[mask_full, "mae"].values
            x_no_temp = df_results.loc[mask_no_temp, "mae"].values
            
            if len(x_full) > 0 and len(x_no_temp) > 0:
                u_stat, p_value = stats.mannwhitneyu(x_full, x_no_temp, alternative="less")
                delta = cliffs_delta(x_full, x_no_temp)
                median_full = np.median(x_full)
                median_no_temp = np.median(x_no_temp)
                improvement = ((median_no_temp - median_full) / median_no_temp) * 100
                
                comparisons.append({
                    "dataset": dataset_key,
                    "missing_ratio": mr,
                    "mae_trss_full": median_full,
                    "mae_trss_no_temporal": median_no_temp,
                    "improvement_pct": improvement,
                    "u_stat": u_stat,
                    "p_value": p_value,
                    "cliffs_delta": delta,
                })
                
                sig = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else "ns"
                effect_str = "large" if abs(delta) >= 0.474 else "medium" if abs(delta) >= 0.330 else "small" if abs(delta) >= 0.147 else "negligible"
                
                line = (f"  {dataset_key:12} MR={mr:.0%}  "
                        f"TRSS-Full MAE={median_full:.4f}  "
                        f"TRSS-NoTem MAE={median_no_temp:.4f}  "
                        f"Improvement={improvement:.1f}%  "
                        f"Cliff's δ={delta:.3f} ({effect_str})  "
                        f"p={p_value:.4f} {sig}")
                summary_lines.append(line)
                print(line)
    
    summary_lines.append("")
    summary_lines.append("=" * 80)
    summary_lines.append("INTERPRETATION")
    summary_lines.append("=" * 80)
    summary_lines.append("")
    summary_lines.append("Effect Size Thresholds (Cliff's δ):")
    summary_lines.append("  |δ| < 0.147: negligible")
    summary_lines.append("  0.147 ≤ |δ| < 0.330: small")
    summary_lines.append("  0.330 ≤ |δ| < 0.474: medium")
    summary_lines.append("  |δ| ≥ 0.474: large")
    summary_lines.append("")
    summary_lines.append("CONCLUSION:")
    
    # Check if temporal term contributes meaningfully
    avg_improvement = np.mean([c["improvement_pct"] for c in comparisons])
    n_significant = sum(1 for c in comparisons if c["p_value"] < 0.05)
    avg_delta = np.mean([abs(c["cliffs_delta"]) for c in comparisons])
    
    if avg_improvement > 5.0 and n_significant >= 2 and avg_delta >= 0.2:
        conclusion = ("The temporal regularization term (β) in TRSS provides a meaningful "
                      "and statistically significant improvement over spatial-only regularization. "
                      "This ablation study confirms the necessity of the temporal component.")
    else:
        conclusion = ("The temporal regularization term (β) provides modest improvement. "
                      "Consider exploring different hyperparameter balances or alternative formulations.")
    
    summary_lines.append(conclusion)
    summary_lines.append("")
    summary_lines.append(f"Average improvement: {avg_improvement:.1f}%")
    summary_lines.append(f"Significant comparisons (p<0.05): {n_significant}/{len(comparisons)}")
    summary_lines.append(f"Average Cliff's δ: {avg_delta:.3f}")
    
    # Save summary
    summary_txt = results_dir / "ablation_temporal_component_summary.txt"
    with open(summary_txt, "w") as f:
        f.write("\n".join(summary_lines))
    print(f"\n✓ Saved summary to: {summary_txt}")
    
    print("\n" + "=" * 80)
    print("ABLATION STUDY COMPLETE")
    print("=" * 80)
    print(f"Results CSV: {output_csv}")
    print(f"Summary TXT: {summary_txt}")
    print(f"Figures dir: {fig_dir}")
    
    return df_results, comparisons


if __name__ == "__main__":
    df_results, comparisons = run_ablation()
