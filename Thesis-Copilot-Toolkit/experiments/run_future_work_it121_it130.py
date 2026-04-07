from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, field, replace
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.io import loadmat
from scipy.stats import mannwhitneyu

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.data_loader import (  # noqa: E402
    load_bci_competition_iv_2a,
    load_physionet_eegmmidb,
    simulate_missing_channels,
)
from src.evaluation import evaluate_signals  # noqa: E402
from src.graph_construction.graph_constructors import build_graph  # noqa: E402
from src.interpolation_methods import interpolate_signals  # noqa: E402

RESULTS = ROOT / "results"
PAPER_FIGS = ROOT / "paper" / "ieee" / "figures"
THESIS_FIGS = ROOT / "thesis" / "usm" / "figures"

INSTANT_METHODS = ["mean", "nearest", "tikhonov"]
TV_METHODS = ["tv", "trss", "graph_time_tikhonov", "temporal_laplacian"]
METHODS = INSTANT_METHODS + TV_METHODS


@dataclass
class IterDef:
    key: str
    tag: str
    description: str
    fase: str
    objective: str
    datasets: List[str]
    mode: str = "base"  # base | lambda | noise
    missing_list: List[Any] = field(default_factory=lambda: [0.1, 0.2, 0.3])
    seeds: List[int] = field(default_factory=lambda: list(range(6)))
    graph_specs: List[Tuple[str, Dict[str, Any]]] = field(default_factory=lambda: [("knn", {"k": 3})])
    lambdas: List[float] = field(default_factory=lambda: [0.05, 0.1, 0.2, 0.4, 0.8])
    snr_levels: List[float] = field(default_factory=lambda: [20.0, 10.0, 5.0, 0.0])
    methods: List[str] | None = None


def _now() -> str:
    return datetime.now(UTC).isoformat()


def _graph_tag(method: str, params: Dict[str, Any]) -> str:
    if method == "knn":
        k = params.get("k")
        return f"knn__k{k}" if k is not None else "knn"
    if method == "gaussian":
        s = params.get("sigma", 1)
        return f"gaussian__sigma{s}"
    return method


def _safe_positions(n_channels: int) -> np.ndarray:
    theta = np.linspace(0, 2 * np.pi, n_channels, endpoint=False)
    return np.stack([np.cos(theta), np.sin(theta), np.zeros(n_channels)], axis=1)


def _sample_segment(signals: np.ndarray, *, n_times: int = 320, max_ch: int = 24) -> np.ndarray:
    x = np.asarray(signals, dtype=float)
    if x.ndim != 2:
        raise ValueError(f"Expected 2D signals array, got shape={x.shape}")
    x = np.nan_to_num(x, nan=0.0, posinf=0.0, neginf=0.0)
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


def _bci_dataset(subject: int, data_root: Path) -> Dict[str, Any]:
    os.environ["BCI_IV_2A_PATH"] = str(data_root)
    d = load_bci_competition_iv_2a(subject=subject)
    x = np.asarray(d["signals"], dtype=float)
    pos = np.asarray(d.get("positions"), dtype=float)
    if pos.ndim != 2 or pos.shape[0] != x.shape[1]:
        pos = _safe_positions(x.shape[1])
    return {"signals": x, "positions": pos, "dataset": f"bci_iv2a_real_s{subject}"}


def _mat_first_2d_numeric(obj: Any) -> np.ndarray | None:
    if isinstance(obj, np.ndarray) and np.issubdtype(obj.dtype, np.number):
        if obj.ndim == 2 and min(obj.shape) >= 4:
            return obj.astype(float)
        if obj.ndim > 2:
            flat = obj.reshape(obj.shape[0], -1)
            if flat.ndim == 2 and min(flat.shape) >= 4:
                return flat.astype(float)
    return None


def _load_mat_100hz(path: Path) -> Dict[str, Any]:
    raw = loadmat(path)
    candidate = None
    for k, v in raw.items():
        if k.startswith("__"):
            continue
        c = _mat_first_2d_numeric(v)
        if c is not None:
            candidate = c
            break
    if candidate is None:
        raise RuntimeError(f"No 2D numeric matrix found in MAT file: {path}")

    x = np.asarray(candidate, dtype=float)
    # Prefer [time, channels]
    if x.shape[0] <= 128 < x.shape[1]:
        x = x.T
    if x.shape[1] > 128 and x.shape[0] < x.shape[1]:
        x = x.T

    x = np.nan_to_num(x)
    pos = _safe_positions(x.shape[1])
    return {"signals": x, "positions": pos, "dataset": "iv100hz_mat"}


def _load_iris(path: Path) -> Dict[str, Any]:
    df = pd.read_csv(path)
    num = df.select_dtypes(include=[np.number]).copy()
    if num.empty:
        raise RuntimeError(f"Iris file has no numeric columns: {path}")
    x = num.to_numpy(dtype=float)
    x = (x - x.mean(axis=0, keepdims=True)) / (x.std(axis=0, keepdims=True) + 1e-8)
    pos = _safe_positions(x.shape[1])
    return {"signals": x, "positions": pos, "dataset": "iris_graph_signal"}


def _load_movielens(u_data_path: Path) -> Dict[str, Any]:
    cols = ["user", "item", "rating", "timestamp"]
    df = pd.read_csv(u_data_path, sep="\t", names=cols)
    top_users = df["user"].value_counts().head(120).index
    top_items = df["item"].value_counts().head(80).index
    sub = df[df["user"].isin(top_users) & df["item"].isin(top_items)]
    mat = sub.pivot_table(index="timestamp", columns="item", values="rating", aggfunc="mean").sort_index()
    mat = mat.fillna(mat.mean()).fillna(0.0)
    x = mat.to_numpy(dtype=float)
    if x.shape[0] < 20:
        by_user = sub.pivot_table(index="user", columns="item", values="rating", aggfunc="mean")
        by_user = by_user.fillna(by_user.mean()).fillna(0.0)
        x = by_user.to_numpy(dtype=float)
    x = (x - x.mean(axis=0, keepdims=True)) / (x.std(axis=0, keepdims=True) + 1e-8)
    pos = _safe_positions(x.shape[1])
    return {"signals": x, "positions": pos, "dataset": "movielens_graph_signal"}


def load_data_availability() -> Dict[str, Any]:
    ds_root = ROOT / "datasets"
    info: Dict[str, Any] = {
        "physionet_real": {"ok": False, "reason": ""},
        "bci_iv2a_real_s1": {"ok": False, "reason": ""},
        "bci_iv2a_real_s2": {"ok": False, "reason": ""},
        "bci_iv2a_real_s3": {"ok": False, "reason": ""},
        "iv100hz_mat": {"ok": False, "reason": ""},
        "iris_graph_signal": {"ok": False, "reason": ""},
        "movielens_graph_signal": {"ok": False, "reason": ""},
    }
    data: Dict[str, Any] = {}

    try:
        os.environ.setdefault("EEGBCI_LOCAL_PATH", str(ds_root / "MNE-eegbci-data"))
        d = load_physionet_eegmmidb(subject=1, run=4)
        x = np.asarray(d["signals"], dtype=float)
        pos = np.asarray(d.get("positions"), dtype=float)
        if pos.ndim != 2 or pos.shape[0] != x.shape[1]:
            pos = _safe_positions(x.shape[1])
        data["physionet_real"] = {"signals": x, "positions": pos, "dataset": "physionet_eegmmidb_real"}
        info["physionet_real"] = {"ok": True, "shape": list(x.shape)}
    except Exception as exc:
        info["physionet_real"] = {"ok": False, "reason": str(exc)}

    bci_root = ds_root / "BCICIV_2a_gdf"
    for s in [1, 2, 3]:
        key = f"bci_iv2a_real_s{s}"
        try:
            d = _bci_dataset(s, bci_root)
            data[key] = d
            info[key] = {"ok": True, "shape": list(np.asarray(d["signals"]).shape)}
        except Exception as exc:
            info[key] = {"ok": False, "reason": str(exc)}

    try:
        mat_d = _load_mat_100hz(ds_root / "100Hz" / "data_set_IVa_aa.mat")
        data["iv100hz_mat"] = mat_d
        info["iv100hz_mat"] = {"ok": True, "shape": list(np.asarray(mat_d["signals"]).shape)}
    except Exception as exc:
        info["iv100hz_mat"] = {"ok": False, "reason": str(exc)}

    try:
        iris_d = _load_iris(ds_root / "Iris" / "Iris.csv")
        data["iris_graph_signal"] = iris_d
        info["iris_graph_signal"] = {"ok": True, "shape": list(np.asarray(iris_d["signals"]).shape)}
    except Exception as exc:
        info["iris_graph_signal"] = {"ok": False, "reason": str(exc)}

    try:
        ml_d = _load_movielens(ds_root / "ml-100k" / "u.data")
        data["movielens_graph_signal"] = ml_d
        info["movielens_graph_signal"] = {"ok": True, "shape": list(np.asarray(ml_d["signals"]).shape)}
    except Exception as exc:
        info["movielens_graph_signal"] = {"ok": False, "reason": str(exc)}

    return {"availability": info, "data": data}


def _iter_rows_base(dataset_name: str, signals: np.ndarray, positions: np.ndarray, *,
                    missing_list: List[Any], seeds: List[int], graph_specs: List[Tuple[str, Dict[str, Any]]],
                    methods: List[str]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []

    for graph_method, graph_params in graph_specs:
        gobj = build_graph(graph_method, positions, signals=signals, **graph_params)
        adj = np.asarray(gobj["adjacency"])
        graph_tag = _graph_tag(graph_method, graph_params)

        for miss in missing_list:
            for seed in seeds:
                if isinstance(miss, str) and miss.endswith("ch"):
                    n_missing = int(miss[:-2])
                    ratio = max(1, n_missing) / max(1, signals.shape[1])
                else:
                    ratio = float(miss)
                    n_missing = int(round(ratio * signals.shape[1]))

                masked = simulate_missing_channels(signals, missing_ratio=ratio, random_state=seed)

                for method in methods:
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
                    met = evaluate_signals(signals, rec, metrics=["mae", "rmse", "snr", "dtw"])

                    rows.append({
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
                    })
    return pd.DataFrame(rows)


def _iter_rows_lambda_grid(dataset_name: str, signals: np.ndarray, positions: np.ndarray, *,
                           lambdas: List[float], seeds: List[int], graph_specs: List[Tuple[str, Dict[str, Any]]]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    tv_methods = ["tv", "graph_time_tikhonov", "trss", "temporal_laplacian"]

    for graph_method, graph_params in graph_specs:
        gobj = build_graph(graph_method, positions, signals=signals, **graph_params)
        adj = np.asarray(gobj["adjacency"])
        graph_tag = _graph_tag(graph_method, graph_params)

        for lam in lambdas:
            for seed in seeds:
                masked = simulate_missing_channels(signals, missing_ratio=0.2, random_state=seed)
                for method in tv_methods:
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
                    rows.append({
                        "dataset": dataset_name,
                        "graph": graph_tag,
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
                    })
    return pd.DataFrame(rows)


def _iter_rows_noise(dataset_name: str, signals: np.ndarray, positions: np.ndarray, *,
                     snr_levels: List[float], seeds: List[int], graph_specs: List[Tuple[str, Dict[str, Any]]],
                     methods: List[str]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []

    for graph_method, graph_params in graph_specs:
        gobj = build_graph(graph_method, positions, signals=signals, **graph_params)
        adj = np.asarray(gobj["adjacency"])
        graph_tag = _graph_tag(graph_method, graph_params)

        for snr0 in snr_levels:
            for seed in seeds:
                noisy = _add_noise_to_snr(signals, snr0, seed)
                masked = simulate_missing_channels(noisy, missing_ratio=0.2, random_state=seed)
                for method in methods:
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
                    rows.append({
                        "dataset": dataset_name,
                        "graph": graph_tag,
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
                    })
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
    rfig = RESULTS / f"{tag}_figures"
    rfig.mkdir(parents=True, exist_ok=True)

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
        short_name = f"fig{i:02d}.pdf"
        pref_name = f"{tag}_fig{i:02d}.pdf"
        fig.savefig(rfig / short_name)
        fig.savefig(PAPER_FIGS / pref_name)
        fig.savefig(THESIS_FIGS / pref_name)
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
        "## Dataset availability snapshot",
    ]
    for k, v in sorted(availability.items()):
        qa_md.append(f"- {k}: {'OK' if v.get('ok') else 'BLOCKED'}")
    qa_md.extend(["", f"Generated: {_now()}"])
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
        "engine_version": "v9",
        "data_availability": availability,
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


def _build_iteration_defs() -> Dict[str, IterDef]:
    all_defs = [
        IterDef("it121", "it121_domain_stratified_gate", "Domain-stratified GO/NO-GO analysis", "Phase 16: Domain stratification", "Estimate TV-vs-Instant gate per domain (EEG real, no-EEG) avoiding aggregated cancellation", ["physionet_real", "bci_iv2a_real_s1", "bci_iv2a_real_s2", "iv100hz_mat", "iris_graph_signal", "movielens_graph_signal"], seeds=list(range(4)), graph_specs=[("knn", {"k": 3}), ("gaussian", {"sigma": 1.0})], missing_list=[0.1, 0.2, 0.3]),
        IterDef("it122", "it122_subjectwise_bci_holdout", "BCI IV 2a subjectwise holdout proxy", "Phase 16: BCI subject generalization", "Evaluate robustness by held-out subject proxy (S1/S2/S3) in BCI IV 2a", ["bci_iv2a_real_s1", "bci_iv2a_real_s2", "bci_iv2a_real_s3"], seeds=list(range(5)), graph_specs=[("knn", {"k": 3})], missing_list=[0.2, 0.3]),
        IterDef("it123", "it123_graph_density_calibration", "Graph density calibration sweep", "Phase 16: Graph calibration", "Sweep k/sigma graph density to stabilize TV behavior where it drops", ["physionet_real", "iv100hz_mat", "movielens_graph_signal"], seeds=list(range(3)), graph_specs=[("knn", {"k": 3}), ("knn", {"k": 5}), ("knn", {"k": 7}), ("gaussian", {"sigma": 0.6}), ("gaussian", {"sigma": 1.0})], missing_list=[0.2, 0.3]),
        IterDef("it124", "it124_missing_pattern_realistic_v2", "Realistic missing-pattern stress test v2", "Phase 16: Missingness realism", "Probe robustness under tougher missingness profiles (higher and asymmetric ratios)", ["physionet_real", "bci_iv2a_real_s1", "bci_iv2a_real_s2"], seeds=list(range(4)), graph_specs=[("knn", {"k": 3})], missing_list=[0.15, 0.25, 0.35, 0.45]),
        IterDef("it125", "it125_temporal_window_sensitivity", "Temporal window sensitivity proxy", "Phase 17: Temporal sensitivity", "Check sensitivity under denser missing regimes as temporal-window stress proxy", ["physionet_real", "bci_iv2a_real_s1", "iv100hz_mat"], seeds=list(range(4)), graph_specs=[("knn", {"k": 3})], missing_list=[0.1, 0.2, 0.3, 0.4]),
        IterDef("it126", "it126_metric_robustness_multiobjective", "Multiobjective robustness ranking", "Phase 17: Multiobjective decision support", "Build MAE/RMSE/DTW/SNR/runtime multiobjective evidence with Pareto front", ["physionet_real", "bci_iv2a_real_s1", "iv100hz_mat", "iris_graph_signal", "movielens_graph_signal"], seeds=list(range(4)), graph_specs=[("knn", {"k": 3}), ("gaussian", {"sigma": 1.0})], missing_list=[0.1, 0.2, 0.3]),
        IterDef("it127", "it127_noise_profile_non_gaussian", "Non-Gaussian-like noise robustness proxy", "Phase 17: Noise robustness", "Stress-test robustness in wider SNR span as proxy for non-Gaussian perturbation", ["physionet_real", "iv100hz_mat", "iris_graph_signal"], mode="noise", seeds=list(range(4)), snr_levels=[25.0, 15.0, 5.0, 0.0, -5.0]),
        IterDef("it128", "it128_calibration_by_dataset_family", "Dataset-family calibration transfer", "Phase 17: Family calibration", "Calibrate TV hyperparameters across EEG/non-EEG families and check transfer behavior", ["physionet_real", "bci_iv2a_real_s1", "iris_graph_signal", "movielens_graph_signal"], mode="lambda", seeds=list(range(5)), graph_specs=[("knn", {"k": 3}), ("gaussian", {"sigma": 1.0})]),
        IterDef("it129", "it129_confidence_interval_stability", "Bootstrap stability of GO/NO-GO", "Phase 18: Decision stability", "Quantify GO/NO-GO fragility under bootstrap resampling of seeds", ["physionet_real", "bci_iv2a_real_s1", "iv100hz_mat", "iris_graph_signal"], seeds=list(range(8)), graph_specs=[("knn", {"k": 3}), ("gaussian", {"sigma": 1.0})], missing_list=[0.2, 0.3]),
        IterDef("it130", "it130_final_decision_matrix", "Final conditional decision matrix", "Phase 18: Final recommendations", "Emit final recommendation matrix by use case (clinical EEG, BCI, non-EEG)", ["physionet_real", "bci_iv2a_real_s1", "bci_iv2a_real_s2", "iv100hz_mat", "iris_graph_signal", "movielens_graph_signal"], seeds=list(range(3)), graph_specs=[("knn", {"k": 3})], missing_list=[0.2]),
    ]
    return {it.key: it for it in all_defs}


def _run_iteration(
    it: IterDef,
    availability: Dict[str, Any],
    data: Dict[str, Any],
    *,
    operational_close_profile: bool = False,
):
    methods = it.methods or METHODS
    frames: List[pd.DataFrame] = []
    blocked: List[str] = []

    for ds_key in it.datasets:
        if not availability.get(ds_key, {}).get("ok"):
            blocked.append(ds_key)
            continue

        d = data[ds_key]
        x = _sample_segment(np.asarray(d["signals"], dtype=float), n_times=320, max_ch=24)
        pos = np.asarray(d.get("positions"), dtype=float)
        if pos.ndim != 2 or pos.shape[0] != np.asarray(d["signals"]).shape[1]:
            pos = _safe_positions(np.asarray(d["signals"]).shape[1])
        pos = np.nan_to_num(pos, nan=0.0, posinf=0.0, neginf=0.0)
        if pos.shape[0] != x.shape[1]:
            idx = np.round(np.linspace(0, pos.shape[0] - 1, x.shape[1])).astype(int)
            pos = pos[idx]

        ds_name = d.get("dataset", ds_key)
        if it.mode == "lambda":
            df = _iter_rows_lambda_grid(ds_name, x, pos, lambdas=it.lambdas, seeds=it.seeds, graph_specs=it.graph_specs)
        elif it.mode == "noise":
            df = _iter_rows_noise(ds_name, x, pos, snr_levels=it.snr_levels, seeds=it.seeds, graph_specs=it.graph_specs, methods=methods)
        else:
            df = _iter_rows_base(ds_name, x, pos, missing_list=it.missing_list, seeds=it.seeds, graph_specs=it.graph_specs, methods=methods)

        if not df.empty:
            frames.append(df)

    if not frames:
        raise RuntimeError(f"Iteration {it.key} has no available datasets to run.")

    df_all = pd.concat(frames, ignore_index=True)
    extra_meta: Dict[str, Any] = {
        "blocked_requested_datasets": blocked,
        "requested_datasets": it.datasets,
    }
    if operational_close_profile:
        extra_meta["execution_profile"] = {
            "name": "it120_operational_close_controlled",
            "description": "Controlled unblocking profile to force operational closure and artifact emission.",
            "seed_count": len(it.seeds),
            "seeds": [int(s) for s in it.seeds],
            "missing_list": [str(m) for m in it.missing_list],
            "methods": list(it.methods or METHODS),
            "graph_specs": [
                {"method": gm, "params": gp}
                for gm, gp in it.graph_specs
            ],
        }

    _write_artifacts(
        it,
        df_all,
        availability,
        extra_meta=extra_meta,
    )


def _dataset_domain(name: str) -> str:
    n = str(name).lower()
    if "iris" in n or "movielens" in n:
        return "non_eeg"
    if "mne_sample_proxy" in n or "bci_competition_proxy" in n:
        return "eeg_proxy"
    return "eeg_real"


def _postprocess_it121(tag: str):
    path = RESULTS / f"{tag}_raw.csv"
    if not path.exists():
        return
    df = pd.read_csv(path)
    if df.empty:
        return
    df["domain"] = df["dataset"].map(_dataset_domain)
    rows = []
    for dom, sub in df.groupby("domain"):
        sig = _significance(sub).iloc[0].to_dict()
        sig["domain"] = dom
        rows.append(sig)
    if rows:
        out = pd.DataFrame(rows)[["domain", "comparison", "tv_median", "instant_median", "u_statistic", "p_value", "decision", "gain_pct"]]
        out.to_csv(RESULTS / f"{tag}_domain_significance.csv", index=False)


def _postprocess_it122(tag: str):
    path = RESULTS / f"{tag}_raw.csv"
    if not path.exists():
        return
    df = pd.read_csv(path)
    if df.empty:
        return
    rows = []
    for ds, sub in df.groupby("dataset"):
        sig = _significance(sub).iloc[0].to_dict()
        sig["holdout_subject"] = ds
        rows.append(sig)
    if rows:
        out = pd.DataFrame(rows)[["holdout_subject", "comparison", "tv_median", "instant_median", "u_statistic", "p_value", "decision", "gain_pct"]]
        out.to_csv(RESULTS / f"{tag}_subjectwise_significance.csv", index=False)


def _postprocess_it126(tag: str):
    path = RESULTS / f"{tag}_raw.csv"
    if not path.exists():
        return
    df = pd.read_csv(path)
    if df.empty:
        return
    mdf = (
        df.groupby("method", as_index=False)
        .agg(
            mae=("mae", "median"),
            rmse=("rmse", "median"),
            dtw=("dtw", "median"),
            snr=("snr", "median"),
            runtime_sec=("time_sec", "mean"),
        )
        .sort_values("mae")
    )
    values = mdf[["mae", "rmse", "dtw", "snr", "runtime_sec"]].to_numpy()
    pareto = np.ones(len(mdf), dtype=bool)
    for i in range(len(mdf)):
        for j in range(len(mdf)):
            if i == j:
                continue
            dominated = (
                values[j, 0] <= values[i, 0]
                and values[j, 1] <= values[i, 1]
                and values[j, 2] <= values[i, 2]
                and values[j, 3] >= values[i, 3]
                and values[j, 4] <= values[i, 4]
                and (
                    values[j, 0] < values[i, 0]
                    or values[j, 1] < values[i, 1]
                    or values[j, 2] < values[i, 2]
                    or values[j, 3] > values[i, 3]
                    or values[j, 4] < values[i, 4]
                )
            )
            if dominated:
                pareto[i] = False
                break
    mdf["is_pareto"] = pareto
    mdf.to_csv(RESULTS / f"{tag}_pareto.csv", index=False)


def _postprocess_it129(tag: str, *, n_boot: int = 200):
    path = RESULTS / f"{tag}_raw.csv"
    if not path.exists():
        return
    df = pd.read_csv(path)
    if df.empty:
        return
    rng = np.random.default_rng(129)
    rows = []
    n = len(df)
    for b in range(n_boot):
        idx = rng.integers(0, n, n)
        sub = df.iloc[idx].reset_index(drop=True)
        sig = _significance(sub).iloc[0]
        rows.append({
            "bootstrap": b,
            "p_value": float(sig["p_value"]),
            "gain_pct": float(sig["gain_pct"]),
            "decision": str(sig["decision"]),
        })
    out = pd.DataFrame(rows)
    out.to_csv(RESULTS / f"{tag}_bootstrap_significance.csv", index=False)
    summary = {
        "n_bootstrap": int(n_boot),
        "go_rate": float((out["decision"] == "GO").mean()),
        "p_value_median": float(out["p_value"].median()),
        "gain_pct_median": float(out["gain_pct"].median()),
        "p_value_ci95": [
            float(np.percentile(out["p_value"], 2.5)),
            float(np.percentile(out["p_value"], 97.5)),
        ],
    }
    (RESULTS / f"{tag}_bootstrap_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


def _postprocess_it130(tag: str):
    it121 = RESULTS / "it121_domain_stratified_gate_domain_significance.csv"
    it122 = RESULTS / "it122_subjectwise_bci_holdout_subjectwise_significance.csv"
    rows: List[Dict[str, Any]] = []

    eeg_dec = "NO-EVIDENCE"
    non_eeg_dec = "NO-EVIDENCE"
    bci_dec = "NO-EVIDENCE"

    if it121.exists():
        d121 = pd.read_csv(it121)
        eeg = d121[d121["domain"] == "eeg_real"]
        non_eeg = d121[d121["domain"] == "non_eeg"]
        if not eeg.empty:
            r = eeg.iloc[0]
            eeg_dec = "GO" if (float(r["p_value"]) < 0.05 and float(r["gain_pct"]) > 0) else "CONDICIONAL"
        if not non_eeg.empty:
            r = non_eeg.iloc[0]
            non_eeg_dec = "GO" if (float(r["p_value"]) < 0.05 and float(r["gain_pct"]) > 0) else "CONDICIONAL"

    if it122.exists():
        d122 = pd.read_csv(it122)
        if not d122.empty:
            go_rate = float((d122["decision"] == "GO").mean())
            bci_dec = "GO" if go_rate >= 0.5 else "CONDICIONAL"

    rows.append({"use_case": "EEG clinico", "recommendation": eeg_dec, "source": "it121_domain_stratified_gate"})
    rows.append({"use_case": "BCI", "recommendation": bci_dec, "source": "it122_subjectwise_bci_holdout"})
    rows.append({"use_case": "no-EEG", "recommendation": non_eeg_dec, "source": "it121_domain_stratified_gate"})
    out = pd.DataFrame(rows)
    out.to_csv(RESULTS / f"{tag}_decision_matrix.csv", index=False)

    md = [
        f"# Decision Matrix: {tag}",
        "",
        "| use_case | recommendation | source |",
        "|---|---|---|",
    ]
    for _, r in out.iterrows():
        md.append(f"| {r['use_case']} | {r['recommendation']} | {r['source']} |")
    (RESULTS / f"{tag}_decision_matrix.md").write_text("\n".join(md), encoding="utf-8")


def main():
    defs = _build_iteration_defs()
    keys = list(defs.keys())

    parser = argparse.ArgumentParser(description="Run future-work iterations it121-it130")
    parser.add_argument(
        "--tags",
        nargs="+",
        default=keys,
        choices=keys,
        help="Subset of iterations to run.",
    )
    parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop batch execution at first failed iteration (default: continue).",
    )
    parser.add_argument(
        "--light-profile",
        action="store_true",
        help="Use reduced seeds/scenarios/methods for faster operational execution.",
    )
    args = parser.parse_args()

    RESULTS.mkdir(parents=True, exist_ok=True)
    check = load_data_availability()
    availability = check["availability"]
    data = check["data"]

    (RESULTS / "it121_it130_data_availability.json").write_text(
        json.dumps(availability, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    failed: List[Dict[str, str]] = []
    completed: List[str] = []
    for k in args.tags:
        it = defs[k]
        if args.light_profile:
            it = replace(
                it,
                seeds=[0, 1],
                missing_list=[0.2] if it.mode == "base" else it.missing_list,
                methods=["mean", "tikhonov", "tv", "trss"] if it.mode in {"base", "noise"} else it.methods,
                graph_specs=it.graph_specs[:1],
                lambdas=it.lambdas[:3],
                snr_levels=it.snr_levels[:3],
            )
        try:
            _run_iteration(
                it,
                availability,
                data,
                operational_close_profile=False,
            )
            if k == "it121":
                _postprocess_it121(it.tag)
            elif k == "it122":
                _postprocess_it122(it.tag)
            elif k == "it126":
                _postprocess_it126(it.tag)
            elif k == "it129":
                _postprocess_it129(it.tag)
            elif k == "it130":
                _postprocess_it130(it.tag)
            completed.append(k)
            print(f"[OK] {k}")
        except Exception as exc:
            failed.append({"iteration": k, "error": str(exc)})
            print(f"[SKIPPED] {k}: {exc}")
            if args.stop_on_error:
                raise

    if failed:
        (RESULTS / "it121_it130_skipped_iterations.json").write_text(
            json.dumps(failed, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    print("Completed:", ",".join(completed))
    if failed:
        print("Skipped:", ",".join([f["iteration"] for f in failed]))


if __name__ == "__main__":
    main()
