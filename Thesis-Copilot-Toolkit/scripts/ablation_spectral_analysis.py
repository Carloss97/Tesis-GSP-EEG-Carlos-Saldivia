#!/usr/bin/env python3
"""
Compute spectral metrics from experiment result files.

Outputs:
- results/ablation_spectral_results.csv (trial-level spectral metrics)
- results/ablation_spectral_summary.txt (pairwise stats: Mann-Whitney U, Cliff's delta)

Usage: python ablation_spectral_analysis.py --results-dir ../results
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
from ast import literal_eval
from pathlib import Path

import numpy as np
import pandas as pd

try:
    from scipy.stats import mannwhitneyu
except Exception:
    mannwhitneyu = None


def parse_signal_field(s: str):
    if pd.isna(s) or s == "":
        return None
    # try json
    try:
        obj = json.loads(s)
        return np.asarray(obj)
    except Exception:
        pass
    # try python literal
    try:
        obj = literal_eval(s)
        return np.asarray(obj)
    except Exception:
        # try comma-separated numbers
        try:
            vals = [float(x) for x in s.split(",") if x.strip()]
            return np.asarray(vals)
        except Exception:
            return None


def bandpower_from_psd(f, Pxx, band):
    fmin, fmax = band
    mask = (f >= fmin) & (f < fmax)
    if not np.any(mask):
        return 0.0
    return np.trapz(Pxx[mask], f[mask])


def spectral_metrics(signal: np.ndarray, fs: float, bands=None):
    if signal is None:
        return {}
    sig = np.asarray(signal)
    if sig.ndim == 2:
        # Heuristic: the longer axis is the temporal axis.
        # For EEG matrices stored as time x channels, this keeps the time resolution.
        if sig.shape[0] >= sig.shape[1]:
            channel_series = [sig[:, idx] for idx in range(sig.shape[1])]
        else:
            channel_series = [sig[idx, :] for idx in range(sig.shape[0])]
    else:
        channel_series = [sig]

    n = channel_series[0].shape[0]
    if fs is None:
        fs = 100.0

    psd_stack = []
    f = None
    for series in channel_series:
        freqs = np.fft.rfftfreq(series.shape[0], d=1.0 / fs)
        fft = np.fft.rfft(series - np.mean(series))
        Pxx_i = (np.abs(fft) ** 2) / series.shape[0]
        f_i = freqs
        if f is None:
            f = f_i
        elif len(f_i) != len(f) or not np.allclose(f_i, f):
            # Interpolate onto the first channel's frequency axis when needed.
            Pxx_i = np.interp(f, f_i, Pxx_i, left=0.0, right=0.0)
            f_i = f
        psd_stack.append(Pxx_i)

    Pxx = np.mean(np.vstack(psd_stack), axis=0)

    # define bands if not provided
    if bands is None:
        bands = {
            "delta": (1.0, 4.0),
            "theta": (4.0, 8.0),
            "alpha": (8.0, 13.0),
            "beta": (13.0, 30.0),
            "gamma": (30.0, min(45.0, fs / 2.0)),
        }

    band_pows = {f"bp_{k}": bandpower_from_psd(f, Pxx, v) for k, v in bands.items()}
    total_power = sum(band_pows.values()) if sum(band_pows.values()) > 0 else np.trapz(Pxx, f)
    rel = {f"r_bp_{k}": (v / total_power if total_power > 0 else 0.0) for k, v in band_pows.items()}

    # peak frequency in 1-45Hz
    mask = (f >= 1.0) & (f <= min(45.0, fs / 2.0))
    if np.any(mask):
        peak_idx = np.argmax(Pxx[mask])
        peak_freq = float(f[mask][peak_idx])
    else:
        peak_freq = float(np.nan)

    # spectral slope: linear fit to log-log PSD between 1 and 45 Hz
    slope = float(np.nan)
    try:
        mask2 = (f >= 1.0) & (f <= min(45.0, fs / 2.0)) & (Pxx > 0)
        if np.sum(mask2) >= 3:
            xf = np.log10(f[mask2])
            yf = np.log10(Pxx[mask2])
            A = np.vstack([xf, np.ones_like(xf)]).T
            m, c = np.linalg.lstsq(A, yf, rcond=None)[0]
            slope = float(m)
    except Exception:
        slope = float(np.nan)

    out = {
        "total_power": float(total_power),
        "peak_freq": peak_freq,
        "spectral_slope": slope,
    }
    out.update(band_pows)
    out.update(rel)
    return out


def cliffs_delta(x, y):
    # compute Cliff's delta (probability-based)
    x = np.asarray(x)
    y = np.asarray(y)
    nx = x.size
    ny = y.size
    if nx == 0 or ny == 0:
        return float(np.nan)
    greater = 0
    less = 0
    for xi in x:
        greater += np.sum(y < xi)
        less += np.sum(y > xi)
    delta = (greater - less) / (nx * ny)
    return float(delta)


def pairwise_stats(df, group_col, value_col, a_label, b_label):
    a = df[df[group_col] == a_label][value_col].dropna().values
    b = df[df[group_col] == b_label][value_col].dropna().values
    if mannwhitneyu is None:
        p = float(np.nan)
    else:
        try:
            stat, p = mannwhitneyu(a, b, alternative="two-sided")
        except Exception:
            p = float(np.nan)
    delta = cliffs_delta(a, b)
    return p, delta


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--results-dir", default=Path(__file__).resolve().parents[1] / "results")
    p.add_argument("--out-csv", default=None)
    p.add_argument("--out-summary", default=None)
    p.add_argument("--fs", type=float, default=None, help="Sampling frequency (Hz). If not given, try to infer or default 100Hz.")
    args = p.parse_args()
    results_dir = Path(args.results_dir)
    out_csv = Path(args.out_csv) if args.out_csv else results_dir / "ablation_spectral_results.csv"
    out_summary = Path(args.out_summary) if args.out_summary else results_dir / "ablation_spectral_summary.txt"

    rows = []
    # search for per-iteration raw files only; the consolidated table does not
    # carry reconstructed signals and slows the scan considerably.
    patterns = [str(results_dir / "itX*_raw.csv")]
    files = []
    for pat in patterns:
        files.extend(sorted(glob.glob(pat)))

    for fp in files:
        try:
            df = pd.read_csv(fp, low_memory=False)
        except Exception:
            continue
        if df.empty:
            continue
        for _, r in df.iterrows():
            base = r.to_dict()
            sig = None
            if "reconstructed_signal" in df.columns:
                sig = parse_signal_field(r.get("reconstructed_signal", ""))
            # sampling rate fallback: try reading run metadata next to file
            fs = args.fs
            # try to infer fs from nearby run metadata
            run_meta = None
            run_meta_path = Path(fp).with_name(Path(fp).stem + "_run_metadata.json")
            if run_meta_path.exists():
                try:
                    with open(run_meta_path, "r", encoding="utf8") as fh:
                        jm = json.load(fh)
                        # look for hints
                        # preferred: explicit 'sampling_rate' key
                        if isinstance(jm, dict) and "sampling_rate" in jm:
                            fs = float(jm["sampling_rate"])
                except Exception:
                    pass

            if fs is None:
                # try dataset-based heuristic
                ds = str(r.get("dataset", ""))
                if "100hz" in ds.lower() or "100hz" in fp.lower():
                    fs = 100.0
                elif "250" in ds or "bci_iv2a" in ds.lower():
                    fs = 250.0
                elif "mne_sample" in ds or "600" in ds:
                    fs = 600.0
                else:
                    fs = 100.0

            metrics = {}
            if sig is not None and sig.size > 0:
                metrics = spectral_metrics(sig, fs)
            else:
                # if no signal, try to take existing spectral fields
                for k in ("snr", "coherence_mean", "lsd"):
                    if k in df.columns:
                        try:
                            metrics[k] = float(r.get(k))
                        except Exception:
                            metrics[k] = float(np.nan)

            # combine
            out = {**{k: base.get(k) for k in ("dataset", "method", "missing_ratio", "seed", "mae", "rmse")}, **metrics}
            rows.append(out)

    if not rows:
        print("No spectral data found or no reconstructed signals present. Exiting.")
        return

    out_df = pd.DataFrame(rows)
    out_df.to_csv(out_csv, index=False)
    print(f"Wrote trial-level spectral CSV to: {out_csv}")

    summary_lines = []
    metrics_to_summarize = [
        "mae",
        "rmse",
        "total_power",
        "peak_freq",
        "spectral_slope",
        "bp_delta",
        "bp_theta",
        "bp_alpha",
        "bp_beta",
        "bp_gamma",
        "coherence_mean",
        "snr",
    ]
    summary_lines.append("Per-method spectral means (all scanned raw files):")
    summary_lines.append("")
    for (ds, method), grp in out_df.groupby(["dataset", "method"], dropna=False):
        parts = [f"{ds} | {method} | n={len(grp)}"]
        for m in metrics_to_summarize:
            if m in grp.columns:
                val = grp[m].astype(float).mean(skipna=True)
                if not math.isnan(val):
                    parts.append(f"{m}={val:.6g}")
        summary_lines.append("; ".join(parts))

    available = set(out_df["method"].dropna().astype(str).unique())
    if {"TRSS-Full", "TRSS-NoTemporal"}.issubset(available):
        summary_lines.append("")
        summary_lines.append("Pairwise comparison TRSS-Full vs TRSS-NoTemporal:")
        for m in metrics_to_summarize:
            if m not in out_df.columns:
                continue
            try:
                pval, delta = pairwise_stats(out_df, "method", m, "TRSS-Full", "TRSS-NoTemporal")
                summary_lines.append(f"{m}: p={pval:.6g}, Cliff's delta={delta:.6g}")
            except Exception as e:
                summary_lines.append(f"{m}: error={e}")
    else:
        summary_lines.append("")
        summary_lines.append("Pairwise comparison TRSS-Full vs TRSS-NoTemporal: not available in the scanned raw files.")
        summary_lines.append("The raw files contained methods such as linear, ica, spherical_spline, rbfi_tps, idw, tikhonov, bgsrp, and sobolev.")

    with open(out_summary, "w", encoding="utf8") as fh:
        fh.write("ABlation Spectral Summary\n")
        fh.write("========================\n\n")
        for ln in summary_lines:
            fh.write(ln + "\n")

    print(f"Wrote summary to: {out_summary}")


if __name__ == "__main__":
    main()
