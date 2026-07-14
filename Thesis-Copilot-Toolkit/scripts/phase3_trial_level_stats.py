#!/usr/bin/env python3
"""
Phase 3: Trial-Level Statistical Analysis

Aggregates data from all iterations and performs granular pairwise
comparisons across methods using Wilcoxon signed-rank test and Cliff's delta.
Outputs LaTeX table and summary for thesis/paper integration.
"""

import sys
import os
import re
import glob
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import wilcoxon, mannwhitneyu

# Add project root
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

RESULTS_DIR = os.path.join(project_root, 'results')
OUTPUT_DIR = os.path.join(project_root, 'results', 'tablas_resumen')
WORK_DIR = os.path.join(project_root, '.agent_work')

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(WORK_DIR, exist_ok=True)


METHOD_DISPLAY_NAMES = {
    'sobolev': 'Sobolev',
    'trss': 'TRSS',
    'tikhonov': 'Tikhonov',
    'spherical_spline': 'Spherical Spline',
    'spherical_s': 'Spherical Spline',
    'rbfi_tps': 'RBF (TPS)',
    'temporal_laplacian': 'Temporal Laplacian',
    'temporal_la': 'Temporal Laplacian',
    'tv': 'Temporal Variation',
    'idw': 'IDW',
    'linear': 'Linear',
    'ica': 'ICA',
    'bgsrp': 'BGSRP',
    'visibility_nnk': 'Visibility NNK',
}


def format_method_label(method_name):
    """Return a LaTeX-safe display label for an internal method identifier."""
    label = METHOD_DISPLAY_NAMES.get(method_name, method_name.replace('_', r'\_'))
    wrapped_labels = {
        'Temporal Laplacian': r'\shortstack{Temporal\\Laplacian}',
        'Spherical Spline': r'\shortstack{Spherical\\Spline}',
        'Temporal Variation': r'\shortstack{Temporal\\Variation}',
    }
    return wrapped_labels.get(label, label)


def cliffs_delta(x, y):
    """
    Compute Cliff's delta effect size.
    Interpretation: |d| < 0.147: negligible, 0.147-0.330: small, 
    0.330-0.474: medium, > 0.474: large
    """
    x = np.asarray(x).flatten()
    y = np.asarray(y).flatten()
    nx, ny = len(x), len(y)
    
    # Count how many times x[i] > y[j]
    greater = 0
    for xi in x:
        greater += np.sum(xi > y)
    
    # Cliff's delta formula
    delta = (2 * greater - nx * ny) / (nx * ny)
    return delta


def bootstrap_ci_median(data, alpha=0.05, n_boot=10000):
    """
    Compute bootstrap 95% confidence interval for the median.
    Returns (median, lower_ci, upper_ci)
    """
    data = np.asarray(data).flatten()
    med_orig = np.median(data)
    
    boot_meds = []
    for _ in range(n_boot):
        boot_sample = np.random.choice(data, size=len(data), replace=True)
        boot_meds.append(np.median(boot_sample))
    
    boot_meds = np.array(boot_meds)
    lower = np.percentile(boot_meds, 100 * (alpha / 2))
    upper = np.percentile(boot_meds, 100 * (1 - alpha / 2))
    return med_orig, lower, upper


def load_all_stats():
    """
    Load all *_stats.csv files from results directory.
    Returns a combined DataFrame with iteration and method info.
    """
    stats_files = sorted(glob.glob(os.path.join(RESULTS_DIR, 'it*_stats.csv')))
    
    dfs = []
    for fpath in stats_files:
        try:
            df = pd.read_csv(fpath)
            # Extract iteration ID
            match = re.search(r'(it[^_]*)', os.path.basename(fpath))
            if match:
                iteration_id = match.group(1)
                df['iteration'] = iteration_id
                dfs.append(df)
        except Exception as e:
            print(f"Warning: could not load {fpath}: {e}")
    
    if not dfs:
        raise ValueError("No stats.csv files found.")
    
    combined = pd.concat(dfs, ignore_index=True)
    print(f"Loaded {len(dfs)} iteration files, {len(combined)} total rows.")
    return combined


def pairwise_analysis(combined_df, metric='mae_median'):
    """
    Perform pairwise comparisons across all methods using trial-level data.
    For each pair of methods, compute Wilcoxon p-value, Cliff's delta, 
    median values, and bootstrap CIs.
    
    Excludes visibility_nnk due to suspected implementation error (consistent outlier).
    """
    methods = sorted(combined_df['method'].unique())
    
    # EXCLUDE visibility_nnk (implementation error, consistent outlier)
    methods = [m for m in methods if m != 'visibility_nnk']
    
    print(f"Found {len(methods)} unique methods (excluding visibility_nnk): {methods[:5]}... (showing first 5)")
    
    results = []
    
    for i, m1 in enumerate(methods):
        for m2 in methods[i+1:]:
            data_m1 = combined_df[combined_df['method'] == m1][metric].dropna().values
            data_m2 = combined_df[combined_df['method'] == m2][metric].dropna().values
            
            # Wilcoxon signed-rank test (paired if same size, Mann-Whitney otherwise)
            try:
                if len(data_m1) > 0 and len(data_m2) > 0:
                    # Use Mann-Whitney (unpaired) for flexibility
                    stat, pval = mannwhitneyu(data_m1, data_m2, alternative='two-sided')
                    
                    # Cliff's delta
                    delta = cliffs_delta(data_m1, data_m2)
                    
                    # Medians and bootstrap CIs
                    med_m1, ci_m1_lower, ci_m1_upper = bootstrap_ci_median(data_m1)
                    med_m2, ci_m2_lower, ci_m2_upper = bootstrap_ci_median(data_m2)
                    
                    # Winner determination
                    if med_m1 < med_m2:
                        winner = m1
                        benefit = med_m2 - med_m1
                    else:
                        winner = m2
                        benefit = med_m1 - med_m2
                    
                    results.append({
                        'method_a': m1,
                        'method_b': m2,
                        'n_a': len(data_m1),
                        'n_b': len(data_m2),
                        'median_a': med_m1,
                        'ci_a_lower': ci_m1_lower,
                        'ci_a_upper': ci_m1_upper,
                        'median_b': med_m2,
                        'ci_b_lower': ci_m2_lower,
                        'ci_b_upper': ci_m2_upper,
                        'p_value': pval,
                        'cliffs_delta': delta,
                        'winner': winner,
                        'benefit': benefit,
                    })
            except Exception as e:
                print(f"Warning: comparison {m1} vs {m2} failed: {e}")
    
    df_results = pd.DataFrame(results)
    df_results = df_results.sort_values('p_value')
    return df_results


def generate_latex_table(df_results, metric='MAE', output_file=None):
    """
    Generate LaTeX table from pairwise results.
    """
    if output_file is None:
        output_file = os.path.join(OUTPUT_DIR, 'phase3_trial_level_table.tex')
    
    latex_lines = []
    latex_lines.append(r'\begin{table}[ht]')
    latex_lines.append(r'\centering')
    latex_lines.append(r'\caption{Phase 3 Trial-Level Pairwise Analysis: MAE (Median) Comparisons. '
                       r'Mann-Whitney test with Cliff delta effect size. '
                       r'Significant: $p < 0.05$ (*, **=0.01, ***=0.001).}')
    latex_lines.append(r'\label{tab:phase3_trial_level}')
    latex_lines.append(r'\resizebox{\linewidth}{!}{%')
    latex_lines.append(r'\begin{tabular}{llrrrrrr}')
    latex_lines.append(r'\toprule')
    latex_lines.append(r'Method A & Method B & Med.~A & Med.~B & $p$ & $\delta$ & Winner & Diff \\')
    latex_lines.append(r'\midrule')
    
    sig_threshold = 0.05
    for _, row in df_results.head(30).iterrows():
        m_a = format_method_label(row['method_a'])
        m_b = format_method_label(row['method_b'])
        med_a = row['median_a']
        med_b = row['median_b']
        pval = row['p_value']
        delta = row['cliffs_delta']
        winner = format_method_label(row['winner'])
        benefit = row['benefit']
        
        # Significance marker
        if pval < 0.001:
            sig_mark = '$^{***}$'
        elif pval < 0.01:
            sig_mark = '$^{**}$'
        elif pval < sig_threshold:
            sig_mark = '$^{*}$'
        else:
            sig_mark = ''
        
        # Simple format without bold (avoid LaTeX issues in tables)
        latex_lines.append(
            f'{m_a} & {m_b} & {med_a:.4f} & {med_b:.4f} & '
            f'{pval:.1e}{sig_mark} & {delta:.2f} & {winner} & {benefit:.3f} \\\\'
        )
    
    latex_lines.append(r'\bottomrule')
    latex_lines.append(r'\end{tabular}')
        latex_lines.append(r'}')
    latex_lines.append(r'\footnotesize Note: Med.~=~median MAE; $\delta$~=~Cliff delta; Diff~=~absolute difference.')
    latex_lines.append(r'\end{table}')
    
    latex_content = '\n'.join(latex_lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print(f"LaTeX table written to {output_file}")
    return output_file


def generate_summary(df_results, output_file=None):
    """
    Generate human-readable summary of trial-level findings.
    """
    if output_file is None:
        output_file = os.path.join(WORK_DIR, 'PHASE3_TRIAL_LEVEL_SUMMARY.txt')
    
    lines = []
    lines.append("=" * 80)
    lines.append("PHASE 3: TRIAL-LEVEL STATISTICAL ANALYSIS SUMMARY")
    lines.append("=" * 80)
    lines.append("")
    
    # Top 10 most significant differences
    lines.append("TOP 10 MOST SIGNIFICANT PAIRWISE DIFFERENCES (by p-value)")
    lines.append("-" * 80)
    for i, (_, row) in enumerate(df_results.head(10).iterrows(), 1):
        method_a = format_method_label(row['method_a'])
        method_b = format_method_label(row['method_b'])
        winner = format_method_label(row['winner'])
        lines.append(f"\n{i}. {method_a} vs {method_b}")
        lines.append(f"   Median {method_a}: {row['median_a']:.6f} "
                     f"({row['ci_a_lower']:.6f}–{row['ci_a_upper']:.6f})")
        lines.append(f"   Median {method_b}: {row['median_b']:.6f} "
                     f"({row['ci_b_lower']:.6f}–{row['ci_b_upper']:.6f})")
        lines.append(f"   p-value: {row['p_value']:.6f} {'***' if row['p_value'] < 0.001 else '**' if row['p_value'] < 0.01 else '*' if row['p_value'] < 0.05 else '(ns)'}")
        lines.append(f"   Cliff's delta: {row['cliffs_delta']:.4f}")
        lines.append(f"   Winner: {winner} (benefit: {row['benefit']:.6f})")
    
    lines.append("\n" + "=" * 80)
    lines.append(f"Total pairwise comparisons: {len(df_results)}")
    lines.append(f"Significant comparisons (p < 0.05): {len(df_results[df_results['p_value'] < 0.05])}")
    lines.append(f"Highly significant (p < 0.001): {len(df_results[df_results['p_value'] < 0.001])}")
    lines.append("=" * 80)
    
    summary_text = '\n'.join(lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(summary_text)
    
    print(f"Summary written to {output_file}")
    return output_file


def save_csv_results(df_results, output_file=None):
    """
    Save pairwise results as CSV for reference.
    """
    if output_file is None:
        output_file = os.path.join(RESULTS_DIR, 'phase3_trial_level_stats.csv')
    
    df_results.to_csv(output_file, index=False)
    print(f"Results CSV written to {output_file}")
    return output_file


def main():
    print("=" * 80)
    print("PHASE 3: TRIAL-LEVEL STATISTICAL ANALYSIS")
    print("=" * 80)
    
    # Load all iteration stats
    print("\n[1] Loading all iteration statistics...")
    combined_df = load_all_stats()
    print(f"    Total rows: {len(combined_df)}")
    print(f"    Metrics available: {list(combined_df.columns)}")
    
    # Perform pairwise analysis
    print("\n[2] Performing pairwise trial-level analysis (metric: mae_median)...")
    df_results = pairwise_analysis(combined_df, metric='mae_median')
    print(f"    Completed {len(df_results)} comparisons.")
    
    # Generate outputs
    print("\n[3] Generating outputs...")
    csv_file = save_csv_results(df_results)
    latex_file = generate_latex_table(df_results, metric='MAE (Median)')
    summary_file = generate_summary(df_results)
    
    print("\n" + "=" * 80)
    print("PHASE 3 COMPLETE")
    print("=" * 80)
    print(f"CSV Results:      {csv_file}")
    print(f"LaTeX Table:      {latex_file}")
    print(f"Summary Report:   {summary_file}")
    print("=" * 80)


if __name__ == '__main__':
    main()
