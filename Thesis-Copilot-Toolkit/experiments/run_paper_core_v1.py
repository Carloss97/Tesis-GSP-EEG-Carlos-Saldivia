#!/usr/bin/env python3
"""Execute and freeze the paper_core_v1 benchmark for the BSPC manuscript.

The script is deliberately independent from historical paper artefacts.  It
loads the real recordings declared by the frozen configuration, applies one
shared deterministic channel mask per paired case, evaluates TRSS and MNE
spherical splines on hidden channels only, and writes a resumable evidence
package.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
import time
import warnings
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib.pyplot as plt
import mne
import numpy as np
import pandas as pd
from scipy import stats

TOOLKIT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = TOOLKIT_ROOT.parent
if str(TOOLKIT_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLKIT_ROOT))

from src.evaluation.evaluation import evaluate_signals  # noqa: E402
from src.graph_construction.graph_constructors import build_graph  # noqa: E402
from src.interpolation_methods import interpolate_signals  # noqa: E402

LOWER_IS_BETTER = {"mae", "rmse", "nrmse", "dtw", "lsd", "runtime_s"}
HIGHER_IS_BETTER = {"snr", "coherence_mean", "corr_mean", "r2"}
QUALITY_METRICS = ["mae", "rmse", "nrmse", "snr", "dtw", "lsd", "coherence_mean", "corr_mean", "r2"]
METRICS = QUALITY_METRICS + ["runtime_s"]
BCI_STANDARD_NAMES = [
    "Fz", "FC3", "FC1", "FCz", "FC2", "FC4", "C5", "C3", "C1", "Cz", "C2",
    "C4", "C6", "CP3", "CP1", "CPz", "CP2", "CP4", "P1", "Pz", "P2", "POz",
]


@dataclass(frozen=True)
class RecordingSpec:
    dataset: str
    recording_id: str
    subject: int | None = None
    run: int | None = None
    session: str | None = None


@dataclass
class Recording:
    spec: RecordingSpec
    signals: np.ndarray
    positions: np.ndarray
    ch_names: list[str]
    sfreq: float
    source_file: str


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_config(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def recording_specs(config: dict[str, Any]) -> list[RecordingSpec]:
    specs: list[RecordingSpec] = []
    datasets = config["datasets"]
    phys = datasets["physionet_eegbci"]
    for subject in phys["subjects"]:
        for run in phys["runs"]:
            specs.append(RecordingSpec("physionet_eegbci", f"S{subject:03d}R{run:02d}", subject, run))
    bci = datasets["bci_competition_iv_2a"]
    for subject in bci["subjects"]:
        specs.append(RecordingSpec("bci_competition_iv_2a", f"A{subject:02d}{bci['session']}", subject, None, bci["session"]))
    specs.append(RecordingSpec("mne_sample", "sample_audvis_raw"))
    return specs


def count_expected_cases(config: dict[str, Any]) -> dict[str, int]:
    units = len(recording_specs(config))
    masks = len(config["masking"]["modes"]) * len(config["masking"]["severities"]) * len(config["masking"]["seeds"])
    computed = {"recording_units": units, "paired_cases": units * masks, "method_evaluations": units * masks * 2}
    declared = {key: int(value) for key, value in config.get("expected_counts", {}).items()}
    if declared and computed != declared:
        raise ValueError(f"Computed counts {computed} disagree with frozen config {declared}")
    return computed


def select_bci_eeg_names(ch_names: list[str], expected_count: int = 22) -> list[str]:
    selected = [name for name in ch_names if "EOG" not in name.upper()][:expected_count]
    if len(selected) != expected_count:
        raise ValueError(f"BCI IV 2a requires {expected_count} EEG channels; found {len(selected)}")
    if any("EOG" in name.upper() for name in selected):
        raise AssertionError("EOG channel leaked into the BCI EEG set")
    return selected


def _preprocess_raw(raw: mne.io.BaseRaw, config: dict[str, Any]) -> tuple[np.ndarray, np.ndarray, list[str], float]:
    prep = config["preprocessing"]
    start = float(prep["crop_start_s"])
    stop = start + float(prep["crop_duration_s"])
    raw.crop(start, stop, include_tmax=False).load_data(verbose="ERROR")
    if prep["average_reference"]:
        raw.set_eeg_reference("average", projection=False, verbose="ERROR")
    raw.filter(
        float(prep["bandpass_hz"][0]),
        float(prep["bandpass_hz"][1]),
        method="iir",
        iir_params={"order": 4, "ftype": "butter"},
        verbose="ERROR",
    )
    raw.resample(float(prep["target_sfreq_hz"]), verbose="ERROR")
    c0, c1 = map(float, prep["analysis_window_s"])
    raw.crop(c0, c1, include_tmax=False)
    signals = raw.get_data().T.astype(np.float64, copy=False)
    montage = raw.get_montage()
    if montage is None:
        raise ValueError("Recording has no montage after preprocessing")
    pos_dict = montage.get_positions()["ch_pos"]
    positions = np.asarray([pos_dict[name] for name in raw.ch_names], dtype=float)
    expected_samples = int(prep["expected_samples"])
    if signals.shape != (expected_samples, len(raw.ch_names)):
        raise ValueError(f"Unexpected processed shape {signals.shape}; expected ({expected_samples}, {len(raw.ch_names)})")
    if not np.isfinite(signals).all() or not np.isfinite(positions).all():
        raise ValueError("Non-finite signal or position after preprocessing")
    if np.any(np.linalg.norm(positions, axis=1) == 0):
        raise ValueError("Zero electrode position after montage assignment")
    return signals, positions, list(raw.ch_names), float(raw.info["sfreq"])


def load_recording(spec: RecordingSpec, config: dict[str, Any]) -> Recording:
    if spec.dataset == "physionet_eegbci":
        path = REPO_ROOT / "datasets" / "MNE-eegbci-data" / "files" / "eegmmidb" / "1.0.0" / f"S{spec.subject:03d}" / f"S{spec.subject:03d}R{spec.run:02d}.edf"
        raw = mne.io.read_raw_edf(path, preload=False, verbose="ERROR")
        raw.pick("eeg")
        mne.datasets.eegbci.standardize(raw)
        raw.set_montage(mne.channels.make_standard_montage("standard_1005"), on_missing="raise", verbose="ERROR")
    elif spec.dataset == "bci_competition_iv_2a":
        path = REPO_ROOT / "datasets" / "BCICIV_2a_gdf" / f"A{spec.subject:02d}{spec.session}.gdf"
        raw = mne.io.read_raw_gdf(path, preload=False, verbose="ERROR")
        selected = select_bci_eeg_names(list(raw.ch_names), 22)
        raw.pick(selected)
        raw.rename_channels(dict(zip(selected, BCI_STANDARD_NAMES, strict=True)))
        raw.set_channel_types({name: "eeg" for name in raw.ch_names}, verbose="ERROR")
        raw.set_montage(mne.channels.make_standard_montage("standard_1005"), on_missing="raise", verbose="ERROR")
    elif spec.dataset == "mne_sample":
        sample_root = Path(mne.datasets.sample.data_path(download=False))
        path = sample_root / "MEG" / "sample" / "sample_audvis_raw.fif"
        raw = mne.io.read_raw_fif(path, preload=False, verbose="ERROR")
        raw.pick("eeg")
        if raw.get_montage() is None:
            raw.set_montage(mne.channels.make_standard_montage("standard_1020"), on_missing="ignore", verbose="ERROR")
    else:
        raise KeyError(f"Unsupported dataset: {spec.dataset}")
    if not path.exists():
        raise FileNotFoundError(path)
    signals, positions, ch_names, sfreq = _preprocess_raw(raw, config)
    return Recording(spec, signals, positions, ch_names, sfreq, str(path.resolve()))


def make_bad_indices(positions: np.ndarray, severity: float, mode: str, seed: int) -> np.ndarray:
    n_channels = positions.shape[0]
    n_bad = max(1, int(round(n_channels * float(severity))))
    if n_bad >= n_channels:
        raise ValueError("Mask must leave at least one observed channel")
    rng = np.random.default_rng(int(seed))
    if mode == "random":
        selected = rng.choice(n_channels, size=n_bad, replace=False)
    elif mode == "nearby":
        anchor = int(rng.integers(0, n_channels))
        distances = np.linalg.norm(positions - positions[anchor], axis=1)
        # Stable tie breaking is required for reproducible masks.
        selected = np.lexsort((np.arange(n_channels), distances))[:n_bad]
    else:
        raise ValueError(f"Unknown masking mode: {mode}")
    return np.sort(np.asarray(selected, dtype=np.int64))


def mask_digest(indices: np.ndarray) -> str:
    return hashlib.sha256(np.asarray(indices, dtype="<i8").tobytes()).hexdigest()


def apply_channel_mask(signals: np.ndarray, bad_indices: np.ndarray) -> np.ndarray:
    masked = np.array(signals, dtype=float, copy=True)
    masked[:, bad_indices] = np.nan
    return masked


def evaluate_hidden_channels(clean: np.ndarray, reconstructed: np.ndarray, bad_indices: np.ndarray, sfreq: float) -> dict[str, float]:
    hidden_clean = clean[:, bad_indices]
    hidden_reconstructed = reconstructed[:, bad_indices]
    values = evaluate_signals(
        hidden_clean,
        hidden_reconstructed,
        metrics=["mae", "rmse", "dtw", "snr", "lsd", "coherence_mean"],
        sfreq=float(sfreq),
    )
    correlations = []
    for channel in range(hidden_clean.shape[1]):
        x = hidden_clean[:, channel]
        y = hidden_reconstructed[:, channel]
        if np.std(x) > 0 and np.std(y) > 0:
            correlations.append(float(np.corrcoef(x, y)[0, 1]))
    values["corr_mean"] = float(np.mean(correlations)) if correlations else float("nan")
    rms_reference = float(np.sqrt(np.mean(hidden_clean ** 2)))
    values["nrmse"] = float(values["rmse"] / max(rms_reference, 1e-15))
    r2_values = []
    for channel in range(hidden_clean.shape[1]):
        x = hidden_clean[:, channel]
        y = hidden_reconstructed[:, channel]
        denominator = float(np.sum((x - np.mean(x)) ** 2))
        if denominator > 0:
            r2_values.append(1.0 - float(np.sum((x - y) ** 2)) / denominator)
    values["r2"] = float(np.mean(r2_values)) if r2_values else float("nan")
    result = {metric: float(values[metric]) for metric in QUALITY_METRICS}
    if not all(np.isfinite(value) for value in result.values()):
        raise ValueError(f"Non-finite metric(s): {result}")
    return result


def reconstruct_trss(recording: Recording, masked: np.ndarray, config: dict[str, Any]) -> tuple[np.ndarray, float]:
    trss_cfg = config["methods"]["trss_fixed"]
    graph = build_graph(
        trss_cfg["graph"], recording.positions, signals=recording.signals,
        k=int(trss_cfg["k"]), sigma=float(trss_cfg["sigma"]),
    )["adjacency"]
    start = time.perf_counter()
    reconstructed = interpolate_signals(
        "trss", masked, adjacency=graph, alpha=float(trss_cfg["alpha"]), beta=float(trss_cfg["beta"]),
        n_iter=int(trss_cfg["n_iter"]), lr=float(trss_cfg["lr"]),
    )["reconstructed"]
    return np.asarray(reconstructed, dtype=float), time.perf_counter() - start


def reconstruct_mne(recording: Recording, masked: np.ndarray, bad_indices: np.ndarray) -> tuple[np.ndarray, float]:
    info = mne.create_info(recording.ch_names, recording.sfreq, ch_types="eeg")
    raw = mne.io.RawArray(np.nan_to_num(masked, nan=0.0).T, info, verbose="ERROR")
    montage = mne.channels.make_dig_montage(
        ch_pos={name: position for name, position in zip(recording.ch_names, recording.positions, strict=True)},
        coord_frame="head",
    )
    raw.set_montage(montage, on_missing="raise", verbose="ERROR")
    raw.info["bads"] = [recording.ch_names[index] for index in bad_indices]
    start = time.perf_counter()
    reconstructed = raw.interpolate_bads(method="spline", origin="auto", reset_bads=False, verbose="ERROR").get_data().T
    return np.asarray(reconstructed, dtype=float), time.perf_counter() - start


def observed_max_abs_error(clean: np.ndarray, reconstructed: np.ndarray, bad_indices: np.ndarray) -> float:
    observed = np.ones(clean.shape[1], dtype=bool)
    observed[bad_indices] = False
    return float(np.max(np.abs(clean[:, observed] - reconstructed[:, observed])))


def case_identifier(spec: RecordingSpec, mode: str, severity: float, seed: int) -> str:
    severity_tag = f"{int(round(100 * severity)):02d}"
    return f"{spec.dataset}__{spec.recording_id}__{mode}__p{severity_tag}__s{seed}"


def assert_no_duplicate_rows(frame: pd.DataFrame) -> None:
    if frame["row_id"].duplicated().any():
        duplicates = frame.loc[frame["row_id"].duplicated(keep=False), "row_id"].tolist()
        raise ValueError(f"Duplicate method evaluations: {duplicates[:10]}")


def _append_rows(path: Path, rows: list[dict[str, Any]]) -> None:
    frame = pd.DataFrame(rows)
    frame.to_csv(path, mode="a", header=not path.exists(), index=False)


def execute_benchmark(config: dict[str, Any], output_dir: Path, smoke: bool = False, resume: bool = True) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_path = output_dir / ("smoke_raw_results.csv" if smoke else "raw_results.csv")
    completed: set[str] = set()
    if resume and raw_path.exists():
        existing = pd.read_csv(raw_path)
        assert_no_duplicate_rows(existing)
        completed = set(existing["row_id"].astype(str))
    specs = recording_specs(config)
    modes = list(config["masking"]["modes"])
    severities = [float(value) for value in config["masking"]["severities"]]
    seeds = [int(value) for value in config["masking"]["seeds"]]
    if smoke:
        specs, modes, severities, seeds = specs[:1], modes[:1], severities[:1], seeds[:1]
    total_cases = len(specs) * len(modes) * len(severities) * len(seeds)
    case_number = 0
    for spec in specs:
        print(f"[{utc_now()}] loading {spec.dataset}/{spec.recording_id}", flush=True)
        recording = load_recording(spec, config)
        for mode in modes:
            for severity in severities:
                for seed in seeds:
                    case_number += 1
                    case_id = case_identifier(spec, mode, severity, seed)
                    bad = make_bad_indices(recording.positions, severity, mode, seed)
                    masked = apply_channel_mask(recording.signals, bad)
                    mask_hash = mask_digest(bad)
                    rows: list[dict[str, Any]] = []
                    for method in ("trss", "mne_spline"):
                        row_id = f"{case_id}__{method}"
                        if row_id in completed:
                            continue
                        base: dict[str, Any] = {
                            "row_id": row_id, "case_id": case_id, "dataset": spec.dataset,
                            "recording_id": spec.recording_id, "subject": spec.subject, "run": spec.run,
                            "session": spec.session, "mode": mode, "severity": severity, "seed": seed,
                            "n_times": recording.signals.shape[0], "n_channels": recording.signals.shape[1],
                            "n_bad": len(bad), "bad_indices": json.dumps(bad.tolist()),
                            "bad_names": json.dumps([recording.ch_names[i] for i in bad]), "mask_hash": mask_hash,
                            "method": method, "source_file": recording.source_file, "success": False,
                            "error": "", "timestamp_utc": utc_now(),
                        }
                        try:
                            if method == "trss":
                                reconstructed, runtime = reconstruct_trss(recording, masked, config)
                            else:
                                reconstructed, runtime = reconstruct_mne(recording, masked, bad)
                            metrics = evaluate_hidden_channels(recording.signals, reconstructed, bad, recording.sfreq)
                            obs_error = observed_max_abs_error(recording.signals, reconstructed, bad)
                            if obs_error > 1e-12:
                                raise ValueError(f"Observed channels changed (max abs error={obs_error:.3e})")
                            base.update(metrics)
                            base.update({"runtime_s": runtime, "observed_max_abs_error": obs_error, "success": True})
                        except Exception as exc:  # preserve failures in the evidence package
                            base["error"] = f"{type(exc).__name__}: {exc}"
                        rows.append(base)
                    if rows:
                        _append_rows(raw_path, rows)
                    if case_number == 1 or case_number % 10 == 0 or case_number == total_cases:
                        print(f"[{utc_now()}] cases {case_number}/{total_cases}", flush=True)
    frame = pd.read_csv(raw_path)
    assert_no_duplicate_rows(frame)
    return raw_path


def _paired_table(raw: pd.DataFrame) -> pd.DataFrame:
    if not raw["success"].astype(bool).all():
        failed = raw.loc[~raw["success"].astype(bool), ["row_id", "error"]]
        raise RuntimeError(f"Benchmark contains {len(failed)} failed evaluations:\n{failed.to_string(index=False)}")
    index_cols = ["case_id", "dataset", "recording_id", "subject", "run", "session", "mode", "severity", "seed", "n_times", "n_channels", "n_bad", "bad_indices", "bad_names", "mask_hash"]
    value_cols = METRICS + ["observed_max_abs_error"]
    paired = raw.pivot(index=index_cols, columns="method", values=value_cols).reset_index()
    paired.columns = ["_".join(str(part) for part in col if str(part)) if isinstance(col, tuple) else str(col) for col in paired.columns]
    required = [f"{metric}_{method}" for metric in METRICS for method in ("trss", "mne_spline")]
    missing = [column for column in required if column not in paired.columns]
    if missing:
        raise ValueError(f"Unpaired method results: {missing}")
    for metric in METRICS:
        trss = paired[f"{metric}_trss"].astype(float)
        mne_values = paired[f"{metric}_mne_spline"].astype(float)
        if metric in LOWER_IS_BETTER:
            difference = mne_values - trss
        else:
            difference = trss - mne_values
        paired[f"{metric}_advantage"] = difference
        paired[f"{metric}_relative_advantage"] = difference / np.maximum(np.abs(mne_values), 1e-12)
        paired[f"{metric}_trss_win"] = difference > 0
    return paired


def hierarchical_bootstrap_ci(frame: pd.DataFrame, metric: str, n_boot: int, seed: int, overall: bool) -> tuple[float, float]:
    """Return a recording-cluster bootstrap CI without repeated DataFrame filtering.

    Dataset and recording units are sampled with replacement.  All mask cases
    belonging to a selected recording are retained, preserving the frozen
    protocol's hierarchical descriptive bootstrap while keeping the 2,000
    resamples practical for manuscript regeneration.
    """
    rng = np.random.default_rng(seed)
    grouped = {
        dataset: [group[metric].to_numpy(dtype=float) for _, group in subset.groupby("recording_id", sort=False)]
        for dataset, subset in frame.groupby("dataset", sort=False)
    }
    datasets = list(grouped)
    values = np.empty(n_boot, dtype=float)
    for index in range(n_boot):
        selected_datasets = (
            rng.choice(datasets, size=len(datasets), replace=True).tolist()
            if overall else datasets
        )
        chunks: list[np.ndarray] = []
        for dataset in selected_datasets:
            recordings = grouped[str(dataset)]
            selected = rng.integers(0, len(recordings), size=len(recordings))
            chunks.extend(recordings[int(recording)] for recording in selected)
        values[index] = float(np.median(np.concatenate(chunks)))
    return float(np.quantile(values, 0.025)), float(np.quantile(values, 0.975))


def summarize_results(paired: pd.DataFrame, config: dict[str, Any]) -> tuple[pd.DataFrame, pd.DataFrame]:
    boot = config["bootstrap"]
    summary_rows: list[dict[str, Any]] = []
    scopes: list[tuple[str, pd.DataFrame, bool]] = [("overall", paired, True)]
    scopes.extend((dataset, paired[paired["dataset"] == dataset], False) for dataset in sorted(paired["dataset"].unique()))
    for scope, frame, overall in scopes:
        for metric in METRICS:
            rel_col = f"{metric}_relative_advantage"
            low, high = hierarchical_bootstrap_ci(frame, rel_col, int(boot["resamples"]), int(boot["seed"]), overall)
            summary_rows.append({
                "scope": scope, "metric": metric, "n_pairs": len(frame),
                "trss_median": float(frame[f"{metric}_trss"].median()),
                "mne_median": float(frame[f"{metric}_mne_spline"].median()),
                "median_advantage": float(frame[f"{metric}_advantage"].median()),
                "median_relative_advantage": float(frame[rel_col].median()),
                "bootstrap_ci_low": low, "bootstrap_ci_high": high,
                "trss_win_rate": float(frame[f"{metric}_trss_win"].mean()),
            })
    scenario = paired.groupby(["dataset", "mode", "severity"], as_index=False).agg(
        n_pairs=("case_id", "count"),
        mae_trss_median=("mae_trss", "median"),
        mae_mne_median=("mae_mne_spline", "median"),
        mae_relative_advantage_median=("mae_relative_advantage", "median"),
        mae_trss_win_rate=("mae_trss_win", "mean"),
        runtime_trss_median=("runtime_s_trss", "median"),
        runtime_mne_median=("runtime_s_mne_spline", "median"),
    )
    return pd.DataFrame(summary_rows), scenario


def choose_representative_cases(paired: pd.DataFrame) -> pd.DataFrame:
    score = paired["mae_relative_advantage"]
    median = float(score.median())
    severe_nearby = paired[(paired["mode"] == "nearby") & (paired["severity"] == paired["severity"].max())]
    severe_median = float(severe_nearby["mae_relative_advantage"].median())
    indices = {
        "best": score.idxmax(),
        "worst": score.idxmin(),
        "practical_tie": score.abs().idxmin(),
        "nearby_severe_median": (severe_nearby["mae_relative_advantage"] - severe_median).abs().idxmin(),
    }
    rows = []
    used: set[str] = set()
    for label, index in indices.items():
        row = paired.loc[index].copy()
        if row["case_id"] in used:
            continue
        used.add(str(row["case_id"]))
        row["selection_label"] = label
        rows.append(row)
    return pd.DataFrame(rows)


def _spec_lookup(config: dict[str, Any]) -> dict[tuple[str, str], RecordingSpec]:
    return {(spec.dataset, spec.recording_id): spec for spec in recording_specs(config)}


def materialize_representatives(cases: pd.DataFrame, config: dict[str, Any], output_dir: Path) -> None:
    lookup = _spec_lookup(config)
    npz_dir = output_dir / "representative_cases"
    npz_dir.mkdir(exist_ok=True)
    for _, row in cases.iterrows():
        spec = lookup[(row["dataset"], row["recording_id"])]
        recording = load_recording(spec, config)
        bad = make_bad_indices(recording.positions, float(row["severity"]), str(row["mode"]), int(row["seed"]))
        masked = apply_channel_mask(recording.signals, bad)
        trss, _ = reconstruct_trss(recording, masked, config)
        mne_rec, _ = reconstruct_mne(recording, masked, bad)
        path = npz_dir / f"{row['selection_label']}__{row['case_id']}.npz"
        np.savez_compressed(
            path, clean=recording.signals, masked=masked, trss=trss, mne_spline=mne_rec,
            positions=recording.positions, ch_names=np.asarray(recording.ch_names), bad_indices=bad,
            target_channel=np.asarray(int(bad[0])), sfreq=np.asarray(recording.sfreq),
            case_id=np.asarray(row["case_id"]), dataset=np.asarray(row["dataset"]),
            recording_id=np.asarray(row["recording_id"]), mode=np.asarray(row["mode"]),
            severity=np.asarray(float(row["severity"])), seed=np.asarray(int(row["seed"])),
        )


def _latex_escape(text: Any) -> str:
    value = str(text)
    for old, new in [("\\", "\\textbackslash{}"), ("_", "\\_"), ("%", "\\%"), ("&", "\\&"), ("#", "\\#")]:
        value = value.replace(old, new)
    return value


def write_tables(paired: pd.DataFrame, summary: pd.DataFrame, scenario: pd.DataFrame, output_dir: Path) -> None:
    table_dir = output_dir / "tables"
    table_dir.mkdir(exist_ok=True)
    cohort = paired.groupby("dataset", as_index=False).agg(recordings=("recording_id", "nunique"), channels_min=("n_channels", "min"), channels_max=("n_channels", "max"), paired_cases=("case_id", "count"))
    lines = ["\\begin{tabular}{lrrrr}", "\\toprule", "Dataset & Recordings & Channels (min) & Channels (max) & Paired cases \\\\", "\\midrule"]
    for _, row in cohort.iterrows():
        lines.append(f"{_latex_escape(row.dataset)} & {int(row.recordings)} & {int(row.channels_min)} & {int(row.channels_max)} & {int(row.paired_cases)} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (table_dir / "cohort.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    overall = summary[summary["scope"] == "overall"]
    lines = ["\\begin{tabular}{lrrrr}", "\\toprule", "Metric & TRSS median & MNE spline median & Relative advantage [95\\% CI] & Win rate \\\\", "\\midrule"]
    metric_label = {
        "mae": "MAE", "rmse": "RMSE", "nrmse": "NRMSE", "snr": "SNR", "dtw": "DTW",
        "lsd": "LSD", "coherence_mean": "Coherence", "corr_mean": "Correlation", "r2": "$R^2$",
        "runtime_s": "Runtime (s)",
    }
    for _, row in overall.iterrows():
        rel = 100.0 * row.median_relative_advantage
        lo = 100.0 * row.bootstrap_ci_low
        hi = 100.0 * row.bootstrap_ci_high
        label = metric_label.get(str(row.metric), _latex_escape(row.metric))
        lines.append(f"{label} & {row.trss_median:.4g} & {row.mne_median:.4g} & {rel:.1f}\\% [{lo:.1f}, {hi:.1f}] & {100*row.trss_win_rate:.1f}\\% \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (table_dir / "overall_metrics.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    mae = scenario.groupby(["mode", "severity"], as_index=False).agg(n_pairs=("n_pairs", "sum"), relative=("mae_relative_advantage_median", "median"), win_rate=("mae_trss_win_rate", "mean"))
    lines = ["\\begin{tabular}{lrrr}", "\\toprule", "Mask mode & Missing channels & Median relative MAE advantage & TRSS win rate \\\\", "\\midrule"]
    for _, row in mae.iterrows():
        lines.append(f"{row['mode'].capitalize()} & {100*row['severity']:.0f}\\% & {100*row['relative']:.1f}\\% & {100*row['win_rate']:.1f}\\% \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (table_dir / "mae_by_scenario.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    macro_lines = ["% Auto-generated from paper_core_v1/summary_metrics.csv; do not edit manually."]
    metric_macro = {
        "mae": "MAE", "rmse": "RMSE", "nrmse": "NRMSE", "snr": "SNR", "dtw": "DTW",
        "lsd": "LSD", "coherence_mean": "Coherence", "corr_mean": "Correlation", "r2": "Rsquared",
        "runtime_s": "Runtime",
    }
    scope_macro = {
        "overall": "Overall",
        "bci_competition_iv_2a": "BciCompetitionIvTwoA",
        "mne_sample": "MneSample",
        "physionet_eegbci": "PhysionetEegbci",
    }
    for _, row in summary.iterrows():
        scope = scope_macro[str(row["scope"])]
        metric = metric_macro[str(row["metric"])]
        macro_lines.extend([
            f"\\newcommand{{\\{scope}{metric}Advantage}}{{{100 * row['median_relative_advantage']:.1f}\\%}}",
            f"\\newcommand{{\\{scope}{metric}CILow}}{{{100 * row['bootstrap_ci_low']:.1f}\\%}}",
            f"\\newcommand{{\\{scope}{metric}CIHigh}}{{{100 * row['bootstrap_ci_high']:.1f}\\%}}",
            f"\\newcommand{{\\{scope}{metric}WinRate}}{{{100 * row['trss_win_rate']:.1f}\\%}}",
            f"\\newcommand{{\\{scope}{metric}TRSSMedian}}{{{row['trss_median']:.4g}}}",
            f"\\newcommand{{\\{scope}{metric}MNEMedian}}{{{row['mne_median']:.4g}}}",
        ])
    (table_dir / "results_macros.tex").write_text("\n".join(macro_lines) + "\n", encoding="utf-8")


def write_figures(paired: pd.DataFrame, output_dir: Path) -> None:
    figure_dir = output_dir / "figures"
    figure_dir.mkdir(exist_ok=True)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    for mode, marker, offset in [("random", "o", -0.45), ("nearby", "s", 0.45)]:
        subset = paired[paired["mode"] == mode]
        grouped = subset.groupby("severity")["mae_relative_advantage"].agg(["median", lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)]).reset_index()
        x = 100 * grouped["severity"].to_numpy() + offset
        median = 100 * grouped["median"].to_numpy()
        lower = 100 * grouped["<lambda_0>"].to_numpy()
        upper = 100 * grouped["<lambda_1>"].to_numpy()
        ax.errorbar(
            x, median, yerr=np.vstack([median - lower, upper - median]), marker=marker,
            lw=1.5, capsize=3.5, markersize=5.5, label=mode.capitalize(),
        )
    ax.axhline(0, color="0.35", lw=0.9, ls="--")
    ax.set(xlabel="Missing channels (%)", ylabel="Relative MAE advantage of TRSS (%)")
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(1.01, 1.0))
    fig.tight_layout()
    fig.savefig(figure_dir / "mae_advantage_by_severity.pdf", bbox_inches="tight")
    fig.savefig(figure_dir / "mae_advantage_by_severity.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    data = [paired["runtime_s_trss"], paired["runtime_s_mne_spline"]]
    ax.boxplot(data, tick_labels=["TRSS", "MNE spline"], showfliers=False)
    ax.set_yscale("log")
    ax.set(ylabel="Runtime per reconstruction (s)")
    fig.tight_layout()
    fig.savefig(figure_dir / "runtime_distribution.pdf", bbox_inches="tight")
    fig.savefig(figure_dir / "runtime_distribution.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

    npz_files = sorted((output_dir / "representative_cases").glob("*.npz"))
    if npz_files:
        fig, axes = plt.subplots(len(npz_files), 1, figsize=(7.2, 2.0 * len(npz_files)), sharex=False)
        axes = np.atleast_1d(axes)
        for ax, path in zip(axes, npz_files, strict=True):
            payload = np.load(path, allow_pickle=False)
            channel = int(payload["target_channel"])
            sfreq = float(payload["sfreq"])
            t = np.arange(payload["clean"].shape[0]) / sfreq
            ax.plot(t, payload["clean"][:, channel] * 1e6, color="black", lw=1.2, label="Reference")
            ax.plot(t, payload["trss"][:, channel] * 1e6, color="#0072B2", lw=1.1, ls="--", label="TRSS")
            ax.plot(t, payload["mne_spline"][:, channel] * 1e6, color="#D55E00", lw=1.1, ls=":", label="MNE spline")
            ax.set_ylabel("Amplitude (µV)")
            title_key = path.stem.split("__", 1)[0]
            title = {
                "best": "(a) TRSS-best case",
                "nearby_severe_median": "(b) Severe-nearby median case",
                "practical_tie": "(c) Practical tie",
                "worst": "(d) TRSS-worst case",
            }.get(title_key, title_key.replace("_", " ").title())
            ax.set_title(title, loc="left", fontsize=10)
        axes[-1].set_xlabel("Time (s)")
        handles, labels = axes[0].get_legend_handles_labels()
        fig.legend(handles, labels, frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.01), ncol=3)
        fig.tight_layout(rect=(0, 0, 1, 0.96))
        fig.savefig(figure_dir / "representative_reconstructions.pdf", bbox_inches="tight")
        fig.savefig(figure_dir / "representative_reconstructions.png", dpi=220, bbox_inches="tight")
        plt.close(fig)

        fig, axes = plt.subplots(len(npz_files), 1, figsize=(7.2, 2.0 * len(npz_files)), sharex=True)
        axes = np.atleast_1d(axes)
        for ax, path in zip(axes, npz_files, strict=True):
            payload = np.load(path, allow_pickle=False)
            channel = int(payload["target_channel"])
            sfreq = float(payload["sfreq"])
            for key, color, linestyle, label in [
                ("clean", "black", "-", "Reference"),
                ("trss", "#0072B2", "--", "TRSS"),
                ("mne_spline", "#D55E00", ":", "MNE spline"),
            ]:
                values = payload[key][:, channel] * 1e6
                window = np.hanning(len(values))
                frequencies = np.fft.rfftfreq(len(values), d=1.0 / sfreq)
                density = np.abs(np.fft.rfft((values - np.mean(values)) * window)) ** 2
                density /= max(float(np.sum(window ** 2) * sfreq), 1e-30)
                keep = (frequencies >= 0.5) & (frequencies <= 45.0)
                ax.semilogy(
                    frequencies[keep], np.maximum(density[keep], 1e-30), color=color,
                    ls=linestyle, lw=1.1, label=label,
                )
            ax.set_ylabel("PSD (µV²/Hz)")
            title_key = path.stem.split("__", 1)[0]
            title = {
                "best": "(a) TRSS-best case",
                "nearby_severe_median": "(b) Severe-nearby median case",
                "practical_tie": "(c) Practical tie",
                "worst": "(d) TRSS-worst case",
            }.get(title_key, title_key.replace("_", " ").title())
            ax.set_title(title, loc="left", fontsize=10)
        axes[-1].set_xlabel("Frequency (Hz)")
        handles, labels = axes[0].get_legend_handles_labels()
        fig.legend(handles, labels, frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.01), ncol=3)
        fig.tight_layout(rect=(0, 0, 1, 0.96))
        fig.savefig(figure_dir / "representative_psd.pdf", bbox_inches="tight")
        fig.savefig(figure_dir / "representative_psd.png", dpi=220, bbox_inches="tight")
        plt.close(fig)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_manifest(config_path: Path, output_dir: Path, counts: dict[str, int]) -> None:
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True).strip()
    except Exception:
        commit = "unavailable"
    files = []
    for path in sorted(output_dir.rglob("*")):
        if path.is_file() and path.name != "manifest.json":
            files.append({"path": str(path.relative_to(output_dir)), "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    manifest = {
        "protocol": "paper_core_v1", "created_utc": utc_now(), "git_commit": commit,
        "config_path": str(config_path.resolve()), "config_sha256": sha256_file(config_path),
        "python": sys.version, "platform": platform.platform(),
        "versions": {"numpy": np.__version__, "pandas": pd.__version__, "mne": mne.__version__},
        "counts": counts,
        "implementation_details": {
            "filter": "MNE IIR fourth-order Butterworth, zero-phase filtfilt",
            "mask_pairing": "same bad_indices and mask_hash for both methods",
            "metric_support": "hidden channels only",
            "mne_method": "spline with origin=auto",
            "dtw_max_points": 80,
        },
        "files": files,
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def analyze(config: dict[str, Any], config_path: Path, output_dir: Path) -> None:
    raw_path = output_dir / "raw_results.csv"
    raw = pd.read_csv(raw_path)
    assert_no_duplicate_rows(raw)
    counts = count_expected_cases(config)
    if len(raw) != counts["method_evaluations"]:
        raise ValueError(f"Expected {counts['method_evaluations']} rows, found {len(raw)}")
    paired = _paired_table(raw)
    if len(paired) != counts["paired_cases"]:
        raise ValueError(f"Expected {counts['paired_cases']} paired cases, found {len(paired)}")
    if paired["case_id"].duplicated().any():
        raise ValueError("Duplicate paired cases")
    paired.to_csv(output_dir / "paired_results.csv", index=False)
    summary, scenario = summarize_results(paired, config)
    summary.to_csv(output_dir / "summary_metrics.csv", index=False)
    summary[summary["scope"] == "overall"].to_csv(output_dir / "summary_overall.csv", index=False)
    summary[summary["scope"] != "overall"].to_csv(output_dir / "summary_by_dataset.csv", index=False)
    summary[["scope", "metric", "n_pairs", "median_relative_advantage", "bootstrap_ci_low", "bootstrap_ci_high"]].to_csv(output_dir / "bootstrap_summary.csv", index=False)
    scenario.to_csv(output_dir / "summary_by_scenario.csv", index=False)
    reps = choose_representative_cases(paired)
    reps.to_csv(output_dir / "representative_cases.csv", index=False)
    materialize_representatives(reps, config, output_dir)
    write_tables(paired, summary, scenario, output_dir)
    write_figures(paired, output_dir)
    success_counts = {**counts, "raw_rows": len(raw), "successful_evaluations": int(raw["success"].astype(bool).sum()), "paired_rows": len(paired)}
    write_manifest(config_path, output_dir, success_counts)


def parse_args() -> argparse.Namespace:
    default_config = TOOLKIT_ROOT / "paper" / "bspc" / "evidence" / "paper_core_v1" / "config.json"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=default_config)
    parser.add_argument("--output-dir", type=Path, default=default_config.parent)
    parser.add_argument("--smoke", action="store_true", help="Run one real paired case only")
    parser.add_argument("--analysis-only", action="store_true")
    parser.add_argument("--no-resume", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    output_dir = args.output_dir.resolve()
    config = read_config(config_path)
    # The shared evaluator's documented bounded-DTW default is 80 points.
    os.environ["B2_DTW_MAX_POINTS"] = "80"
    warnings.filterwarnings("ignore", message=".*Only.*head digitization points.*")
    print(json.dumps(count_expected_cases(config), indent=2))
    if not args.analysis_only:
        execute_benchmark(config, output_dir, smoke=args.smoke, resume=not args.no_resume)
    if not args.smoke:
        analyze(config, config_path, output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
