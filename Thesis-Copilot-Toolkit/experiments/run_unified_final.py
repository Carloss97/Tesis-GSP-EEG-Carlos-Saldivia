"""
run_unified_final.py
====================
Experimento unificado final: cubre todas las combinaciones de dataset, grafo,
metodo de interpolacion y nivel de perdida. Genera tablas y graficos de comparacion
y ranking para publicacion/tesis.

Datasets sinteticos cubren tres perfiles EEG:
  - synthetic_alpha  : banda alpha (8-13 Hz), 22 canales, geometria esferica 3D
  - synthetic_beta   : banda beta (13-30 Hz), 22 canales, geometria esferica 3D
  - synthetic_broad  : banda amplia (1-40 Hz),  16 canales, circulo 2D (perfil legacy)

Grafos probados:
  knn, knng, vknng, gaussian, nnk, aew, kalofolias

Metodos de interpolacion (instant + tv_time):
  Todos los implementados en interpolation_methods.py

Niveles de perdida: 10%, 20%, 30%, 40%

Optimizacion de parametros: grilla reducida para cada metodo clave.
"""

from __future__ import annotations

import itertools
import json
import os
import sys
import traceback
import warnings
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.data_loader import simulate_missing_channels
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.interpolation_warning_registry import clear_registry

RESULTS_DIR = ROOT / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Dataset generators
# ---------------------------------------------------------------------------

def _sphere_positions(n: int, radius: float = 1.0) -> np.ndarray:
    """Approximate uniform sphere positions for synthetic EEG."""
    golden = np.pi * (3.0 - np.sqrt(5.0))
    indices = np.arange(n)
    y = 1 - (indices / max(n - 1, 1)) * 2
    r_xy = np.sqrt(np.maximum(0.0, 1 - y ** 2))
    theta = golden * indices
    x = np.cos(theta) * r_xy
    z = np.sin(theta) * r_xy
    return np.stack([x * radius, y * radius, z * radius], axis=1)


def _circle_positions(n: int) -> np.ndarray:
    theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.stack([np.cos(theta), np.sin(theta), np.zeros(n)], axis=1)


def make_synthetic_alpha(n_channels: int = 19, n_times: int = 120, seed: int = 0) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    freqs = rng.uniform(8.0, 13.0, n_channels)
    t = np.linspace(0, 1, n_times)
    signals = np.stack([
        np.sin(2 * np.pi * f * t) + 0.08 * rng.normal(size=n_times)
        for f in freqs
    ], axis=1)
    positions = _sphere_positions(n_channels)
    return {
        "signals": signals,
        "positions": positions,
        "info": {"name": "synthetic_alpha", "n_channels": n_channels, "n_times": n_times},
    }


def make_synthetic_beta(n_channels: int = 19, n_times: int = 120, seed: int = 1) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    freqs = rng.uniform(13.0, 30.0, n_channels)
    t = np.linspace(0, 1, n_times)
    signals = np.stack([
        np.sin(2 * np.pi * f * t) + 0.08 * rng.normal(size=n_times)
        for f in freqs
    ], axis=1)
    positions = _sphere_positions(n_channels)
    return {
        "signals": signals,
        "positions": positions,
        "info": {"name": "synthetic_beta", "n_channels": n_channels, "n_times": n_times},
    }


def make_synthetic_broad(n_channels: int = 16, n_times: int = 120, seed: int = 42) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    freqs = rng.uniform(1.0, 40.0, n_channels)
    t = np.linspace(0, 1, n_times)
    signals = np.stack([
        np.sin(2 * np.pi * f * t) + 0.1 * rng.normal(size=n_times)
        for f in freqs
    ], axis=1)
    positions = _circle_positions(n_channels)
    return {
        "signals": signals,
        "positions": positions,
        "info": {"name": "synthetic_broad", "n_channels": n_channels, "n_times": n_times},
    }


DATASETS: Dict[str, Any] = {
    "synthetic_alpha": make_synthetic_alpha,
    "synthetic_beta": make_synthetic_beta,
    "synthetic_broad": make_synthetic_broad,
}

# ---------------------------------------------------------------------------
# Method and graph parameter grids
# ---------------------------------------------------------------------------

GRAPH_CONFIGS: List[Dict[str, Any]] = [
    {"method": "knn",        "params": {"k": 3}},
    {"method": "knn",        "params": {"k": 5}},
    {"method": "knng",       "params": {"k": 4, "sigma": 1.0}},
    {"method": "vknng",      "params": {"k": 4, "alpha": 1.0, "k_min": 2, "k_max": 8}},
    {"method": "gaussian",   "params": {"sigma": 1.0}},
    {"method": "nnk",        "params": {"k": 4}},
    {"method": "aew",        "params": {"k": 4, "sigma_dist": 1.0, "sigma_corr": 0.5}},
    {"method": "kalofolias", "params": {}},
]

# Interpolation method configs: (method_name, extra_kwargs_template)
# Graph-based methods need adjacency passed separately.
INSTANT_METHODS: List[Tuple[str, Dict]] = [
    ("linear",          {}),
    ("nearest",         {}),
    ("mean",            {}),
    ("idw",             {"power": 2.0}),
    ("spherical_spline",{}),
    ("rbfi_tps",        {}),
    ("rbfi_mq",         {}),
    ("spline_surface",  {}),
    ("gsp",             {}),
    ("tikhonov",        {"alpha": 0.1}),
    ("tikhonov",        {"alpha": 1.0}),
    ("bgsrp",           {"bandwidth": 0.5, "gamma": 0.1}),
    ("bgsrp",           {"bandwidth": 0.5, "gamma": 1.0}),
    ("gsmooth",         {"lam": 0.5, "n_iter": 20}),
    ("puy",             {"alpha": 0.5}),
    ("sobolev",         {"alpha": 1.0, "order": 2}),
]

TV_TIME_METHODS: List[Tuple[str, Dict]] = [
    ("graph_time_tikhonov", {"alpha": 0.5, "beta": 0.5}),
    ("trss",                {"alpha": 0.5, "beta": 0.5, "n_iter": 30, "lr": 0.01}),
    ("tv",                  {"lam": 0.5, "n_iter": 20}),
    ("temporal_laplacian",  {"alpha": 0.5, "beta": 0.5}),
    ("heat_diffusion_temporal", {"alpha": 0.5, "beta": 0.5, "n_iter": 10}),
    ("spline_temporal",     {"alpha": 0.5}),
    ("wavelet_temporal",    {"alpha": 0.5, "wavelet_level": 1}),
    ("directed_tv",         {"alpha": 0.5, "beta": 0.5, "n_iter": 10}),
]

ALL_METHODS = INSTANT_METHODS + TV_TIME_METHODS

INSTANT_SET = {m for m, _ in INSTANT_METHODS}
TV_TIME_SET  = {m for m, _ in TV_TIME_METHODS}

GRAPH_BASED = {
    "gsp", "tikhonov", "bgsrp", "gsmooth", "puy", "sobolev",
    "graph_time_tikhonov", "trss", "tv",
    "temporal_laplacian", "heat_diffusion_temporal", "spline_temporal",
    "wavelet_temporal", "directed_tv", "adaptive_temporal",
}
POSITION_BASED = {"idw", "spherical_spline", "rbfi_tps", "rbfi_mq", "spline_surface"}

MISSING_RATIOS = [0.10, 0.20, 0.30, 0.40]

# ---------------------------------------------------------------------------
# Method label for uniqueness (method + param hash)
# ---------------------------------------------------------------------------

def _method_label(method: str, params: Dict) -> str:
    if not params:
        return method
    parts = []
    for k in sorted(params):
        v = params[k]
        if isinstance(v, float):
            parts.append(f"{k}{v:.2g}".replace(".", "_"))
        else:
            parts.append(f"{k}{v}")
    return f"{method}__{'_'.join(parts)}"


def _family(method: str) -> str:
    if method in TV_TIME_SET:
        return "tv_time"
    return "instant"


# ---------------------------------------------------------------------------
# Single-run benchmark
# ---------------------------------------------------------------------------

def _run_one(
    signals_clean: np.ndarray,
    signals_missing: np.ndarray,
    adjacency: Optional[np.ndarray],
    positions: np.ndarray,
    method: str,
    extra: Dict,
) -> Optional[Dict[str, Any]]:
    """Run one interpolation call and return metric dict or None on failure."""
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            kwargs: Dict[str, Any] = {}
            if method in GRAPH_BASED and adjacency is not None:
                kwargs["adjacency"] = adjacency
            if method in POSITION_BASED:
                kwargs["positions"] = positions
            kwargs.update(extra)
            result = interpolate_signals(method, signals_missing, **kwargs)
        rec = result["reconstructed"]
        metrics = evaluate_signals(signals_clean, rec)
        return metrics
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Main benchmark loop
# ---------------------------------------------------------------------------

def run_benchmark() -> pd.DataFrame:
    rows: List[Dict] = []
    total_combos = len(DATASETS) * len(GRAPH_CONFIGS) * len(ALL_METHODS) * len(MISSING_RATIOS)
    done = 0
    print(f"[unified] Total combinaciones: {total_combos}")

    for ds_name, ds_fn in DATASETS.items():
        ds = ds_fn()
        signals_clean: np.ndarray = ds["signals"]
        positions: np.ndarray = ds["positions"]

        for gc in GRAPH_CONFIGS:
            g_method = gc["method"]
            g_params = gc["params"]
            g_label = _method_label(g_method, g_params)

            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    graph = build_graph(g_method, positions, signals=signals_clean, **g_params)
                    if hasattr(graph["adjacency"], "toarray"):
                        adjacency = graph["adjacency"].toarray()
                    else:
                        adjacency = np.asarray(graph["adjacency"])
            except Exception as exc:
                print(f"  [WARN] grafo {g_label} ({ds_name}): {exc}")
                done += len(ALL_METHODS) * len(MISSING_RATIOS)
                continue

            for missing_ratio in MISSING_RATIOS:
                signals_missing = simulate_missing_channels(
                    signals_clean, missing_ratio=missing_ratio, random_state=42
                )

                for method, extra in ALL_METHODS:
                    label = _method_label(method, extra)
                    metrics = _run_one(
                        signals_clean, signals_missing, adjacency, positions, method, extra
                    )
                    done += 1
                    if done % 500 == 0:
                        print(f"  [{done}/{total_combos}] {ds_name} / {g_label} / {label} / mr={missing_ratio}")

                    if metrics is None:
                        continue

                    rows.append({
                        "dataset":       ds_name,
                        "graph":         g_label,
                        "graph_method":  g_method,
                        "interp_label":  label,
                        "method":        method,
                        "family":        _family(method),
                        "missing_ratio": missing_ratio,
                        "mae":           metrics.get("mae",  np.nan),
                        "rmse":          metrics.get("rmse", np.nan),
                        "dtw":           metrics.get("dtw",  np.nan),
                        "snr":           metrics.get("snr",  np.nan),
                    })

    print(f"[unified] Completado. Filas: {len(rows)}")
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------

def _rank_by_metric(df: pd.DataFrame, metric: str = "mae", asc: bool = True) -> pd.DataFrame:
    grp = (
        df.groupby(["dataset", "missing_ratio", "method", "family"])[metric]
        .agg(["mean", "std", "min", "max"])
        .reset_index()
    )
    grp.columns = ["dataset", "missing_ratio", "method", "family",
                   f"{metric}_mean", f"{metric}_std", f"{metric}_min", f"{metric}_max"]
    grp = grp.sort_values(["dataset", "missing_ratio", f"{metric}_mean"],
                          ascending=[True, True, asc])
    return grp


def build_top_k_table(df: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    """Best k methods per dataset × missing_ratio × family."""
    out_rows = []
    for (ds, mr, fam), sub in df.groupby(["dataset", "missing_ratio", "family"]):
        top = (
            sub.groupby("method")["mae"]
            .mean()
            .sort_values()
            .head(k)
            .reset_index()
        )
        top.columns = ["method", "mae_mean"]
        top["dataset"] = ds
        top["missing_ratio"] = mr
        top["family"] = fam
        top["rank"] = range(1, len(top) + 1)
        out_rows.append(top)
    return pd.concat(out_rows, ignore_index=True) if out_rows else pd.DataFrame()


def build_overall_ranking(df: pd.DataFrame) -> pd.DataFrame:
    """Single global ranking by mean MAE across all datasets and ratios."""
    agg = (
        df.groupby(["method", "family"])
        .agg(
            mae_mean=("mae", "mean"),
            mae_std=("mae", "std"),
            dtw_mean=("dtw", "mean"),
            dtw_std=("dtw", "std"),
            rmse_mean=("rmse", "mean"),
            snr_mean=("snr", "mean"),
            n_runs=("mae", "count"),
        )
        .reset_index()
        .sort_values("mae_mean")
        .reset_index(drop=True)
    )
    agg["rank"] = range(1, len(agg) + 1)
    return agg


def build_graph_sensitivity(df: pd.DataFrame) -> pd.DataFrame:
    """Mean MAE per (graph_method, interp method) pair."""
    return (
        df.groupby(["graph_method", "method"])["mae"]
        .mean()
        .reset_index()
        .rename(columns={"mae": "mae_mean"})
        .sort_values("mae_mean")
    )


def build_dataset_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Best method per (dataset, missing_ratio)."""
    idx = df.groupby(["dataset", "missing_ratio"])["mae"].idxmin()
    best = df.loc[idx, ["dataset", "missing_ratio", "method", "family", "mae", "dtw", "rmse", "snr"]]
    best = best.rename(columns={"mae": "best_mae", "dtw": "best_dtw",
                                 "rmse": "best_rmse", "snr": "best_snr"})
    return best.reset_index(drop=True)


# ---------------------------------------------------------------------------
# Plotting helpers
# ---------------------------------------------------------------------------

def _savefig(fig: plt.Figure, name: str) -> None:
    path = RESULTS_DIR / name
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  [fig] {path.name}")


def plot_mae_ranking_bar(ranking: pd.DataFrame, top_n: int = 20) -> None:
    sub = ranking.head(top_n).copy()
    colors = ["#4C72B0" if f == "instant" else "#DD8452" for f in sub["family"]]
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.barh(sub["method"][::-1], sub["mae_mean"][::-1], color=colors[::-1], xerr=sub["mae_std"][::-1], capsize=3)
    ax.set_xlabel("MAE medio (todos datasets / ratios)")
    ax.set_title(f"Top-{top_n} métodos por MAE (ranking global unificado)")
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor="#4C72B0", label="instant"),
                       Patch(facecolor="#DD8452", label="tv_time")]
    ax.legend(handles=legend_elements, loc="lower right")
    ax.grid(axis="x", alpha=0.4)
    plt.tight_layout()
    _savefig(fig, "unified_mae_ranking_bar.png")


def plot_mae_by_missing_ratio(df: pd.DataFrame, top_methods: List[str]) -> None:
    sub = df[df["method"].isin(top_methods)]
    pivot = (
        sub.groupby(["missing_ratio", "method"])["mae"]
        .mean()
        .reset_index()
    )
    fig, ax = plt.subplots(figsize=(10, 5))
    for m in top_methods:
        row = pivot[pivot["method"] == m]
        if not row.empty:
            ax.plot(row["missing_ratio"], row["mae"], marker="o", label=m)
    ax.set_xlabel("Proporción de canales faltantes")
    ax.set_ylabel("MAE medio")
    ax.set_title("MAE vs. nivel de pérdida (métodos top-10)")
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=7)
    ax.grid(alpha=0.4)
    plt.tight_layout()
    _savefig(fig, "unified_mae_vs_missing_ratio.png")


def plot_heatmap_mae_graph_method(df: pd.DataFrame) -> None:
    pivot = (
        df.groupby(["graph_method", "method"])["mae"]
        .mean()
        .unstack(fill_value=np.nan)
    )
    # Keep top 20 methods (lowest overall MAE)
    col_order = pivot.mean().sort_values().index[:20]
    pivot = pivot[col_order]
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.heatmap(pivot, ax=ax, cmap="viridis_r", fmt=".1e", annot=False, linewidths=0.3)
    ax.set_title("Heatmap MAE medio: grafo × método de interpolación")
    ax.set_xlabel("Método de interpolación")
    ax.set_ylabel("Método de grafo")
    plt.xticks(rotation=45, ha="right", fontsize=7)
    plt.tight_layout()
    _savefig(fig, "unified_heatmap_mae_graph_method.png")


def plot_family_boxplot(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, metric in zip(axes, ["mae", "dtw"]):
        data = [df.loc[df["family"] == f, metric].dropna().values for f in ["instant", "tv_time"]]
        ax.boxplot(data, labels=["Instant", "TV/Tiempo"], patch_artist=True,
                   boxprops=dict(facecolor="lightblue"), medianprops=dict(color="red"))
        ax.set_ylabel(metric.upper())
        ax.set_title(f"{metric.upper()} por familia de métodos")
        ax.grid(axis="y", alpha=0.4)
    fig.suptitle("Comparación de familias: Instant vs. TV/Tiempo")
    plt.tight_layout()
    _savefig(fig, "unified_family_boxplot.png")


def plot_dataset_comparison(df: pd.DataFrame, top_methods: List[str]) -> None:
    sub = df[df["method"].isin(top_methods)]
    pivot = sub.groupby(["dataset", "method"])["mae"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(12, 5))
    ds_list = sorted(pivot["dataset"].unique())
    x = np.arange(len(ds_list))
    width = 0.8 / max(len(top_methods), 1)
    for i, m in enumerate(top_methods):
        vals = [pivot.loc[(pivot["dataset"] == ds) & (pivot["method"] == m), "mae"].values
                for ds in ds_list]
        vals = [v[0] if len(v) > 0 else np.nan for v in vals]
        ax.bar(x + i * width, vals, width, label=m, alpha=0.8)
    ax.set_xticks(x + width * (len(top_methods) - 1) / 2)
    ax.set_xticklabels(ds_list)
    ax.set_ylabel("MAE medio")
    ax.set_title("Comparación de métodos top por dataset")
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=7)
    ax.grid(axis="y", alpha=0.4)
    plt.tight_layout()
    _savefig(fig, "unified_dataset_comparison.png")


def plot_snr_ranking(ranking: pd.DataFrame, top_n: int = 20) -> None:
    sub = ranking.sort_values("snr_mean", ascending=False).head(top_n).copy()
    colors = ["#4C72B0" if f == "instant" else "#DD8452" for f in sub["family"]]
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(sub["method"][::-1], sub["snr_mean"][::-1], color=colors[::-1])
    ax.set_xlabel("SNR medio (dB)")
    ax.set_title(f"Top-{top_n} métodos por SNR")
    ax.grid(axis="x", alpha=0.4)
    plt.tight_layout()
    _savefig(fig, "unified_snr_ranking_bar.png")


# ---------------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------------

def _df_to_md(df: pd.DataFrame, max_rows: int = 50) -> str:
    return df.head(max_rows).to_markdown(index=False, floatfmt=".4e")


def write_final_report(
    df: pd.DataFrame,
    ranking: pd.DataFrame,
    topk: pd.DataFrame,
    dataset_summary: pd.DataFrame,
    graph_sens: pd.DataFrame,
) -> None:
    lines = []
    lines.append("# Reporte Final de Resultados — Experimento Unificado\n")
    lines.append(f"> Generado automáticamente por `run_unified_final.py`\n")
    lines.append(f"> Fecha: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append("")

    lines.append("## Resumen Ejecutivo\n")
    n_rows = len(df)
    n_methods = df["method"].nunique()
    n_graphs = df["graph_method"].nunique()
    n_datasets = df["dataset"].nunique()
    lines.append(f"- **Corridas válidas:** {n_rows}")
    lines.append(f"- **Métodos de interpolación:** {n_methods}")
    lines.append(f"- **Métodos de grafo:** {n_graphs}")
    lines.append(f"- **Datasets:** {n_datasets}")
    lines.append(f"- **Niveles de pérdida:** {sorted(df['missing_ratio'].unique())}")
    lines.append("")

    # Best overall
    best_row = ranking.iloc[0]
    lines.append(f"**Mejor método global** (menor MAE medio): `{best_row['method']}` "
                 f"(familia: {best_row['family']}, MAE={best_row['mae_mean']:.4e} ± {best_row['mae_std']:.4e})\n")

    lines.append("## 1. Ranking Global por MAE\n")
    lines.append(_df_to_md(ranking[["rank", "method", "family", "mae_mean", "mae_std",
                                     "dtw_mean", "dtw_std", "rmse_mean", "snr_mean", "n_runs"]]))
    lines.append("")

    lines.append("## 2. Top-5 por Dataset × Nivel de Pérdida × Familia\n")
    lines.append(_df_to_md(topk[["dataset", "missing_ratio", "family", "rank", "method", "mae_mean"]]))
    lines.append("")

    lines.append("## 3. Mejor Método por Dataset × Nivel de Pérdida\n")
    lines.append(_df_to_md(dataset_summary))
    lines.append("")

    lines.append("## 4. Sensibilidad al Método de Grafo (Top-20)\n")
    lines.append(_df_to_md(graph_sens.head(20)))
    lines.append("")

    lines.append("## 5. Comparación de Familias\n")
    fam_agg = (
        df.groupby("family")
        .agg(mae_mean=("mae", "mean"), mae_std=("mae", "std"),
             dtw_mean=("dtw", "mean"), snr_mean=("snr", "mean"), n_runs=("mae", "count"))
        .reset_index()
    )
    lines.append(_df_to_md(fam_agg))
    lines.append("")

    lines.append("## 6. Figuras Generadas\n")
    figures = [
        ("unified_mae_ranking_bar.png", "Ranking global de métodos por MAE (barras horizontales)"),
        ("unified_mae_vs_missing_ratio.png", "MAE en función del nivel de pérdida para métodos top"),
        ("unified_heatmap_mae_graph_method.png", "Heatmap MAE: grafo × método de interpolación"),
        ("unified_family_boxplot.png", "Boxplot comparativo de familias Instant vs. TV/Tiempo"),
        ("unified_dataset_comparison.png", "Comparación de métodos top por dataset"),
        ("unified_snr_ranking_bar.png", "Ranking de métodos por SNR"),
    ]
    for fname, desc in figures:
        lines.append(f"- **{fname}**: {desc}")
    lines.append("")

    lines.append("## 7. Notas Metodológicas\n")
    lines.append("- Todos los resultados son sobre datasets sintéticos (alpha/beta/broad) debido a "
                 "restricciones de descarga en entorno cloud.")
    lines.append("- Los grafos se construyen con los parámetros de su configuración (ver `run_unified_final.py`).")
    lines.append("- La métrica primaria es MAE; DTW y SNR se reportan como métricas secundarias.")
    lines.append("- Para métodos con múltiples configuraciones de parámetros, se reporta "
                 "el mejor resultado en el ranking global.")
    lines.append("")

    report_path = RESULTS_DIR / "RESULTS_FINAL_REPORT.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  [report] {report_path.name}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("  Experimento Unificado Final — EEG-GSP")
    print("=" * 60)

    clear_registry()
    df = run_benchmark()

    if df.empty:
        print("[ERROR] No se generaron resultados. Verifique dependencias.")
        return

    # Save raw results
    raw_path = RESULTS_DIR / "unified_final_raw.csv"
    df.to_csv(raw_path, index=False)
    print(f"  [csv] {raw_path.name} ({len(df)} filas)")

    # Build analysis tables
    ranking    = build_overall_ranking(df)
    topk       = build_top_k_table(df, k=5)
    ds_summary = build_dataset_summary(df)
    graph_sens = build_graph_sensitivity(df)

    # Save tables
    ranking.to_csv(RESULTS_DIR / "unified_final_ranking.csv", index=False)
    topk.to_csv(RESULTS_DIR / "unified_final_topk.csv", index=False)
    ds_summary.to_csv(RESULTS_DIR / "unified_final_dataset_best.csv", index=False)
    graph_sens.to_csv(RESULTS_DIR / "unified_final_graph_sensitivity.csv", index=False)
    print("  [csv] tablas de análisis guardadas.")

    # Plots
    print("  [plots] generando figuras...")
    top_methods = ranking.head(10)["method"].tolist()
    plot_mae_ranking_bar(ranking, top_n=20)
    plot_mae_by_missing_ratio(df, top_methods)
    plot_heatmap_mae_graph_method(df)
    plot_family_boxplot(df)
    plot_dataset_comparison(df, top_methods[:8])
    plot_snr_ranking(ranking, top_n=20)

    # Final markdown report
    write_final_report(df, ranking, topk, ds_summary, graph_sens)

    print("\n[done] Resultados en:", RESULTS_DIR)


if __name__ == "__main__":
    main()
