"""
scratch_plot_multi.py — Multi-metric plotting utility

Generates multi-panel comparison plots for interpolation methods across
multiple metrics (MAE, RMSE, DTW, LSD, SNR, Coherence).

Used for generating visual summaries during the thesis/paper writing process.
"""
import os
import sys
import glob
import json
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────

METRICS = ["mae", "rmse", "dtw", "lsd", "snr", "coherence"]
METRIC_LABELS = {
    "mae": "MAE",
    "rmse": "RMSE",
    "dtw": "DTW",
    "lsd": "LSD",
    "snr": "SNR (dB)",
    "coherence": "Coherencia",
}
HIGHER_IS_BETTER = {"snr", "coherence"}

DEFAULT_RESULTS_DIR = os.path.join(
    os.path.dirname(__file__), "results_optuna_final"
)


def load_results(results_dir: str) -> pd.DataFrame:
    """Load all CSV results from a directory into a single DataFrame."""
    csvs = glob.glob(os.path.join(results_dir, "*.csv"))
    if not csvs:
        raise FileNotFoundError(f"No CSV files found in {results_dir}")
    frames = []
    for csv_path in csvs:
        try:
            df = pd.read_csv(csv_path)
            frames.append(df)
        except Exception as e:
            print(f"Warning: could not read {csv_path}: {e}")
    if not frames:
        raise ValueError("No valid CSV files loaded")
    return pd.concat(frames, ignore_index=True)


def normalize_metric(series: pd.Series, metric: str) -> pd.Series:
    """Normalize a metric series to [0, 1]. Higher = better for all."""
    s = series.copy()
    s = s.replace([np.inf, -np.inf], np.nan)
    vmin, vmax = s.min(), s.max()
    if vmax == vmin:
        return pd.Series(0.5, index=s.index)
    normed = (s - vmin) / (vmax - vmin)
    if metric not in HIGHER_IS_BETTER:
        normed = 1.0 - normed
    return normed


def plot_radar(df: pd.DataFrame, methods: list, metrics: list, title: str, ax=None):
    """Plot a radar / spider chart comparing methods across metrics."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
    angles += angles[:1]  # close polygon

    labels = [METRIC_LABELS.get(m, m) for m in metrics]

    for method in methods:
        row = df[df["method"] == method]
        if row.empty:
            continue
        values = []
        for m in metrics:
            col = f"{m}_norm"
            if col in row.columns:
                values.append(row[col].values[0])
            else:
                values.append(0)
        values += values[:1]
        ax.plot(angles, values, linewidth=2, label=method)
        ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, size=10)
    ax.set_ylim(0, 1)
    ax.set_title(title, size=14, pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0), fontsize=8)
    return ax


def plot_bar_comparison(df: pd.DataFrame, methods: list, metrics: list, title: str):
    """Plot grouped bar chart comparing methods across metrics."""
    n_methods = len(methods)
    n_metrics = len(metrics)
    x = np.arange(n_metrics)
    width = 0.8 / n_methods

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, method in enumerate(methods):
        row = df[df["method"] == method]
        if row.empty:
            continue
        values = []
        for m in metrics:
            col = f"{m}_norm"
            if col in row.columns:
                values.append(row[col].values[0])
            else:
                values.append(0)
        offset = (i - n_methods / 2 + 0.5) * width
        ax.bar(x + offset, values, width, label=method)

    ax.set_xticks(x)
    ax.set_xticklabels([METRIC_LABELS.get(m, m) for m in metrics])
    ax.set_ylabel("Score normalizado (mayor = mejor)")
    ax.set_title(title)
    ax.legend(fontsize=8)
    ax.set_ylim(0, 1.05)
    plt.tight_layout()
    return fig


def main():
    parser = argparse.ArgumentParser(description="Multi-metric plot generator")
    parser.add_argument(
        "--results-dir",
        default=DEFAULT_RESULTS_DIR,
        help="Directory with CSV results",
    )
    parser.add_argument("--output", default=None, help="Output PNG path")
    parser.add_argument(
        "--plot-type",
        choices=["radar", "bar"],
        default="radar",
        help="Type of plot",
    )
    args = parser.parse_args()

    df = load_results(args.results_dir)

    # Aggregate by method
    agg = {}
    for m in METRICS:
        if m in df.columns:
            agg[m] = "mean"
    summary = df.groupby("method").agg(agg).reset_index()

    # Normalize
    for m in METRICS:
        if m in summary.columns:
            summary[f"{m}_norm"] = normalize_metric(summary[m], m)

    methods = summary["method"].unique().tolist()
    available_metrics = [m for m in METRICS if m in summary.columns]

    if args.plot_type == "radar":
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
        plot_radar(summary, methods, available_metrics, "Comparación Multi-Métrica", ax)
    else:
        fig = plot_bar_comparison(
            summary, methods, available_metrics, "Comparación Multi-Métrica"
        )

    if args.output:
        fig.savefig(args.output, dpi=150, bbox_inches="tight")
        print(f"Saved to {args.output}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
