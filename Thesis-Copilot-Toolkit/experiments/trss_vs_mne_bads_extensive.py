#!/usr/bin/env python3
"""
Extensive, checkpointed TRSS vs MNE interpolate_bads() benchmark.

Goal
----
Compare GraphTRSS against the de-facto MNE EEG bad-channel interpolation
(`Raw.interpolate_bads(..., method='spline')`) under realistic missing-channel
scenarios. The script evaluates:
  * reconstruction metrics on held-out bad channels only;
  * random, clustered/nearby, peripheral-edge, and high-variance missing cases;
  * single/few-channel failures and high-loss regimes;
  * default TRSS, tuned TRSS, and oracle-grid TRSS upper bound;
  * runtime and failure/warning behavior.

Outputs are written incrementally to results/trss_vs_mne_bads_extensive/ so the
run can be resumed safely if interrupted.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import traceback
import warnings
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Tuple

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Make PhysioNet local path explicit. The loader's default resolves outside this
# repo when called from WSL, so set it here unless the user overrides it.
os.environ.setdefault(
    "EEGBCI_LOCAL_PATH",
    str(ROOT.parent / "datasets" / "MNE-eegbci-data"),
)
os.environ.setdefault("B2_DTW_MAX_POINTS", "80")

from src.data.data_loader import load_physionet_eegmmidb, load_mne_sample_dataset
from src.evaluation.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals


METRICS = ["mae", "rmse", "dtw", "snr", "lsd", "coherence_mean"]
LOWER_BETTER = {"mae", "rmse", "nrmse", "dtw", "lsd", "abs_bias", "runtime_s"}
HIGHER_BETTER = {"snr", "coherence_mean", "corr_mean", "r2"}


@dataclass(frozen=True)
class TRSSConfig:
    label: str
    k: int
    sigma: float
    alpha: float
    beta: float
    n_iter: int = 80
    lr: float = 0.05

    def params_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True)


# Candidate grid intentionally small but covers regimes observed in prior Optuna
# artifacts: low alpha / moderate beta, default-ish regularization, and the older
# high-alpha/low-beta profile. This supports both practical tuning and oracle
# upper-bound analysis without exploding runtime.
TRSS_CANDIDATES: List[TRSSConfig] = [
    TRSSConfig("trss_default", k=4, sigma=1.0, alpha=0.8, beta=0.15, n_iter=120, lr=0.05),
    TRSSConfig("trss_prior_global", k=4, sigma=1.0, alpha=0.03, beta=0.50, n_iter=80, lr=0.05),
    TRSSConfig("trss_lowalpha_lowbeta", k=4, sigma=1.0, alpha=0.03, beta=0.10, n_iter=80, lr=0.05),
    TRSSConfig("trss_lowalpha_highbeta_k3", k=3, sigma=0.30, alpha=0.02, beta=0.70, n_iter=80, lr=0.05),
    TRSSConfig("trss_lowalpha_highbeta_k8", k=8, sigma=0.30, alpha=0.015, beta=0.70, n_iter=80, lr=0.05),
    TRSSConfig("trss_midalpha_midbeta", k=6, sigma=1.0, alpha=0.10, beta=0.30, n_iter=80, lr=0.05),
    TRSSConfig("trss_spatial_dominant", k=8, sigma=2.0, alpha=0.10, beta=0.02, n_iter=80, lr=0.05),
    TRSSConfig("trss_legacy_profile", k=4, sigma=1.0, alpha=4.77, beta=0.0094, n_iter=80, lr=0.05),
]
DEFAULT_TRSS_LABEL = "trss_default"


@dataclass
class DatasetSpec:
    name: str
    loader: Callable[[], Dict[str, Any]]
    n_times: int
    start: int = 0
    max_channels: int | None = None


def sphere_positions(n: int, radius: float = 1.0) -> np.ndarray:
    golden = np.pi * (3.0 - np.sqrt(5.0))
    indices = np.arange(n)
    y = 1.0 - (indices / max(n - 1, 1)) * 2.0
    r_xy = np.sqrt(np.maximum(0.0, 1.0 - y**2))
    theta = golden * indices
    x = np.cos(theta) * r_xy
    z = np.sin(theta) * r_xy
    return np.stack([x * radius, y * radius, z * radius], axis=1)


def make_synthetic_spatiotemporal(
    name: str,
    n_channels: int = 32,
    n_times: int = 640,
    sfreq: float = 160.0,
    seed: int = 123,
    rough: bool = False,
) -> Dict[str, Any]:
    """Generate synthetic EEG-like data with known ground truth.

    smooth=False/rough=False produces spatially and temporally smooth signals,
    favorable to graph/temporal methods. rough=True deliberately violates TRSS's
    smoothness prior to test failure modes.
    """
    rng = np.random.default_rng(seed)
    pos = sphere_positions(n_channels)
    t = np.arange(n_times) / sfreq

    # Smooth spatial factors from low-order coordinate functions.
    factors = np.column_stack([
        np.ones(n_channels),
        pos[:, 0], pos[:, 1], pos[:, 2],
        pos[:, 0] * pos[:, 1], pos[:, 1] * pos[:, 2], pos[:, 0] ** 2 - pos[:, 1] ** 2,
    ])
    temporal = np.vstack([
        18e-6 * np.sin(2 * np.pi * 10.0 * t),
        10e-6 * np.sin(2 * np.pi * 6.0 * t + 0.4),
        8e-6 * np.sin(2 * np.pi * 18.0 * t + 0.8),
        5e-6 * np.sin(2 * np.pi * 26.0 * t + 1.2),
        4e-6 * np.sin(2 * np.pi * 3.0 * t + 0.5),
        3e-6 * np.sin(2 * np.pi * 35.0 * t + 0.9),
        2e-6 * np.sin(2 * np.pi * 12.0 * t + 1.7),
    ])
    signals = temporal.T @ factors.T
    signals += 1.5e-6 * rng.normal(size=signals.shape)

    if rough:
        # Add channel-local oscillations and transients: this intentionally weakens
        # graph/temporal smoothness assumptions.
        freqs = rng.uniform(4.0, 42.0, n_channels)
        phases = rng.uniform(0, 2 * np.pi, n_channels)
        local = 8e-6 * np.sin(2 * np.pi * t[:, None] * freqs[None, :] + phases[None, :])
        transient = np.zeros_like(signals)
        for _ in range(max(3, n_channels // 4)):
            ch = rng.integers(0, n_channels)
            center = rng.integers(n_times // 8, 7 * n_times // 8)
            width = rng.uniform(8, 35)
            amp = rng.choice([-1, 1]) * rng.uniform(8e-6, 18e-6)
            transient[:, ch] += amp * np.exp(-0.5 * ((np.arange(n_times) - center) / width) ** 2)
        signals = 0.45 * signals + local + transient + 2e-6 * rng.normal(size=signals.shape)

    ch_names = [f"SYN{i:02d}" for i in range(n_channels)]
    return {
        "signals": signals.astype(float),
        "positions": pos.astype(float),
        "info": {"sfreq": sfreq, "ch_names": ch_names, "n_channels": n_channels, "dataset": name},
    }


def load_dataset(spec: DatasetSpec) -> Dict[str, Any]:
    d = spec.loader()
    signals = np.asarray(d["signals"], dtype=float)
    positions = np.asarray(d["positions"], dtype=float)
    info = dict(d.get("info", {}))
    ch_names = list(info.get("ch_names", [f"CH{i:03d}" for i in range(signals.shape[1])]))

    if positions.shape[0] != signals.shape[1]:
        n = min(positions.shape[0], signals.shape[1])
        positions = positions[:n]
        signals = signals[:, :n]
        ch_names = ch_names[:n]

    if spec.max_channels is not None and signals.shape[1] > spec.max_channels:
        # Deterministic subset spread across the montage; useful for MNE sample to
        # keep runtime bounded while avoiding an arbitrary frontal-only subset.
        idx = np.linspace(0, signals.shape[1] - 1, spec.max_channels, dtype=int)
        signals = signals[:, idx]
        positions = positions[idx]
        ch_names = [ch_names[i] for i in idx]

    start = min(max(0, spec.start), max(0, signals.shape[0] - 1))
    end = min(signals.shape[0], start + spec.n_times)
    if end - start < min(spec.n_times, 128):
        start = 0
        end = min(signals.shape[0], spec.n_times)
    signals = signals[start:end].copy()

    # Remove channels with non-finite or exactly zero positions if possible.
    good_pos = np.isfinite(positions).all(axis=1)
    if np.sum(good_pos) >= 8:
        positions = positions[good_pos]
        signals = signals[:, good_pos]
        ch_names = [c for c, g in zip(ch_names, good_pos) if g]

    info["sfreq"] = float(info.get("sfreq", 160.0))
    info["ch_names"] = ch_names
    info["n_channels"] = int(signals.shape[1])
    info["window_start"] = int(start)
    info["window_n_times"] = int(signals.shape[0])
    info["dataset_spec"] = spec.name
    return {"signals": signals, "positions": positions, "info": info}


def dataset_specs(profile: str) -> List[DatasetSpec]:
    base = [
        DatasetSpec(
            "synthetic_smooth",
            lambda: make_synthetic_spatiotemporal("synthetic_smooth", rough=False),
            n_times=640,
        ),
        DatasetSpec(
            "synthetic_rough",
            lambda: make_synthetic_spatiotemporal("synthetic_rough", rough=True),
            n_times=640,
        ),
        DatasetSpec(
            "physionet_s1_r4_w0",
            lambda: load_physionet_eegmmidb(subject=1, run=4),
            n_times=640,
            start=0,
        ),
        DatasetSpec(
            "physionet_s2_r4_w0",
            lambda: load_physionet_eegmmidb(subject=2, run=4),
            n_times=640,
            start=0,
        ),
        DatasetSpec(
            "mne_sample_w0",
            load_mne_sample_dataset,
            n_times=900,
            start=0,
            max_channels=40,
        ),
    ]
    if profile == "quick":
        return base[:3]
    if profile == "balanced":
        return base
    # full adds held-out windows/subjects.
    return base + [
        DatasetSpec(
            "physionet_s3_r4_w0",
            lambda: load_physionet_eegmmidb(subject=3, run=4),
            n_times=640,
            start=0,
        ),
        DatasetSpec(
            "physionet_s1_r4_w4096",
            lambda: load_physionet_eegmmidb(subject=1, run=4),
            n_times=640,
            start=4096,
        ),
        DatasetSpec(
            "mne_sample_w12000",
            load_mne_sample_dataset,
            n_times=900,
            start=12000,
            max_channels=40,
        ),
    ]


def missing_values(profile: str) -> List[float | int]:
    if profile == "quick":
        return [1, 0.3]
    if profile == "balanced":
        return [1, 2, 0.1, 0.3, 0.4]
    return [1, 2, 3, 0.1, 0.2, 0.3, 0.4]


def missing_modes(profile: str) -> List[str]:
    if profile == "quick":
        return ["random", "nearby"]
    return ["random", "nearby", "edge", "high_variance"]


def seeds(profile: str) -> List[int]:
    if profile == "quick":
        return [0, 1]
    if profile == "balanced":
        return [0, 1, 2]
    return [0, 1, 2, 3, 4]


def n_missing_from_value(n_channels: int, value: float | int) -> int:
    v = float(value)
    if v < 1.0:
        n = int(round(n_channels * v))
    else:
        n = int(round(v))
    return int(np.clip(max(1, n), 1, max(1, n_channels - 4)))


def pairwise_dists(positions: np.ndarray) -> np.ndarray:
    p = np.asarray(positions, dtype=float)
    diff = p[:, None, :] - p[None, :, :]
    return np.sqrt(np.sum(diff**2, axis=-1))


def make_bad_indices(
    signals: np.ndarray,
    positions: np.ndarray,
    missing_value: float | int,
    mode: str,
    seed: int,
) -> np.ndarray:
    n_channels = signals.shape[1]
    n_missing = n_missing_from_value(n_channels, missing_value)
    rng = np.random.default_rng(seed)
    dists = pairwise_dists(positions)

    if mode == "random":
        idx = rng.choice(n_channels, size=n_missing, replace=False)
    elif mode == "nearby":
        center = int(rng.integers(0, n_channels))
        idx = np.argsort(dists[center])[:n_missing]
    elif mode == "edge":
        # Peripheral/edge channel plus nearest neighbors. If radii are nearly
        # identical, choose a deterministic angular extreme perturbed by seed.
        radii = np.linalg.norm(positions - np.mean(positions, axis=0), axis=1)
        top = np.argsort(radii)[-max(4, min(n_channels, 2 * n_missing + 3)):]
        center = int(rng.choice(top))
        idx = np.argsort(dists[center])[:n_missing]
    elif mode == "high_variance":
        std = np.nanstd(signals, axis=0)
        pool = np.argsort(std)[-max(n_missing, min(n_channels, 2 * n_missing + 5)):]
        idx = rng.choice(pool, size=n_missing, replace=False)
    else:
        raise ValueError(f"unknown missing mode: {mode}")
    return np.asarray(sorted(map(int, idx)), dtype=int)


def apply_missing(signals: np.ndarray, bad_idx: np.ndarray) -> np.ndarray:
    masked = np.asarray(signals, dtype=float).copy()
    masked[:, bad_idx] = np.nan
    return masked


def normalize_positions_for_mne(positions: np.ndarray) -> np.ndarray:
    pos = np.asarray(positions, dtype=float)
    if pos.shape[1] == 2:
        pos = np.column_stack([pos, np.zeros(len(pos))])
    else:
        pos = pos[:, :3].copy()
    finite = np.isfinite(pos).all(axis=1)
    if finite.any():
        pos = pos - np.mean(pos[finite], axis=0)
        scale = float(np.max(np.linalg.norm(pos[finite], axis=1)))
        if not np.isfinite(scale) or scale <= 0:
            scale = 1.0
        pos = pos / scale
    pos[~finite] = 0.0
    return pos


def run_mne_spline(
    signals_missing: np.ndarray,
    positions: np.ndarray,
    sfreq: float,
    ch_names: List[str],
    bad_idx: np.ndarray,
) -> np.ndarray:
    import mne

    n_times, n_channels = signals_missing.shape
    if len(ch_names) != n_channels:
        ch_names = [f"EEG{i:03d}" for i in range(n_channels)]
    data = np.nan_to_num(signals_missing, nan=0.0, posinf=0.0, neginf=0.0)
    info = mne.create_info(ch_names=ch_names, sfreq=float(sfreq), ch_types="eeg")
    raw = mne.io.RawArray(data.T, info, verbose="ERROR")

    pos = normalize_positions_for_mne(positions)
    ch_pos = {name: tuple(pos[i, :3]) for i, name in enumerate(ch_names)}
    montage = mne.channels.make_dig_montage(ch_pos=ch_pos, coord_frame="head")
    raw.set_montage(montage, on_missing="ignore", verbose="ERROR")
    # Be explicit: MNE's EEG branch is spherical spline interpolation.
    raw.info["bads"] = [ch_names[i] for i in bad_idx]
    raw_interp = raw.copy().interpolate_bads(
        reset_bads=False,
        method="spline",
        origin="auto",
        verbose="ERROR",
    )
    out = raw_interp.get_data().T
    observed = ~np.isnan(signals_missing)
    out[observed] = signals_missing[observed]
    return out


def graph_cache_key(dataset_name: str, cfg: TRSSConfig) -> Tuple[str, int, float]:
    return (dataset_name, int(cfg.k), float(cfg.sigma))


def build_adj_cached(
    cache: Dict[Tuple[str, int, float], np.ndarray],
    dataset_name: str,
    positions: np.ndarray,
    signals: np.ndarray,
    cfg: TRSSConfig,
) -> np.ndarray:
    key = graph_cache_key(dataset_name, cfg)
    if key not in cache:
        graph = build_graph("knng", positions, signals=signals, k=int(cfg.k), sigma=float(cfg.sigma))
        adj = graph["adjacency"]
        if hasattr(adj, "toarray"):
            adj = adj.toarray()
        cache[key] = np.asarray(adj, dtype=float)
    return cache[key]


def run_trss(signals_missing: np.ndarray, adjacency: np.ndarray, cfg: TRSSConfig) -> np.ndarray:
    result = interpolate_signals(
        "trss",
        signals_missing,
        adjacency=adjacency,
        alpha=float(cfg.alpha),
        beta=float(cfg.beta),
        n_iter=int(cfg.n_iter),
        lr=float(cfg.lr),
    )
    return np.asarray(result["reconstructed"], dtype=float)


def corr_mean(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    vals: List[float] = []
    for ch in range(y_true.shape[1] if y_true.ndim == 2 else 1):
        a = y_true[:, ch] if y_true.ndim == 2 else y_true
        b = y_pred[:, ch] if y_pred.ndim == 2 else y_pred
        mask = np.isfinite(a) & np.isfinite(b)
        if np.sum(mask) < 3:
            continue
        aa = a[mask] - np.mean(a[mask])
        bb = b[mask] - np.mean(b[mask])
        denom = float(np.linalg.norm(aa) * np.linalg.norm(bb))
        if denom > 0:
            vals.append(float(np.dot(aa, bb) / denom))
    return float(np.mean(vals)) if vals else float("nan")


def extra_metrics(y_true: np.ndarray, y_pred: np.ndarray, runtime_s: float) -> Dict[str, float]:
    mask = np.isfinite(y_true) & np.isfinite(y_pred)
    if not np.any(mask):
        return {
            "nrmse": float("nan"), "corr_mean": float("nan"), "r2": float("nan"),
            "bias": float("nan"), "abs_bias": float("nan"), "amp_ratio": float("nan"),
            "runtime_s": float(runtime_s),
        }
    err = y_true[mask] - y_pred[mask]
    scale = float(np.nanstd(y_true[mask]))
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0
    sse = float(np.sum(err**2))
    sst = float(np.sum((y_true[mask] - np.mean(y_true[mask])) ** 2))
    amp_den = float(np.nanstd(y_true[mask]))
    amp_num = float(np.nanstd(y_pred[mask]))
    return {
        "nrmse": float(np.sqrt(np.mean(err**2)) / scale),
        "corr_mean": corr_mean(y_true, y_pred),
        "r2": float(1.0 - sse / sst) if sst > 0 else float("nan"),
        "bias": float(np.mean(y_pred[mask] - y_true[mask])),
        "abs_bias": float(abs(np.mean(y_pred[mask] - y_true[mask]))),
        "amp_ratio": float(amp_num / amp_den) if amp_den > 0 else float("nan"),
        "runtime_s": float(runtime_s),
    }


def evaluate_hidden(
    clean: np.ndarray,
    reconstructed: np.ndarray,
    bad_idx: np.ndarray,
    sfreq: float,
    runtime_s: float,
) -> Dict[str, float]:
    y_true = clean[:, bad_idx]
    y_pred = reconstructed[:, bad_idx]
    out: Dict[str, float] = {}
    try:
        out.update(evaluate_signals(y_true, y_pred, metrics=METRICS, sfreq=sfreq))
    except Exception:
        # Keep core metrics even if spectral metrics fail.
        err = y_true - y_pred
        out["mae"] = float(np.nanmean(np.abs(err)))
        out["rmse"] = float(np.sqrt(np.nanmean(err**2)))
        out["dtw"] = float("nan")
        out["snr"] = float("nan")
        out["lsd"] = float("nan")
        out["coherence_mean"] = float("nan")
    out.update(extra_metrics(y_true, y_pred, runtime_s=runtime_s))
    return out


def row_id(dataset: str, mode: str, missing_value: float | int, seed: int, method_label: str) -> str:
    return f"{dataset}|{mode}|{missing_value}|{seed}|{method_label}"


def append_row(path: Path, row: Dict[str, Any]) -> None:
    df = pd.DataFrame([row])
    header = not path.exists()
    df.to_csv(path, mode="a", header=header, index=False)


def load_done_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    try:
        df = pd.read_csv(path, usecols=["row_id"])
        return set(df["row_id"].astype(str).tolist())
    except Exception:
        return set()


def safe_eval_method(
    method_label: str,
    fn: Callable[[], np.ndarray],
    clean: np.ndarray,
    bad_idx: np.ndarray,
    sfreq: float,
) -> Tuple[Dict[str, float], bool, str, float]:
    t0 = time.perf_counter()
    success = True
    err_msg = ""
    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            recon = fn()
        warning_count = len(caught)
        runtime_s = time.perf_counter() - t0
        metrics = evaluate_hidden(clean, recon, bad_idx, sfreq, runtime_s)
        metrics["warning_count"] = float(warning_count)
        if not np.isfinite(recon[:, bad_idx]).all():
            success = False
            err_msg = "non-finite reconstruction"
    except Exception as exc:
        runtime_s = time.perf_counter() - t0
        success = False
        err_msg = f"{type(exc).__name__}: {exc}"
        metrics = {m: float("nan") for m in METRICS}
        metrics.update({
            "nrmse": float("nan"), "corr_mean": float("nan"), "r2": float("nan"),
            "bias": float("nan"), "abs_bias": float("nan"), "amp_ratio": float("nan"),
            "runtime_s": float(runtime_s), "warning_count": 0.0,
        })
    return metrics, success, err_msg, runtime_s


def base_case_row(
    dataset_name: str,
    info: Dict[str, Any],
    mode: str,
    missing_value: float | int,
    seed: int,
    bad_idx: np.ndarray,
    method_label: str,
    method_family: str,
    params: str,
) -> Dict[str, Any]:
    return {
        "row_id": row_id(dataset_name, mode, missing_value, seed, method_label),
        "dataset": dataset_name,
        "source_dataset": info.get("dataset", info.get("dataset_spec", dataset_name)),
        "sfreq": float(info.get("sfreq", np.nan)),
        "n_times": int(info.get("window_n_times", 0)),
        "n_channels": int(info.get("n_channels", 0)),
        "missing_mode": mode,
        "missing_value": missing_value,
        "n_missing": int(len(bad_idx)),
        "missing_ratio_actual": float(len(bad_idx) / max(1, int(info.get("n_channels", 1)))),
        "seed": int(seed),
        "bad_idx": " ".join(map(str, bad_idx.tolist())),
        "method": method_label,
        "method_family": method_family,
        "params": params,
    }


def run_benchmark(args: argparse.Namespace) -> Path:
    out_dir = ROOT / "results" / "trss_vs_mne_bads_extensive"
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_path = out_dir / f"raw_{args.profile}.csv"
    done = load_done_ids(raw_path)

    cfg_path = out_dir / f"config_{args.profile}.json"
    cfg_path.write_text(json.dumps({
        "profile": args.profile,
        "metrics": METRICS + ["nrmse", "corr_mean", "r2", "bias", "abs_bias", "amp_ratio", "runtime_s"],
        "trss_candidates": [asdict(c) for c in TRSS_CANDIDATES],
        "missing_modes": missing_modes(args.profile),
        "missing_values": missing_values(args.profile),
        "seeds": seeds(args.profile),
        "datasets": [asdict(s) | {"loader": str(s.loader)} for s in dataset_specs(args.profile)],
        "note": "MNE is Raw.interpolate_bads(method='spline'), i.e. MNE's EEG spherical spline implementation. Metrics are computed only on artificially hidden bad channels.",
    }, indent=2, default=str), encoding="utf-8")

    graph_cache: Dict[Tuple[str, int, float], np.ndarray] = {}
    total_cases = 0
    for spec in dataset_specs(args.profile):
        print(f"\n=== Loading {spec.name} ===", flush=True)
        try:
            data = load_dataset(spec)
        except Exception as exc:
            print(f"SKIP dataset {spec.name}: {type(exc).__name__}: {exc}", flush=True)
            continue
        clean = np.asarray(data["signals"], dtype=float)
        positions = np.asarray(data["positions"], dtype=float)
        info = dict(data["info"])
        sfreq = float(info.get("sfreq", 160.0))
        ch_names = list(info.get("ch_names", [f"CH{i:03d}" for i in range(clean.shape[1])]))
        dataset_name = spec.name
        print(f"Dataset {dataset_name}: signals={clean.shape}, sfreq={sfreq:.3f}, channels={len(ch_names)}", flush=True)

        for mode in missing_modes(args.profile):
            for missing_value in missing_values(args.profile):
                for seed in seeds(args.profile):
                    bad_idx = make_bad_indices(clean, positions, missing_value, mode, seed)
                    signals_missing = apply_missing(clean, bad_idx)
                    total_cases += 1

                    # MNE official spherical spline.
                    method_label = "mne_interpolate_bads_spline"
                    rid = row_id(dataset_name, mode, missing_value, seed, method_label)
                    if not args.resume or rid not in done:
                        row = base_case_row(dataset_name, info, mode, missing_value, seed, bad_idx, method_label, "mne", "method=spline; origin=auto")
                        metrics, success, err_msg, _ = safe_eval_method(
                            method_label,
                            lambda: run_mne_spline(signals_missing, positions, sfreq, ch_names, bad_idx),
                            clean,
                            bad_idx,
                            sfreq,
                        )
                        row.update(metrics)
                        row["success"] = bool(success)
                        row["error"] = err_msg
                        append_row(raw_path, row)
                        done.add(rid)

                    # TRSS candidates. These support default comparison, practical
                    # tuning, sensitivity, and oracle-grid upper bound.
                    for cfg in TRSS_CANDIDATES:
                        method_label = cfg.label
                        rid = row_id(dataset_name, mode, missing_value, seed, method_label)
                        if args.resume and rid in done:
                            continue
                        row = base_case_row(dataset_name, info, mode, missing_value, seed, bad_idx, method_label, "trss_grid", cfg.params_json())
                        try:
                            adj = build_adj_cached(graph_cache, dataset_name, positions, clean, cfg)
                            fn = lambda adj=adj, cfg=cfg: run_trss(signals_missing, adj, cfg)
                            metrics, success, err_msg, _ = safe_eval_method(method_label, fn, clean, bad_idx, sfreq)
                        except Exception as exc:
                            metrics = {m: float("nan") for m in METRICS}
                            metrics.update({
                                "nrmse": float("nan"), "corr_mean": float("nan"), "r2": float("nan"),
                                "bias": float("nan"), "abs_bias": float("nan"), "amp_ratio": float("nan"),
                                "runtime_s": 0.0, "warning_count": 0.0,
                            })
                            success = False
                            err_msg = f"{type(exc).__name__}: {exc}"
                        row.update(metrics)
                        row["success"] = bool(success)
                        row["error"] = err_msg
                        append_row(raw_path, row)
                        done.add(rid)

                    if total_cases % 10 == 0:
                        print(f"  completed case {total_cases}; rows={len(done)}", flush=True)

    print(f"\nRaw results written to: {raw_path}", flush=True)
    return raw_path


def paired_bootstrap_ci(diff: np.ndarray, n_boot: int = 5000, seed: int = 123) -> Tuple[float, float]:
    diff = np.asarray(diff, dtype=float)
    diff = diff[np.isfinite(diff)]
    if diff.size == 0:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    means = np.empty(n_boot, dtype=float)
    n = diff.size
    for i in range(n_boot):
        means[i] = np.mean(diff[rng.integers(0, n, size=n)])
    lo, hi = np.percentile(means, [2.5, 97.5])
    return float(lo), float(hi)


def wilcoxon_or_sign(diff: np.ndarray) -> Tuple[float, str]:
    diff = np.asarray(diff, dtype=float)
    diff = diff[np.isfinite(diff)]
    diff = diff[np.abs(diff) > 1e-15]
    if diff.size < 5:
        return float("nan"), "insufficient"
    try:
        from scipy.stats import wilcoxon
        res = wilcoxon(diff, alternative="two-sided", zero_method="wilcox")
        return float(res.pvalue), "wilcoxon"
    except Exception:
        # Two-sided sign-test fallback.
        from scipy.stats import binomtest
        n_pos = int(np.sum(diff > 0))
        res = binomtest(n_pos, n=diff.size, p=0.5, alternative="two-sided")
        return float(res.pvalue), "sign_test"


def select_representative_methods(df: pd.DataFrame) -> pd.DataFrame:
    """Add deployable tuned and oracle rows derived from TRSS grid candidates.

    - trss_oracle_grid: best TRSS candidate per exact case using ground truth. This
      is an upper bound, not deployable.
    - trss_cv_tuned_seed0: for each dataset/mode/missing_value, pick best candidate
      on seed 0 and reuse it on all seeds. This is a simple validation-style tuning
      policy and is more realistic than the oracle.
    """
    case_cols = ["dataset", "missing_mode", "missing_value", "seed"]
    group_cols = ["dataset", "missing_mode", "missing_value"]
    trss = df[df["method_family"].eq("trss_grid") & df["success"].astype(bool)].copy()
    if trss.empty:
        return df.copy()

    # Composite score for selecting candidates: nRMSE primary, with LSD as a small
    # spectral tie-breaker. Lower is better.
    trss["select_score"] = trss["nrmse"].astype(float) + 0.10 * trss["lsd"].astype(float).fillna(0)

    oracle_idx = trss.groupby(case_cols)["select_score"].idxmin()
    oracle = trss.loc[oracle_idx].copy()
    oracle["method"] = "trss_oracle_grid"
    oracle["method_family"] = "trss_oracle_upper_bound"
    oracle["row_id"] = oracle.apply(lambda r: row_id(r["dataset"], r["missing_mode"], r["missing_value"], int(r["seed"]), "trss_oracle_grid"), axis=1)

    # Seed-0 tuning. If seed 0 missing for a group, use first available seed.
    chosen_rows = []
    for key, g in trss.groupby(group_cols):
        train = g[g["seed"].eq(0)]
        if train.empty:
            first_seed = sorted(g["seed"].unique())[0]
            train = g[g["seed"].eq(first_seed)]
        best = train.loc[train["select_score"].idxmin()]
        chosen_rows.append((*key, best["method"]))
    chosen = pd.DataFrame(chosen_rows, columns=group_cols + ["chosen_method"])
    tuned = trss.merge(chosen, on=group_cols, how="inner")
    tuned = tuned[tuned["method"].eq(tuned["chosen_method"])].copy()
    tuned["method"] = "trss_cv_tuned_seed0"
    tuned["method_family"] = "trss_deployable_tuned"
    tuned["row_id"] = tuned.apply(lambda r: row_id(r["dataset"], r["missing_mode"], r["missing_value"], int(r["seed"]), "trss_cv_tuned_seed0"), axis=1)
    tuned["params"] = tuned["params"].astype(str) + "; tuning_policy=best_seed0_per_dataset_mode_loss"

    # Keep only MNE, default TRSS, plus derived tuned/oracle rows for headline.
    return pd.concat([df, oracle, tuned], ignore_index=True, sort=False)


def compare_methods(df: pd.DataFrame, method_a: str, method_b: str, metrics: Iterable[str]) -> pd.DataFrame:
    # method_a - method_b for lower-better metrics: negative means A better.
    key_cols = ["dataset", "missing_mode", "missing_value", "seed", "n_missing", "missing_ratio_actual"]
    a = df[df["method"].eq(method_a)].copy()
    b = df[df["method"].eq(method_b)].copy()
    merged = a.merge(b, on=key_cols, suffixes=("_a", "_b"))
    rows = []
    for metric in metrics:
        if f"{metric}_a" not in merged or f"{metric}_b" not in merged:
            continue
        av = pd.to_numeric(merged[f"{metric}_a"], errors="coerce")
        bv = pd.to_numeric(merged[f"{metric}_b"], errors="coerce")
        if metric in HIGHER_BETTER:
            diff = av - bv  # positive means A better
            rel = (av - bv) / bv.abs().replace(0, np.nan)
            a_better = diff > 0
        else:
            diff = av - bv  # negative means A better
            rel = (bv - av) / bv.abs().replace(0, np.nan)  # positive means A relative improvement
            a_better = diff < 0
        valid = np.isfinite(diff)
        d = diff[valid].to_numpy(dtype=float)
        r = rel[valid].to_numpy(dtype=float)
        p, test = wilcoxon_or_sign(d)
        ci_lo, ci_hi = paired_bootstrap_ci(d)
        rows.append({
            "method_a": method_a,
            "method_b": method_b,
            "metric": metric,
            "n_pairs": int(valid.sum()),
            "a_mean": float(np.nanmean(av)),
            "b_mean": float(np.nanmean(bv)),
            "mean_diff_a_minus_b": float(np.nanmean(d)) if d.size else float("nan"),
            "median_diff_a_minus_b": float(np.nanmedian(d)) if d.size else float("nan"),
            "ci95_diff_low": ci_lo,
            "ci95_diff_high": ci_hi,
            "mean_relative_improvement_of_a": float(np.nanmean(r)) if r.size else float("nan"),
            "median_relative_improvement_of_a": float(np.nanmedian(r)) if r.size else float("nan"),
            "a_win_rate": float(np.mean(a_better[valid])) if valid.sum() else float("nan"),
            "p_value": p,
            "test": test,
        })
    return pd.DataFrame(rows)


def summarize(raw_path: Path, profile: str) -> None:
    out_dir = raw_path.parent
    df = pd.read_csv(raw_path)
    for col in ["success"]:
        if col in df:
            df[col] = df[col].astype(str).str.lower().isin(["true", "1", "yes"])
    numeric_cols = ["mae", "rmse", "dtw", "snr", "lsd", "coherence_mean", "nrmse", "corr_mean", "r2", "bias", "abs_bias", "amp_ratio", "runtime_s", "warning_count"]
    for c in numeric_cols:
        if c in df:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    derived = select_representative_methods(df)
    derived.to_csv(out_dir / f"derived_{profile}.csv", index=False)

    headline_methods = [
        "mne_interpolate_bads_spline",
        "trss_default",
        "trss_cv_tuned_seed0",
        "trss_oracle_grid",
    ]
    head = derived[derived["method"].isin(headline_methods)].copy()
    summary = head.groupby(["method", "dataset", "missing_mode", "missing_value"], dropna=False).agg(
        n=("mae", "size"),
        success_rate=("success", "mean"),
        mae_mean=("mae", "mean"), mae_median=("mae", "median"),
        rmse_mean=("rmse", "mean"), nrmse_mean=("nrmse", "mean"),
        snr_mean=("snr", "mean"), lsd_mean=("lsd", "mean"),
        coherence_mean=("coherence_mean", "mean"), corr_mean=("corr_mean", "mean"),
        r2_mean=("r2", "mean"), runtime_s_mean=("runtime_s", "mean"),
        runtime_s_median=("runtime_s", "median"), warning_count_mean=("warning_count", "mean"),
    ).reset_index()
    summary.to_csv(out_dir / f"summary_by_scenario_{profile}.csv", index=False)

    overall = head.groupby(["method"], dropna=False).agg(
        n=("mae", "size"),
        success_rate=("success", "mean"),
        mae_mean=("mae", "mean"), mae_median=("mae", "median"),
        rmse_mean=("rmse", "mean"), nrmse_mean=("nrmse", "mean"),
        snr_mean=("snr", "mean"), lsd_mean=("lsd", "mean"),
        coherence_mean=("coherence_mean", "mean"), corr_mean=("corr_mean", "mean"),
        r2_mean=("r2", "mean"), runtime_s_mean=("runtime_s", "mean"),
        runtime_s_median=("runtime_s", "median"), warning_count_mean=("warning_count", "mean"),
    ).reset_index()
    overall.to_csv(out_dir / f"summary_overall_{profile}.csv", index=False)

    comp_frames = []
    pairs = [
        ("trss_default", "mne_interpolate_bads_spline"),
        ("trss_cv_tuned_seed0", "mne_interpolate_bads_spline"),
        ("trss_oracle_grid", "mne_interpolate_bads_spline"),
    ]
    cmp_metrics = ["mae", "rmse", "nrmse", "dtw", "snr", "lsd", "coherence_mean", "corr_mean", "r2", "runtime_s"]
    for a, b in pairs:
        comp_frames.append(compare_methods(head, a, b, cmp_metrics))
    comparisons = pd.concat(comp_frames, ignore_index=True, sort=False)
    comparisons.to_csv(out_dir / f"pairwise_comparisons_{profile}.csv", index=False)

    # Stratified win rates by missing mode and severity for MAE.
    mae_rows = []
    for a, b in pairs:
        a_df = head[head["method"].eq(a)]
        b_df = head[head["method"].eq(b)]
        key_cols = ["dataset", "missing_mode", "missing_value", "seed", "n_missing", "missing_ratio_actual"]
        m = a_df.merge(b_df, on=key_cols, suffixes=("_a", "_b"))
        m["a_win_mae"] = m["mae_a"] < m["mae_b"]
        m["rel_improve_mae"] = (m["mae_b"] - m["mae_a"]) / m["mae_b"].abs().replace(0, np.nan)
        for keys, g in m.groupby(["missing_mode", "missing_value"], dropna=False):
            mae_rows.append({
                "method_a": a,
                "method_b": b,
                "missing_mode": keys[0],
                "missing_value": keys[1],
                "n_pairs": int(len(g)),
                "a_win_rate_mae": float(g["a_win_mae"].mean()),
                "median_rel_improve_mae": float(g["rel_improve_mae"].median()),
                "mean_rel_improve_mae": float(g["rel_improve_mae"].mean()),
            })
    strat = pd.DataFrame(mae_rows)
    strat.to_csv(out_dir / f"mae_winrate_by_scenario_{profile}.csv", index=False)

    make_figures(out_dir, profile, head, comparisons, strat)
    write_report(out_dir, profile, overall, comparisons, strat, head)
    print(f"Summary written under: {out_dir}", flush=True)


def make_figures(out_dir: Path, profile: str, head: pd.DataFrame, comparisons: pd.DataFrame, strat: pd.DataFrame) -> None:
    fig_dir = out_dir / "figures"
    fig_dir.mkdir(exist_ok=True)

    # Overall MAE distribution.
    try:
        methods = ["mne_interpolate_bads_spline", "trss_default", "trss_cv_tuned_seed0", "trss_oracle_grid"]
        data = [head.loc[head["method"].eq(m), "nrmse"].dropna().to_numpy() for m in methods]
        plt.figure(figsize=(8, 4))
        plt.boxplot(data, tick_labels=["MNE spline", "TRSS default", "TRSS tuned", "TRSS oracle"], showfliers=False)
        plt.ylabel("NRMSE on hidden channels (lower is better)")
        plt.xticks(rotation=15, ha="right")
        plt.tight_layout()
        plt.savefig(fig_dir / f"nrmse_boxplot_{profile}.pdf")
        plt.close()
    except Exception:
        traceback.print_exc()

    # Runtime distribution.
    try:
        plt.figure(figsize=(8, 4))
        data = [head.loc[head["method"].eq(m), "runtime_s"].dropna().to_numpy() for m in methods]
        plt.boxplot(data, tick_labels=["MNE spline", "TRSS default", "TRSS tuned", "TRSS oracle"], showfliers=False)
        plt.ylabel("Runtime per case (s, lower is better)")
        plt.yscale("log")
        plt.xticks(rotation=15, ha="right")
        plt.tight_layout()
        plt.savefig(fig_dir / f"runtime_boxplot_{profile}.pdf")
        plt.close()
    except Exception:
        traceback.print_exc()

    # Win-rate heatmap for tuned TRSS vs MNE.
    try:
        sub = strat[strat["method_a"].eq("trss_cv_tuned_seed0")].copy()
        if not sub.empty:
            pivot = sub.pivot_table(index="missing_mode", columns="missing_value", values="a_win_rate_mae")
            plt.figure(figsize=(7, 3.2))
            im = plt.imshow(pivot.values, aspect="auto", vmin=0, vmax=1, cmap="viridis")
            plt.colorbar(im, label="TRSS tuned win-rate vs MNE (MAE)")
            plt.yticks(range(len(pivot.index)), pivot.index)
            plt.xticks(range(len(pivot.columns)), [str(c) for c in pivot.columns])
            plt.xlabel("Missing value: channel count or ratio")
            plt.tight_layout()
            plt.savefig(fig_dir / f"tuned_winrate_heatmap_{profile}.pdf")
            plt.close()
    except Exception:
        traceback.print_exc()


def _fmt_pct(x: float) -> str:
    if not np.isfinite(x):
        return "NA"
    return f"{100*x:.1f}%"


def write_report(out_dir: Path, profile: str, overall: pd.DataFrame, comparisons: pd.DataFrame, strat: pd.DataFrame, head: pd.DataFrame) -> None:
    report = out_dir / f"REPORT_{profile}.md"
    comp_mae = comparisons[comparisons["metric"].eq("mae")].copy()
    comp_nrmse = comparisons[comparisons["metric"].eq("nrmse")].copy()
    comp_runtime = comparisons[comparisons["metric"].eq("runtime_s")].copy()

    def lookup(comp: pd.DataFrame, a: str, metric: str) -> Dict[str, Any]:
        rows = comparisons[(comparisons["method_a"].eq(a)) & (comparisons["metric"].eq(metric))]
        if rows.empty:
            return {}
        return rows.iloc[0].to_dict()

    lines: List[str] = []
    lines.append(f"# TRSS vs MNE interpolate_bads() — {profile} profile")
    lines.append("")
    lines.append("## Protocol")
    lines.append("- MNE baseline: `Raw.interpolate_bads(reset_bads=False, method='spline', origin='auto')`, i.e. MNE's standard EEG spherical-spline bad-channel interpolation.")
    lines.append("- TRSS variants: default, seed-0 tuned per dataset/missing scenario, and oracle grid upper bound. Oracle uses ground truth and is **not deployable**; it estimates how much headroom TRSS has if tuning is perfect.")
    lines.append("- Metrics are computed only on artificially hidden channels: MAE, RMSE, NRMSE, DTW, SNR, LSD, coherence, correlation, R², bias/amplitude ratio, runtime and warnings/failures.")
    lines.append("- Missing cases include random channels, nearby clusters, peripheral/edge clusters and high-variance channels; values include one/two/few bad channels and ratio-based high-loss cases depending on profile.")
    lines.append("")
    lines.append("## Overall metrics")
    lines.append(overall.to_markdown(index=False, floatfmt=".4g"))
    lines.append("")
    lines.append("## Pairwise headline comparisons against MNE")
    subset = comparisons[comparisons["metric"].isin(["mae", "nrmse", "snr", "lsd", "corr_mean", "runtime_s"])]
    lines.append(subset.to_markdown(index=False, floatfmt=".4g"))
    lines.append("")
    lines.append("## Scenario MAE win-rates")
    lines.append(strat.to_markdown(index=False, floatfmt=".4g"))
    lines.append("")

    tuned_mae = lookup(comparisons, "trss_cv_tuned_seed0", "mae")
    default_mae = lookup(comparisons, "trss_default", "mae")
    oracle_mae = lookup(comparisons, "trss_oracle_grid", "mae")
    tuned_runtime = lookup(comparisons, "trss_cv_tuned_seed0", "runtime_s")

    lines.append("## Interpretation")
    if tuned_mae:
        win = tuned_mae.get("a_win_rate", float("nan"))
        rel = tuned_mae.get("median_relative_improvement_of_a", float("nan"))
        p = tuned_mae.get("p_value", float("nan"))
        lines.append(f"- Tuned TRSS vs MNE on MAE: win-rate={_fmt_pct(win)}, median relative improvement={_fmt_pct(rel)}, p={p:.3g}.")
    if default_mae:
        win = default_mae.get("a_win_rate", float("nan"))
        rel = default_mae.get("median_relative_improvement_of_a", float("nan"))
        lines.append(f"- Default TRSS vs MNE on MAE: win-rate={_fmt_pct(win)}, median relative improvement={_fmt_pct(rel)}. This estimates whether TRSS is useful without tuning.")
    if oracle_mae:
        win = oracle_mae.get("a_win_rate", float("nan"))
        rel = oracle_mae.get("median_relative_improvement_of_a", float("nan"))
        lines.append(f"- Oracle-grid TRSS vs MNE on MAE: win-rate={_fmt_pct(win)}, median relative improvement={_fmt_pct(rel)}. This is the best-case TRSS headroom, not a fair deployable baseline.")
    if tuned_runtime:
        rel = tuned_runtime.get("median_relative_improvement_of_a", float("nan"))
        diff = tuned_runtime.get("median_diff_a_minus_b", float("nan"))
        lines.append(f"- Runtime: for runtime lower is better; tuned TRSS median difference vs MNE is {diff:.4g} s. Positive relative improvement means TRSS is faster; negative means slower ({_fmt_pct(rel)}).")

    # Decision heuristic written transparently; final thesis prose should use the
    # actual numbers above rather than a blind accept/reject.
    lines.append("")
    lines.append("## Decision heuristic")
    lines.append("Use TRSS as the primary method only if the deployable tuned variant beats MNE on MAE/NRMSE with a large and statistically supported margin **and** the runtime/tuning burden is acceptable. If tuned TRSS is only comparable, wins mainly in oracle mode, or is slower/less stable, MNE should remain the practical default and TRSS should be framed as a research method useful in specific regimes (e.g., clustered losses or temporally smooth signals).")
    lines.append("")
    lines.append("## Output files")
    lines.append(f"- Raw grid results: `{(out_dir / f'raw_{profile}.csv').name}`")
    lines.append(f"- Derived headline rows: `{(out_dir / f'derived_{profile}.csv').name}`")
    lines.append(f"- Overall summary: `{(out_dir / f'summary_overall_{profile}.csv').name}`")
    lines.append(f"- Scenario summary: `{(out_dir / f'summary_by_scenario_{profile}.csv').name}`")
    lines.append(f"- Pairwise stats: `{(out_dir / f'pairwise_comparisons_{profile}.csv').name}`")
    lines.append(f"- Figures: `figures/`")
    report.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=["quick", "balanced", "full"], default="balanced")
    parser.add_argument("--resume", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--summarize-only", action="store_true")
    args = parser.parse_args()

    out_dir = ROOT / "results" / "trss_vs_mne_bads_extensive"
    raw_path = out_dir / f"raw_{args.profile}.csv"
    if args.summarize_only:
        summarize(raw_path, args.profile)
        return
    raw_path = run_benchmark(args)
    summarize(raw_path, args.profile)


if __name__ == "__main__":
    main()
