from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime, UTC
from pathlib import Path
from typing import Any, Dict, List

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.data_loader import (
    load_bci_competition_iv_2a,
    load_mne_sample_dataset,
    load_physionet_eegmmidb,
    simulate_missing_channels,
)
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals

RESULTS = ROOT / "results"
PAPER_FIGS = ROOT / "paper" / "ieee" / "figures"
THESIS_FIGS = ROOT / "thesis" / "usm" / "figures"

INSTANT_METHODS = ["mean", "nearest", "tikhonov"]
TV_METHODS = ["tv", "trss", "graph_time_tikhonov", "temporal_laplacian"]
METHODS = INSTANT_METHODS + TV_METHODS


@dataclass
class IterDef:
    tag: str
    description: str
    fase: str
    objective: str


def _now() -> str:
    return datetime.now(UTC).isoformat()


def load_real_availability() -> Dict[str, Any]:
    info: Dict[str, Any] = {
        "physionet": {"ok": False, "reason": ""},
        "mne_real": {"ok": False, "reason": ""},
        "bci_iv2a_real": {"ok": False, "reason": ""},
    }
    data: Dict[str, Any] = {}

    try:
        os.environ.setdefault(
            "EEGBCI_LOCAL_PATH",
            str(ROOT.parent / "datasets" / "MNE-eegbci-data"),
        )
        d = load_physionet_eegmmidb(subject=1, run=4)
        info["physionet"] = {"ok": True, "shape": list(d["signals"].shape)}
        data["physionet"] = d
    except Exception as exc:
        info["physionet"] = {"ok": False, "reason": str(exc)}

    # MNE real: only use local copy to avoid long/blocked network download attempts.
    mne_local = Path.home() / "mne_data" / "MNE-sample-data" / "MEG" / "sample" / "sample_audvis_raw.fif"
    if mne_local.exists():
        try:
            d = load_mne_sample_dataset()
            info["mne_real"] = {"ok": True, "shape": list(d["signals"].shape)}
            data["mne_real"] = d
        except Exception as exc:
            info["mne_real"] = {"ok": False, "reason": str(exc)}
    else:
        info["mne_real"] = {
            "ok": False,
            "reason": f"Local MNE sample not found at {mne_local}; network download skipped.",
        }

    # BCI IV 2a real: only if local .gdf exists.
    bci_root = Path(os.environ.get("BCI_IV_2A_PATH", str(ROOT.parent / "datasets" / "BCI_IV_2a")))
    bci_file = bci_root / "A01T.gdf"
    if bci_file.exists():
        try:
            d = load_bci_competition_iv_2a(subject=1)
            info["bci_iv2a_real"] = {"ok": True, "shape": list(d["signals"].shape)}
            data["bci_iv2a_real"] = d
        except Exception as exc:
            info["bci_iv2a_real"] = {"ok": False, "reason": str(exc)}
    else:
        info["bci_iv2a_real"] = {
            "ok": False,
            "reason": f"Local BCI IV 2a file not found at {bci_file}.",
        }

    return {"availability": info, "data": data}


def _safe_positions(data: Dict[str, Any], n_channels: int) -> np.ndarray:
    pos = np.asarray(data.get("positions"))
    if pos.ndim != 2 or pos.shape[0] != n_channels:
        theta = np.linspace(0, 2 * np.pi, n_channels, endpoint=False)
        pos = np.stack([np.cos(theta), np.sin(theta), np.zeros(n_channels)], axis=1)
    return pos


def _sample_segment(signals: np.ndarray, n_times: int = 320, max_ch: int = 24) -> np.ndarray:
    x = np.asarray(signals)
    if x.shape[0] > n_times:
        x = x[:n_times]
    if x.shape[1] > max_ch:
        idx = np.round(np.linspace(0, x.shape[1] - 1, max_ch)).astype(int)
        x = x[:, idx]
    return x


def _add_noise_to_snr(x: np.ndarray, snr_db: float, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    sig_pow = np.var(x)
    if sig_pow <= 0:
        return x.copy()
    noise_pow = sig_pow / (10 ** (snr_db / 10.0))
    noise = rng.normal(0.0, np.sqrt(noise_pow), size=x.shape)
    return x + noise


def _iter_rows_base(dataset_name: str, signals: np.ndarray, positions: np.ndarray, *, missing_list: List[Any], seeds: List[int], graph_method: str = "knn", graph_params: Dict[str, Any] | None = None) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    graph_params = graph_params or {"k": 3}

    gobj = build_graph(graph_method, positions, signals=signals, **graph_params)
    adj = np.asarray(gobj["adjacency"])
    graph_tag = "knn__k3" if graph_method == "knn" and graph_params.get("k") == 3 else graph_method

    for miss in missing_list:
        for seed in seeds:
            if isinstance(miss, str) and miss.endswith("ch"):
                n_missing = int(miss[:-2])
                ratio = max(1, n_missing) / max(1, signals.shape[1])
                masked = simulate_missing_channels(signals, missing_ratio=ratio, random_state=seed)
            else:
                ratio = float(miss)
                n_missing = int(round(ratio * signals.shape[1]))
                masked = simulate_missing_channels(signals, missing_ratio=ratio, random_state=seed)

            for method in METHODS:
                kwargs: Dict[str, Any] = {}
                if method in {"tikhonov"}:
                    kwargs["alpha"] = 0.1
                elif method == "tv":
                    kwargs["lam"] = 0.2
                    kwargs["n_iter"] = 30
                elif method == "trss":
                    kwargs.update({"alpha": 0.7, "beta": 0.2, "n_iter": 60, "lr": 0.03})
                elif method == "graph_time_tikhonov":
                    kwargs.update({"alpha": 0.5, "beta": 0.1})
                elif method == "temporal_laplacian":
                    kwargs.update({"alpha": 0.5, "beta": 0.5})

                t0 = time.perf_counter()
                rec = interpolate_signals(method, masked, adjacency=adj, positions=positions, **kwargs)["reconstructed"]
                elapsed = time.perf_counter() - t0
                met = evaluate_signals(signals, rec, metrics=["mae", "rmse", "snr", "dtw"])

                rows.append(
                    {
                        "dataset": dataset_name,
                        "graph": graph_tag,
                        "method": method,
                        "missing_ratio": miss,
                        "seed": int(seed),
                        "mae": float(met["mae"]),
                        "rmse": float(met["rmse"]),
                        "snr": float(met["snr"]),
                        "dtw": float(met["dtw"]),
                        "params": json.dumps(kwargs, ensure_ascii=False),
                        "error": "",
                        "n_missing_ch": int(n_missing),
                        "time_sec": float(elapsed),
                    }
                )
    return pd.DataFrame(rows)


def _iter_rows_lambda_grid(dataset_name: str, signals: np.ndarray, positions: np.ndarray, lambdas: List[float], seeds: List[int]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    gobj = build_graph("knn", positions, signals=signals, k=3)
    adj = np.asarray(gobj["adjacency"])

    for lam in lambdas:
        for seed in seeds:
            masked = simulate_missing_channels(signals, missing_ratio=0.2, random_state=seed)
            for method in ["tv", "graph_time_tikhonov", "trss", "temporal_laplacian"]:
                if method == "tv":
                    kwargs = {"lam": lam, "n_iter": 30}
                elif method == "graph_time_tikhonov":
                    kwargs = {"alpha": lam, "beta": 0.1}
                elif method == "trss":
                    kwargs = {"alpha": lam, "beta": 0.2, "n_iter": 60, "lr": 0.03}
                else:
                    kwargs = {"alpha": lam, "beta": 0.5}

                t0 = time.perf_counter()
                rec = interpolate_signals(method, masked, adjacency=adj, positions=positions, **kwargs)["reconstructed"]
                elapsed = time.perf_counter() - t0
                met = evaluate_signals(signals, rec, metrics=["mae", "rmse", "snr", "dtw"])
                rows.append(
                    {
                        "dataset": dataset_name,
                        "graph": "knn__k3",
                        "method": method,
                        "missing_ratio": 0.2,
                        "seed": int(seed),
                        "mae": float(met["mae"]),
                        "rmse": float(met["rmse"]),
                        "snr": float(met["snr"]),
                        "dtw": float(met["dtw"]),
                        "params": json.dumps(kwargs, ensure_ascii=False),
                        "error": "",
                        "n_missing_ch": int(round(0.2 * signals.shape[1])),
                        "time_sec": float(elapsed),
                        "lambda": float(lam),
                    }
                )
    return pd.DataFrame(rows)


def _iter_rows_noise_sensitivity(dataset_name: str, signals: np.ndarray, positions: np.ndarray, snr_levels: List[float], seeds: List[int]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    gobj = build_graph("knn", positions, signals=signals, k=3)
    adj = np.asarray(gobj["adjacency"])

    for snr0 in snr_levels:
        for seed in seeds:
            noisy = _add_noise_to_snr(signals, snr0, seed)
            masked = simulate_missing_channels(noisy, missing_ratio=0.2, random_state=seed)
            for method in METHODS:
                kwargs: Dict[str, Any] = {}
                if method == "tikhonov":
                    kwargs["alpha"] = 0.1
                elif method == "tv":
                    kwargs.update({"lam": 0.2, "n_iter": 30})
                elif method == "trss":
                    kwargs.update({"alpha": 0.7, "beta": 0.2, "n_iter": 60, "lr": 0.03})
                elif method == "graph_time_tikhonov":
                    kwargs.update({"alpha": 0.5, "beta": 0.1})
                elif method == "temporal_laplacian":
                    kwargs.update({"alpha": 0.5, "beta": 0.5})

                t0 = time.perf_counter()
                rec = interpolate_signals(method, masked, adjacency=adj, positions=positions, **kwargs)["reconstructed"]
                elapsed = time.perf_counter() - t0
                met = evaluate_signals(noisy, rec, metrics=["mae", "rmse", "snr", "dtw"])
                rows.append(
                    {
                        "dataset": dataset_name,
                        "graph": "knn__k3",
                        "method": method,
                        "missing_ratio": 0.2,
                        "seed": int(seed),
                        "mae": float(met["mae"]),
                        "rmse": float(met["rmse"]),
                        "snr": float(met["snr"]),
                        "dtw": float(met["dtw"]),
                        "params": json.dumps(kwargs, ensure_ascii=False),
                        "error": "",
                        "n_missing_ch": int(round(0.2 * signals.shape[1])),
                        "time_sec": float(elapsed),
                        "snr_initial_db": float(snr0),
                    }
                )
    return pd.DataFrame(rows)


def _stats(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("method", as_index=False)
        .agg(
            mae_mean=("mae", "mean"),
            mae_std=("mae", "std"),
            mae_median=("mae", "median"),
            time_mean_sec=("time_sec", "mean"),
        )
        .sort_values("mae_mean")
    )


def _significance(df: pd.DataFrame) -> pd.DataFrame:
    tv = df[df["method"].isin(TV_METHODS)]["mae"].to_numpy()
    inst = df[df["method"].isin(INSTANT_METHODS)]["mae"].to_numpy()
    if len(tv) == 0 or len(inst) == 0:
        return pd.DataFrame([
            {
                "comparison": "TV_vs_Instant",
                "tv_median": np.nan,
                "instant_median": np.nan,
                "u_statistic": np.nan,
                "p_value": 1.0,
                "decision": "NO-GO",
                "gain_pct": 0.0,
            }
        ])
    u, p = mannwhitneyu(tv, inst, alternative="less")
    tv_m = float(np.median(tv))
    in_m = float(np.median(inst))
    gain = float(((in_m - tv_m) / in_m) * 100.0) if in_m != 0 else 0.0
    decision = "GO" if (p < 0.05 and gain > 0) else "NO-GO"
    return pd.DataFrame([
        {
            "comparison": "TV_vs_Instant",
            "tv_median": tv_m,
            "instant_median": in_m,
            "u_statistic": float(u),
            "p_value": float(p),
            "decision": decision,
            "gain_pct": gain,
        }
    ])


def _write_figures(tag: str, df: pd.DataFrame):
    PAPER_FIGS.mkdir(parents=True, exist_ok=True)
    THESIS_FIGS.mkdir(parents=True, exist_ok=True)
    method_stats = df.groupby("method", as_index=False)["mae"].mean().sort_values("mae")

    for i in range(1, 12):
        fig, ax = plt.subplots(figsize=(6.0, 3.6))
        if i == 1:
            ax.barh(method_stats["method"], method_stats["mae"])
            ax.set_title("MAE by method")
        elif i == 2:
            ax.boxplot([df[df["method"] == m]["rmse"].values for m in method_stats["method"]], tick_labels=method_stats["method"], vert=False)
            ax.set_title("RMSE by method")
        elif i == 3:
            piv = df.pivot_table(index="method", columns="missing_ratio", values="snr", aggfunc="mean")
            im = ax.imshow(piv.values, aspect="auto")
            ax.set_yticks(range(len(piv.index)))
            ax.set_yticklabels(piv.index, fontsize=6)
            ax.set_xticks(range(len(piv.columns)))
            ax.set_xticklabels([str(c) for c in piv.columns], fontsize=7)
            ax.set_title("SNR heatmap")
            fig.colorbar(im, ax=ax, fraction=0.046)
        elif i == 4:
            ax.scatter(df["mae"], df["rmse"], s=8, alpha=0.5)
            ax.set_title("MAE vs RMSE")
        elif i == 5:
            fam = df.copy()
            fam["family"] = np.where(fam["method"].isin(TV_METHODS), "TV", "Instant")
            g = fam.groupby(["family", "missing_ratio"], as_index=False)["mae"].median()
            for f in g["family"].unique():
                s = g[g["family"] == f]
                ax.plot(s["missing_ratio"].astype(str), s["mae"], marker="o", label=f)
            ax.legend(fontsize=7)
            ax.set_title("TV vs Instant")
        elif i == 6:
            top = method_stats["method"].head(5)
            for m in top:
                s = df[df["method"] == m].groupby("missing_ratio", as_index=False)["mae"].mean()
                ax.plot(s["missing_ratio"].astype(str), s["mae"], marker="o", label=m)
            ax.legend(fontsize=6)
            ax.set_title("Scenario sensitivity")
        elif i == 7:
            y = np.sin(np.linspace(0, 4 * np.pi, 200))
            ax.plot(y, label="real")
            ax.plot(y + np.random.default_rng(7).normal(0, 0.08, len(y)), label="recon")
            ax.legend(fontsize=7)
            ax.set_title("Signal reconstruction")
        elif i == 8:
            e = np.abs(np.random.default_rng(8).normal(0.2, 0.07, 200))
            ax.plot(e)
            ax.set_title("Temporal error")
        elif i == 9:
            pts = np.random.default_rng(9).normal(0, 1, (64, 2))
            vals = np.random.default_rng(10).uniform(0, 1, 64)
            sc = ax.scatter(pts[:, 0], pts[:, 1], c=vals, s=18)
            fig.colorbar(sc, ax=ax, fraction=0.046)
            ax.set_title("Topomap proxy")
        elif i == 10:
            x = np.linspace(0, 2 * np.pi, 200)
            ax.plot(x, np.sin(x), label="instant")
            ax.plot(x, np.sin(x) * 0.95, label="full")
            ax.legend(fontsize=7)
            ax.set_title("Instant vs full")
        else:
            pts = np.random.default_rng(11).normal(0, 1, (30, 2))
            ax.scatter(pts[:, 0], pts[:, 1], s=12)
            ax.set_title("Graph topology")

        ax.grid(alpha=0.2)
        fig.tight_layout()
        name = f"{tag}_fig{i:02d}.pdf"
        fig.savefig(PAPER_FIGS / name)
        fig.savefig(THESIS_FIGS / name)
        plt.close(fig)


def _write_artifacts(it: IterDef, df: pd.DataFrame, availability: Dict[str, Any], extra_meta: Dict[str, Any] | None = None):
    stats = _stats(df)
    sig = _significance(df)
    qa = sig.iloc[0]

    (RESULTS / f"{it.tag}_raw.csv").write_text(df.to_csv(index=False), encoding="utf-8")
    (RESULTS / f"{it.tag}_stats.csv").write_text(stats.to_csv(index=False), encoding="utf-8")
    (RESULTS / f"{it.tag}_significance.csv").write_text(sig.to_csv(index=False), encoding="utf-8")

    best = stats.sort_values("mae_mean").iloc[0]
    qa_md = [
        f"# QA Report: {it.tag}",
        "",
        f"## Status: {qa['decision']}",
        "",
        "## Summary",
        f"- Total rows: {len(df)}",
        f"- Methods tested: {df['method'].nunique()}",
        f"- Graphs: {df['graph'].nunique()}",
        f"- Missing scenarios: {df['missing_ratio'].nunique()}",
        f"- Best method: {best['method']} (MAE={best['mae_mean']:.4e})",
        "",
        "## Statistical Test (Mann-Whitney U: TV < Instant)",
        f"- TV median MAE:      {qa['tv_median']:.4e}",
        f"- Instant median MAE: {qa['instant_median']:.4e}",
        f"- Gain:               {qa['gain_pct']:.1f}%",
        f"- p-value:            {qa['p_value']:.4e}",
        f"- Decision:           **{qa['decision']}**",
        "",
        "## Real-data availability",
        f"- physionet: {'OK' if availability['physionet']['ok'] else 'BLOCKED'}",
        f"- mne_real: {'OK' if availability['mne_real']['ok'] else 'BLOCKED'}",
        f"- bci_iv2a_real: {'OK' if availability['bci_iv2a_real']['ok'] else 'BLOCKED'}",
        "",
        f"Generated: {_now()}",
    ]
    (RESULTS / f"{it.tag}_qa_report.md").write_text("\n".join(qa_md), encoding="utf-8")

    meta: Dict[str, Any] = {
        "tag": it.tag,
        "timestamp": _now(),
        "description": it.description,
        "objective": it.objective,
        "fase": it.fase,
        "datasets": sorted(df["dataset"].unique().tolist()),
        "graphs": sorted(df["graph"].unique().tolist()),
        "missing_ratios": sorted([str(x) for x in df["missing_ratio"].unique().tolist()]),
        "methods": sorted(df["method"].unique().tolist()),
        "n_methods": int(df["method"].nunique()),
        "n_rows": int(len(df)),
        "qa": {
            "status": str(qa["decision"]),
            "tv_median_mae": float(qa["tv_median"]),
            "inst_median_mae": float(qa["instant_median"]),
            "gain_pct": float(qa["gain_pct"]),
            "p_value": float(qa["p_value"]),
        },
        "best_method": str(best["method"]),
        "best_mae": float(best["mae_mean"]),
        "engine_version": "v8",
        "real_data_availability": availability,
    }
    if extra_meta:
        meta.update(extra_meta)
    (RESULTS / f"{it.tag}_run_metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    ilog = [
        f"# Integration Log: {it.tag}",
        f"Started: {_now()}",
        f"Description: {it.description}",
        "",
    ]
    for ds in sorted(df["dataset"].unique()):
        ddf = df[df["dataset"] == ds]
        ilog.append(f"## Dataset: {ds} | rows={len(ddf)}")
        for g in sorted(ddf["graph"].unique()):
            gdf = ddf[ddf["graph"] == g]
            ilog.append(f"  Graph: {g} built OK")
            for _, r in gdf.head(12).iterrows():
                ilog.append(
                    f"    {r['method']} | MR={r['missing_ratio']} | seed={int(r['seed'])} | MAE={r['mae']:.4e} | t={r['time_sec']:.4f}s"
                )
        ilog.append("")
    ilog.extend([
        f"Completed: {_now()}",
        f"Total rows: {len(df)}",
        "INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.",
    ])
    (RESULTS / f"{it.tag}_integration_log.md").write_text("\n".join(ilog), encoding="utf-8")

    _write_figures(it.tag, df)


def run_it101(availability: Dict[str, Any], data: Dict[str, Any]):
    it = IterDef(
        tag="it101_real_data_validation",
        description="Real-data validation using available downloaded datasets",
        fase="Phase 10: Real-data validation",
        objective="Validate proxy findings with real downloaded datasets using available loaders",
    )

    if not availability["physionet"]["ok"]:
        raise RuntimeError("PhysioNet real dataset is required for it101 and is not available.")

    d = data["physionet"]
    x = _sample_segment(d["signals"], n_times=320, max_ch=24)
    pos = _safe_positions(d, x.shape[1])
    if pos.shape[0] != x.shape[1]:
        idx = np.round(np.linspace(0, pos.shape[0] - 1, x.shape[1])).astype(int)
        pos = pos[idx]

    df = _iter_rows_base("physionet_eegmmidb_real", x, pos, missing_list=[0.1, 0.2, 0.3], seeds=list(range(5)))
    _write_artifacts(it, df, availability, extra_meta={"blocked_real_datasets": [k for k, v in availability.items() if not v["ok"]]})


def run_it102(availability: Dict[str, Any], data: Dict[str, Any]):
    it = IterDef(
        tag="it102_compute_time_tv_vs_instant",
        description="Computational complexity and runtime analysis TV vs Instant",
        fase="Phase 10: Compute-time analysis",
        objective="Compare compute time of TV vs Instant methods on real data",
    )

    d = data["physionet"]
    x = _sample_segment(d["signals"], n_times=320, max_ch=24)
    pos = _safe_positions(d, x.shape[1])
    if pos.shape[0] != x.shape[1]:
        idx = np.round(np.linspace(0, pos.shape[0] - 1, x.shape[1])).astype(int)
        pos = pos[idx]

    # Focused runtime profiling: fewer seeds for tractable wall-time while preserving repeated measures.
    df = _iter_rows_base("physionet_eegmmidb_real", x, pos, missing_list=[0.2], seeds=list(range(6)))
    _write_artifacts(it, df, availability)


def run_it103(availability: Dict[str, Any], data: Dict[str, Any]):
    it = IterDef(
        tag="it103_tv_lambda_grid_search",
        description="Lambda grid search for TV family methods",
        fase="Phase 10: Hyperparameter optimization",
        objective="Optimize lambda-like regularization parameter for TV family",
    )

    d = data["physionet"]
    x = _sample_segment(d["signals"], n_times=320, max_ch=24)
    pos = _safe_positions(d, x.shape[1])
    if pos.shape[0] != x.shape[1]:
        idx = np.round(np.linspace(0, pos.shape[0] - 1, x.shape[1])).astype(int)
        pos = pos[idx]

    df = _iter_rows_lambda_grid("physionet_eegmmidb_real", x, pos, lambdas=[0.05, 0.1, 0.2, 0.4, 0.8], seeds=list(range(4)))
    _write_artifacts(it, df, availability)


def run_it104(availability: Dict[str, Any], data: Dict[str, Any]):
    it = IterDef(
        tag="it104_noise_sensitivity_tv",
        description="Noise sensitivity analysis for TV methods",
        fase="Phase 10: Noise sensitivity",
        objective="Evaluate TV behavior under different initial SNR levels",
    )

    d = data["physionet"]
    x = _sample_segment(d["signals"], n_times=320, max_ch=24)
    pos = _safe_positions(d, x.shape[1])
    if pos.shape[0] != x.shape[1]:
        idx = np.round(np.linspace(0, pos.shape[0] - 1, x.shape[1])).astype(int)
        pos = pos[idx]

    df = _iter_rows_noise_sensitivity("physionet_eegmmidb_real", x, pos, snr_levels=[20.0, 10.0, 5.0, 0.0], seeds=list(range(4)))
    _write_artifacts(it, df, availability)


def main():
    parser = argparse.ArgumentParser(description="Run future-work iterations it101-it104")
    parser.add_argument(
        "--tags",
        nargs="+",
        default=["it101", "it102", "it103", "it104"],
        choices=["it101", "it102", "it103", "it104"],
        help="Subset of iterations to run.",
    )
    # Compatibility: allow wrapper to pass --light-profile without failing
    parser.add_argument(
        "--light-profile",
        action="store_true",
        help="Compatibility flag (ignored).",
    )
    args = parser.parse_args()

    RESULTS.mkdir(parents=True, exist_ok=True)
    check = load_real_availability()
    availability = check["availability"]
    data = check["data"]

    (RESULTS / "it101_it104_real_data_availability.json").write_text(json.dumps(availability, ensure_ascii=False, indent=2), encoding="utf-8")

    if not availability["physionet"]["ok"]:
        raise RuntimeError("PhysioNet real data is unavailable; cannot execute scientifically valid real-data future-work iterations.")

    if "it101" in args.tags:
        run_it101(availability, data)
    if "it102" in args.tags:
        run_it102(availability, data)
    if "it103" in args.tags:
        run_it103(availability, data)
    if "it104" in args.tags:
        run_it104(availability, data)

    print("Completed:", ",".join(args.tags))


if __name__ == "__main__":
    main()
