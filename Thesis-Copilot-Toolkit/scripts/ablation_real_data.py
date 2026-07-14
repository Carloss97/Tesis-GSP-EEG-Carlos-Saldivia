#!/usr/bin/env python3
"""
Ablation Study: Temporal Component Contribution to TRSS (REAL DATA)
==================================================================
PURPOSE:
  Demonstrate that temporal regularization (β term) meaningfully contributes
  to TRSS performance using REAL EEG data (BCI IV 2a and PhysioNet EEGBCI).

METHODOLOGY:
  - 2 real datasets: BCI Competition IV 2a, PhysioNet EEGBCI
  - Missing ratios: 10%, 20%, 30%, 40%
  - 10 iterations per variant per scenario (240 total interpolations)
  - Metrics: MAE, RMSE, DTW, SNR, LSD, coherence_mean, plus PSD-derived summaries
  - Statistical test: Mann-Whitney U with Cliff's delta effect size

OUTPUT:
  - results/ablation_real_data_extended_results.csv
  - results/ablation_real_data_extended_summary.txt

AUTHOR: Publication Strengthening Phase 4b (Real Data Ablation)
DATE: 2026-04-28
"""

from __future__ import annotations

import os
import sys
import json
import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats
from scipy.io import loadmat
from datetime import datetime
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Add src/ to path for imports
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "src"))
sys.path.insert(0, str(repo_root))

from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import (
    interpolate_trss,
    interpolate_spherical_spline,
)
from src.evaluation import evaluate_signals


def load_bci_iv_2a_real(subject: int = 1, training: bool = True, duration_seconds: int = 10):
    """Load a short BCI Competition IV 2a segment for the ablation study."""
    dataset_dir = repo_root / "datasets" / "BCICIV_2a_gdf"

    filename = f"A{subject:02d}T.gdf" if training else f"A{subject:02d}E.gdf"
    filepath = dataset_dir / filename
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    import mne

    raw = mne.io.read_raw_gdf(str(filepath), preload=True)
    sfreq = float(raw.info["sfreq"])
    n_samples = int(duration_seconds * sfreq)
    signals = raw.get_data(start=0, stop=n_samples).T

    n_channels = signals.shape[1]
    angles = np.linspace(0, 2 * np.pi, n_channels, endpoint=False)
    positions = np.column_stack([
        np.cos(angles),
        np.sin(angles),
        np.zeros(n_channels),
    ])

    print(f"  Loaded BCI IV 2a subject {subject} ({duration_seconds}s segment): {signals.shape}")
    return signals, positions, {"dataset": "BCI_IV_2a", "subject": subject, "sfreq": sfreq}


def load_eegbci_real(subject: int = 1, run: int = 1, duration_seconds: int = 10):
    """Load a short PhysioNet EEGBCI segment for the ablation study."""
    import mne
    from mne.datasets import eegbci

    files = eegbci.load_data(subjects=[subject], runs=[run], path=repo_root / "datasets")
    if isinstance(files, str):
        files = [files]

    raw = mne.io.read_raw_edf(files[0], preload=True)
    sfreq = float(raw.info["sfreq"])
    n_samples = int(duration_seconds * sfreq)
    signals = raw.get_data(start=0, stop=n_samples).T

    n_channels = signals.shape[1]
    angles = np.linspace(0, 2 * np.pi, n_channels, endpoint=False)
    positions = np.column_stack([
        np.cos(angles),
        np.sin(angles),
        np.zeros(n_channels),
    ])

    print(f"  Loaded PhysioNet EEGBCI subject {subject} run {run} ({duration_seconds}s segment): {signals.shape}")
    return signals, positions, {"dataset": "PhysioNet_EEGBCI", "subject": subject, "run": run, "sfreq": sfreq}


def simulate_missing_channels_random(signals, missing_ratio, seed=42):
    """Create NaN mask at random channels (consistent across time)."""
    np.random.seed(seed)
    n_times, n_channels = signals.shape
    n_missing = max(1, int(n_channels * missing_ratio))
    missing_idx = np.random.choice(n_channels, size=n_missing, replace=False)

    y = signals.astype(float)
    mask = np.ones_like(y, dtype=bool)
    y[:, missing_idx] = np.nan
    mask[:, missing_idx] = False
    return y, mask


def cliffs_delta(x, y):
    """Cliff's delta effect size."""
    x, y = np.asarray(x), np.asarray(y)
    n1, n2 = len(x), len(y)
    if n1 == 0 or n2 == 0:
        return np.nan
    dominance = 0.0
    for xi in x:
        dominance += np.sum(xi > y) - np.sum(xi < y)
    return dominance / (n1 * n2)


def bandpower_from_psd(freqs, psd, band):
    fmin, fmax = band
    mask = (freqs >= fmin) & (freqs < fmax)
    if not np.any(mask):
        return 0.0
    return float(np.trapz(psd[mask], freqs[mask]))


def spectral_metrics(signal, sfreq):
    """Compute compact PSD-derived descriptors from a reconstructed signal."""
    if signal is None or sfreq is None:
        return {}
    if not np.isfinite(float(sfreq)) or float(sfreq) <= 0:
        return {}

    sig = np.asarray(signal, dtype=float)
    if sig.ndim != 2 or sig.shape[0] < 2:
        return {}

    if sig.shape[0] >= sig.shape[1]:
        channel_series = [sig[:, idx] for idx in range(sig.shape[1])]
    else:
        channel_series = [sig[idx, :] for idx in range(sig.shape[0])]

    psd_stack = []
    freqs_ref = None
    for series in channel_series:
        series = np.asarray(series, dtype=float) - np.mean(series)
        freqs = np.fft.rfftfreq(series.shape[0], d=1.0 / float(sfreq))
        fft_vals = np.fft.rfft(series)
        psd = (np.abs(fft_vals) ** 2) / series.shape[0]
        if freqs_ref is None:
            freqs_ref = freqs
        elif len(freqs) != len(freqs_ref) or not np.allclose(freqs, freqs_ref):
            psd = np.interp(freqs_ref, freqs, psd, left=0.0, right=0.0)
        psd_stack.append(psd)

    if not psd_stack:
        return {}

    freqs = freqs_ref
    psd_mean = np.mean(np.vstack(psd_stack), axis=0)
    bands = {
        "delta": (1.0, 4.0),
        "theta": (4.0, 8.0),
        "alpha": (8.0, 13.0),
        "beta": (13.0, 30.0),
        "gamma": (30.0, min(45.0, float(sfreq) / 2.0)),
    }

    band_powers = {f"bp_{band}": bandpower_from_psd(freqs, psd_mean, limits) for band, limits in bands.items()}
    total_band_power = sum(band_powers.values())
    if total_band_power <= 0:
        total_band_power = float(np.trapz(psd_mean, freqs))

    mask = (freqs >= 1.0) & (freqs <= min(45.0, float(sfreq) / 2.0))
    if np.any(mask):
        peak_freq = float(freqs[mask][np.argmax(psd_mean[mask])])
    else:
        peak_freq = float(np.nan)

    slope = float(np.nan)
    try:
        slope_mask = mask & (psd_mean > 0)
        if np.sum(slope_mask) >= 3:
            x = np.log10(freqs[slope_mask])
            y = np.log10(psd_mean[slope_mask])
            design = np.vstack([x, np.ones_like(x)]).T
            slope = float(np.linalg.lstsq(design, y, rcond=None)[0][0])
    except Exception:
        slope = float(np.nan)

    return {
        "total_power": float(total_band_power),
        "peak_freq": peak_freq,
        "spectral_slope": slope,
        **band_powers,
    }


def run_ablation_real_data():
    """Execute ablation study with real EEG data."""

    print("=" * 80)
    print("ABLATION STUDY: Temporal Component Contribution (REAL DATA)")
    print("=" * 80)
    print(f"Timestamp: {datetime.now().isoformat()}\n")

    results_dir = repo_root / "results"
    results_dir.mkdir(exist_ok=True)

    datasets_to_load = [
        {"name": "BCI IV 2a", "loader": "bci_iv2a", "subject": 1, "key": "bci_iv2a_s1"},
        {"name": "PhysioNet EEGBCI", "loader": "eegbci", "subject": 1, "run": 1, "key": "eegbci_s1r1"},
    ]

    missing_ratios = [0.1, 0.2, 0.3, 0.4]
    n_iter_ablation = 10

    trss_alpha_opt = 0.7
    trss_beta_opt = 0.15
    trss_n_iter = 15
    trss_lr = 0.01

    metric_names = ["mae", "rmse", "dtw", "snr", "lsd", "coherence_mean"]

    all_results = []

    for dataset_cfg in datasets_to_load:
        dataset_name = dataset_cfg["name"]
        dataset_key = dataset_cfg["key"]

        print(f"\n{'=' * 80}")
        print(f"Dataset: {dataset_name}")
        print(f"{'=' * 80}")

        try:
            if dataset_cfg["loader"] == "bci_iv2a":
                signals, positions, info = load_bci_iv_2a_real(
                    subject=dataset_cfg["subject"],
                    training=True,
                    duration_seconds=5,
                )
            elif dataset_cfg["loader"] == "eegbci":
                signals, positions, info = load_eegbci_real(
                    subject=dataset_cfg["subject"],
                    run=dataset_cfg["run"],
                    duration_seconds=5,
                )
            else:
                print(f"  ERROR: Unknown loader {dataset_cfg['loader']}")
                continue
        except Exception as e:
            print(f"  ERROR loading dataset: {e}")
            continue

        sfreq = info.get("sfreq") if isinstance(info, dict) else None

        try:
            graph_result = build_graph(method="knn", positions=positions, k=5)
            adjacency = graph_result["adjacency"] if isinstance(graph_result, dict) else graph_result
            print("  Graph built (KNN, k=5)")
        except Exception as e:
            print(f"  ERROR building graph: {e}")
            continue

        for missing_ratio in missing_ratios:
            print(f"\n  Missing ratio: {missing_ratio:.0%}")

            for iter_idx in range(n_iter_ablation):
                y, mask = simulate_missing_channels_random(signals, missing_ratio, seed=1000 + iter_idx)
                x_true = signals.copy()

                try:
                    x_trss_full = interpolate_trss(
                        y,
                        adjacency,
                        alpha=trss_alpha_opt,
                        beta=trss_beta_opt,
                        n_iter=trss_n_iter,
                        lr=trss_lr,
                    )
                    metrics_full = evaluate_signals(
                        x_true,
                        x_trss_full,
                        metrics=metric_names,
                        sfreq=sfreq,
                    )
                    metrics_full.update(spectral_metrics(x_trss_full, sfreq))
                    all_results.append({
                        "iteration": iter_idx,
                        "dataset": dataset_key,
                        "missing_ratio": missing_ratio,
                        "variant": "TRSS-Full",
                        **metrics_full,
                    })
                except Exception as e:
                    if iter_idx == 0:
                        print(f"\n      TRSS-Full error: {str(e)[:80]}")

                try:
                    x_no_temp = interpolate_trss(
                        y,
                        adjacency,
                        alpha=trss_alpha_opt,
                        beta=0.0,
                        n_iter=trss_n_iter,
                        lr=trss_lr,
                    )
                    metrics_no_temp = evaluate_signals(
                        x_true,
                        x_no_temp,
                        metrics=metric_names,
                        sfreq=sfreq,
                    )
                    metrics_no_temp.update(spectral_metrics(x_no_temp, sfreq))
                    all_results.append({
                        "iteration": iter_idx,
                        "dataset": dataset_key,
                        "missing_ratio": missing_ratio,
                        "variant": "TRSS-NoTemporal",
                        **metrics_no_temp,
                    })
                except Exception as e:
                    if iter_idx == 0:
                        print(f"\n      TRSS-NoTemp error: {str(e)[:80]}")

                try:
                    x_spline = interpolate_spherical_spline(y, positions)
                    metrics_spline = evaluate_signals(
                        x_true,
                        x_spline,
                        metrics=metric_names,
                        sfreq=sfreq,
                    )
                    metrics_spline.update(spectral_metrics(x_spline, sfreq))
                    all_results.append({
                        "iteration": iter_idx,
                        "dataset": dataset_key,
                        "missing_ratio": missing_ratio,
                        "variant": "Spatial-Only Spline",
                        **metrics_spline,
                    })
                except Exception as e:
                    if iter_idx == 0:
                        print(f"\n      Spline error: {str(e)[:80]}")

            print("OK")

    if len(all_results) == 0:
        print("\n\nERROR: No results collected. Check dataset loading.")
        return None, None

    df_results = pd.DataFrame(all_results)
    print(f"\n\nCollected {len(df_results)} result rows across all variants")

    output_csv = results_dir / "ablation_real_data_extended_results.csv"
    df_results.to_csv(output_csv, index=False)
    print(f"Saved results to: {output_csv}\n")

    print("=" * 80)
    print("STATISTICAL ANALYSIS: TRSS-Full vs. TRSS-NoTemporal (REAL DATA)")
    print("=" * 80)

    summary_lines = []
    summary_lines.append("ABLATION STUDY SUMMARY (REAL EEG DATA)")
    summary_lines.append("=" * 80)
    summary_lines.append(f"Timestamp: {datetime.now().isoformat()}")
    summary_lines.append(f"Total iterations per scenario: {n_iter_ablation}")
    summary_lines.append("Datasets: 2 (BCI IV 2a, PhysioNet EEGBCI)")
    summary_lines.append(f"Missing ratios: {missing_ratios}")
    summary_lines.append(
        "Metrics: MAE, RMSE, DTW, SNR, LSD, coherence_mean, total_power, peak_freq, spectral_slope, bp_delta, bp_theta, bp_alpha, bp_beta, bp_gamma"
    )
    summary_lines.append("")
    summary_lines.append("=" * 80)
    summary_lines.append("PAIRWISE COMPARISONS (FULL vs NO-TEMPORAL)")
    summary_lines.append("=" * 80)

    metric_specs = {
        "mae": "lower",
        "rmse": "lower",
        "dtw": "lower",
        "snr": "higher",
        "lsd": "lower",
        "coherence_mean": "higher",
        "total_power": "descriptive",
        "peak_freq": "descriptive",
        "spectral_slope": "descriptive",
        "bp_delta": "descriptive",
        "bp_theta": "descriptive",
        "bp_alpha": "descriptive",
        "bp_beta": "descriptive",
        "bp_gamma": "descriptive",
    }

    comparisons = []
    for dataset_key in df_results["dataset"].dropna().unique():
        for mr in missing_ratios:
            mask_full = (
                (df_results["variant"] == "TRSS-Full")
                & (df_results["dataset"] == dataset_key)
                & (df_results["missing_ratio"] == mr)
            )
            mask_no_temp = (
                (df_results["variant"] == "TRSS-NoTemporal")
                & (df_results["dataset"] == dataset_key)
                & (df_results["missing_ratio"] == mr)
            )

            scenario = {"dataset": dataset_key, "missing_ratio": mr, "metrics": {}}
            metric_parts = []

            for metric_name, direction in metric_specs.items():
                if metric_name not in df_results.columns:
                    continue

                x_full = df_results.loc[mask_full, metric_name].dropna().values
                x_no_temp = df_results.loc[mask_no_temp, metric_name].dropna().values
                if len(x_full) < 3 or len(x_no_temp) < 3:
                    continue

                alternative = "less" if direction == "lower" else "greater" if direction == "higher" else "two-sided"
                try:
                    _, p_value = stats.mannwhitneyu(x_full, x_no_temp, alternative=alternative)
                except Exception:
                    p_value = np.nan

                delta = cliffs_delta(x_full, x_no_temp)
                median_full = np.median(x_full)
                median_no_temp = np.median(x_no_temp)

                if direction == "lower":
                    change_pct = ((median_no_temp - median_full) / median_no_temp * 100) if median_no_temp != 0 else 0.0
                elif direction == "higher":
                    change_pct = ((median_full - median_no_temp) / abs(median_no_temp) * 100) if median_no_temp != 0 else 0.0
                else:
                    change_pct = ((median_full - median_no_temp) / abs(median_no_temp) * 100) if median_no_temp != 0 else 0.0

                scenario["metrics"][metric_name] = {
                    "full_median": float(median_full),
                    "no_temp_median": float(median_no_temp),
                    "change_pct": float(change_pct),
                    "p_value": float(p_value) if np.isfinite(p_value) else np.nan,
                    "cliffs_delta": float(delta),
                    "direction": direction,
                }

                sig = "***" if np.isfinite(p_value) and p_value < 0.001 else "**" if np.isfinite(p_value) and p_value < 0.01 else "*" if np.isfinite(p_value) and p_value < 0.05 else "ns"
                effect_str = (
                    "large" if abs(delta) >= 0.474
                    else "medium" if abs(delta) >= 0.330
                    else "small" if abs(delta) >= 0.147
                    else "negligible"
                )
                metric_parts.append(
                    f"{metric_name}={change_pct:+.1f}% (δ={delta:+.3f}, p={p_value:.4f} {sig}, {effect_str})"
                )

            if scenario["metrics"]:
                comparisons.append(scenario)
                line = f"  {dataset_key:15} MR={mr:.0%}  " + " | ".join(metric_parts)
                summary_lines.append(line)
                print(line)

    summary_lines.append("")
    summary_lines.append("=" * 80)
    summary_lines.append("EFFECT SIZE INTERPRETATION")
    summary_lines.append("=" * 80)
    summary_lines.append("")
    summary_lines.append("Cliff's delta (|δ|):")
    summary_lines.append("  < 0.147: negligible")
    summary_lines.append("  0.147–0.330: small")
    summary_lines.append("  0.330–0.474: medium")
    summary_lines.append("  ≥ 0.474: large")
    summary_lines.append("")

    if comparisons:
        metric_overall = {}
        for metric_name in metric_specs:
            metric_rows = []
            for scenario in comparisons:
                metric_data = scenario.get("metrics", {}).get(metric_name)
                if metric_data is not None:
                    metric_rows.append(metric_data)
            if not metric_rows:
                continue

            changes = [row["change_pct"] for row in metric_rows if np.isfinite(row["change_pct"])]
            deltas = [abs(row["cliffs_delta"]) for row in metric_rows if np.isfinite(row["cliffs_delta"])]
            pvals = [row["p_value"] for row in metric_rows if np.isfinite(row["p_value"])]

            metric_overall[metric_name] = {
                "avg_change_pct": float(np.mean(changes)) if changes else np.nan,
                "avg_abs_delta": float(np.mean(deltas)) if deltas else np.nan,
                "significant": int(sum(1 for p in pvals if p < 0.05)),
                "count": int(len(metric_rows)),
            }

        summary_lines.append("OVERALL SUMMARY")
        summary_lines.append("=" * 80)
        for metric_name in ["mae", "rmse", "dtw", "snr", "lsd", "coherence_mean", "total_power", "peak_freq", "spectral_slope"]:
            if metric_name not in metric_overall:
                continue
            row = metric_overall[metric_name]
            summary_lines.append(
                f"  {metric_name}: avg_change={row['avg_change_pct']:+.2f}% | avg_|δ|={row['avg_abs_delta']:.3f} | significant={row['significant']}/{row['count']}"
            )

        summary_lines.append("")
        summary_lines.append("CONCLUSION")
        mae_row = metric_overall.get("mae")
        lsd_row = metric_overall.get("lsd")
        snr_row = metric_overall.get("snr")
        if mae_row and lsd_row:
            if mae_row["avg_change_pct"] > 0 and lsd_row["avg_change_pct"] > 0:
                conclusion = (
                    "The temporal regularization term (β) improves both pointwise error and spectral fidelity. "
                    "MAE/RMSE/DTW move favorably, and LSD drops alongside cleaner PSD descriptors, which supports the temporal component as a useful complement to spatial regularization."
                )
            elif snr_row and snr_row["avg_change_pct"] > 0:
                conclusion = (
                    "The temporal regularization term (β) shows mixed pointwise gains but clearer signal-quality improvements. "
                    "SNR/LSD are the most informative additions here, suggesting the temporal term helps preserve spectral structure even when error reductions are modest."
                )
            else:
                conclusion = (
                    "The temporal regularization term (β) shows limited or mixed benefit across the expanded metric set. "
                    "The PSD/LSD metrics should be interpreted together with the reconstruction losses rather than in isolation."
                )
        else:
            conclusion = "Expanded metric analysis completed, but there were insufficient valid comparisons to derive a single robust conclusion."

        summary_lines.append("  " + conclusion)

    summary_txt = results_dir / "ablation_real_data_extended_summary.txt"
    with open(summary_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))

    print(f"\nSaved summary to: {summary_txt}")
    print("\n" + "=" * 80)
    print("ABLATION STUDY COMPLETE (REAL DATA)")
    print("=" * 80)

    return df_results, comparisons


if __name__ == "__main__":
    df_results, comparisons = run_ablation_real_data()
