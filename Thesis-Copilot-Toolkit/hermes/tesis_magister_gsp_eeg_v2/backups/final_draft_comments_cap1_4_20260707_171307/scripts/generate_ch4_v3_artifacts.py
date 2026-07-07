#!/usr/bin/env python3
"""Generate V3 Chapter 4 tables and figures.

The V3 results chapter is descriptive rather than hypothesis-test driven. This
script uses existing CSV artifacts for summary tables/figures and regenerates a
small set of representative MNE Sample reconstructions from raw data for the
qualitative time/PSD figures.
"""
from __future__ import annotations

import ast
import json
import sys
import warnings
from dataclasses import dataclass
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mne
import numpy as np
import pandas as pd
from scipy.signal import welch

THESIS = Path(__file__).resolve().parents[1]
TOOLKIT = THESIS.parents[1]
sys.path.insert(0, str(TOOLKIT))

from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals

TABLES = THESIS / "tables"
FIGURES = THESIS / "figures"
LOGS = THESIS / "build_logs"
TABLES.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)
LOGS.mkdir(exist_ok=True)

SRC = TOOLKIT / "results" / "trss_vs_mne_bads_extensive"
ROBUST = SRC / "robust_stats"
MNE_RAW = TOOLKIT / "datasets" / "MNE-eegbci-data" / "MNE-sample-data" / "MNE-sample-data" / "MEG" / "sample" / "sample_audvis_raw.fif"

OKABE = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "red": "#D55E00",
    "purple": "#CC79A7",
    "cyan": "#56B4E9",
    "gray": "#666666",
    "black": "#111111",
}

METHOD_LABEL = {
    "mne_interpolate_bads_spline": "MNE",
    "trss_default": "TRSS fijo",
    "trss_cv_tuned_seed0": "TRSS calibrado",
    "trss_oracle_grid": "TRSS oráculo",
}

METRIC_LABEL = {
    "mae": "MAE",
    "rmse": "RMSE",
    "nrmse": "NRMSE",
    "dtw": "DTW",
    "snr": "SNR",
    "lsd": "LSD",
    "coherence_mean": "Coherencia",
    "corr_mean": "Correlación",
    "r2": "$R^2$",
    "runtime_s": "Tiempo",
}

METRIC_CATEGORY = {
    "mae": "Amplitud",
    "rmse": "Amplitud",
    "nrmse": "Amplitud",
    "dtw": "Forma",
    "snr": "Amplitud",
    "lsd": "Espectral",
    "coherence_mean": "Espectral",
    "corr_mean": "Forma",
    "r2": "Forma",
    "runtime_s": "Costo",
}

MODE_LABEL = {
    "random": "Aleatorio",
    "nearby": "Cercano",
    "edge": "Periférico",
    "high_variance": "Alta varianza",
}

DATASET_LABEL = {
    "mne_sample_w0": "MNE Sample",
    "physionet_s1_r4_w0": "PhysioNet S1",
    "physionet_s2_r4_w0": "PhysioNet S2",
    "synthetic_smooth": "Sintético suave",
    "synthetic_rough": "Sintético rugoso",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})


def tex_escape(text: str) -> str:
    repl = {
        "_": r"\_",
        "%": r"\%",
        "&": r"\&",
        "#": r"\#",
    }
    return "".join(repl.get(ch, ch) for ch in str(text))


def write(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(THESIS)}")


def pct(x: float, digits: int = 1, signed: bool = False) -> str:
    val = float(x) * 100.0
    if abs(val) < 0.5 * 10 ** (-digits):
        val = 0.0
    sign = "+" if signed and val > 0 else ""
    return f"{sign}{val:.{digits}f}"


def sci(x: float, digits: int = 2) -> str:
    x = float(x)
    if not np.isfinite(x):
        return "--"
    if x == 0:
        return "0"
    exp = int(np.floor(np.log10(abs(x))))
    mant = x / (10 ** exp)
    return f"${mant:.{digits}f}\\times 10^{{{exp}}}$"


def parse_bad_idx(raw: object) -> list[int]:
    s = str(raw).strip()
    if not s:
        return []
    if s.startswith("[") or s.startswith("("):
        try:
            val = ast.literal_eval(s)
            if isinstance(val, (list, tuple, np.ndarray)):
                return [int(v) for v in val]
            return [int(val)]
        except Exception:
            pass
    return [int(float(tok)) for tok in s.replace(",", " ").split() if tok.strip()]


def load_sources() -> dict[str, pd.DataFrame]:
    return {
        "raw": pd.read_csv(SRC / "raw_balanced.csv"),
        "derived": pd.read_csv(SRC / "derived_balanced.csv"),
        "robust": pd.read_csv(ROBUST / "robust_pairwise_summary.csv"),
        "by_dataset": pd.read_csv(ROBUST / "robust_by_dataset.csv"),
        "by_scenario": pd.read_csv(ROBUST / "robust_by_missing_scenario.csv"),
        "scenario_wr": pd.read_csv(SRC / "mae_winrate_by_scenario_balanced.csv"),
        "summary": pd.read_csv(SRC / "summary_overall_balanced.csv"),
        "ablation": pd.read_csv(TOOLKIT / "results" / "ablation_real_data_extended_results.csv"),
    }


def generate_descriptive_tables(data: dict[str, pd.DataFrame]) -> None:
    robust = data["robust"]
    summary = data["summary"]
    scenario_wr = data["scenario_wr"]
    ablation = data["ablation"]

    # Main descriptive comparison table: no p/q columns; runtime is handled in the cost section.
    metrics = ["mae", "rmse", "nrmse", "dtw", "snr", "lsd", "coherence_mean", "corr_mean", "r2"]
    main = robust.query("method_a == 'trss_default' and method_b == 'mne_interpolate_bads_spline' and metric in @metrics").copy()
    main["_order"] = main["metric"].map({m: i for i, m in enumerate(metrics)})
    main = main.sort_values("_order")
    rows = []
    for _, r in main.iterrows():
        metric = r["metric"]
        rows.append(
            f"{METRIC_CATEGORY.get(metric, '')} & {METRIC_LABEL.get(metric, metric)} & "
            f"{sci(r['b_median'])} & {sci(r['a_median'])} & "
            f"{pct(r['median_improvement'], signed=True)} & "
            f"{pct(r['win_rate'])} & "
            f"[{pct(r['boot_median_improvement_ci_low'], signed=True)}, {pct(r['boot_median_improvement_ci_high'], signed=True)}] \\\\"
        )
    write(
        TABLES / "ch4_descriptive_trss_mne.tex",
        r"""
\begin{table}[htbp]
\centering
\scriptsize
\setlength{\tabcolsep}{2pt}
\caption{Resumen descriptivo pareado de TRSS fijo frente a MNE. La mejora mediana positiva favorece a TRSS después de respetar la dirección de cada métrica. La tasa de victoria indica la proporción de pares donde TRSS supera a MNE. Los intervalos son bootstrap descriptivos al 95\%, no pruebas de hipótesis.}
\label{tab:ch4_descriptive_trss_mne}
\begin{tabular}{@{}p{1.45cm}p{1.45cm}rrrrr@{}}
\toprule
Categoría & Métrica & Med. MNE & Med. TRSS & Mej. med. (\%) & Victoria (\%) & IC descriptivo (\%) \\
\midrule
""" + "\n".join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""",
    )

    # Scenario summary table.
    sc = scenario_wr.query("method_a == 'trss_default' and method_b == 'mne_interpolate_bads_spline'").copy()
    selected = [
        ("nearby", 0.4), ("nearby", 0.3), ("edge", 0.4), ("edge", 0.1),
        ("random", 0.4), ("random", 0.1), ("high_variance", 0.4), ("nearby", 2.0),
    ]
    rows = []
    for mode, val in selected:
        sub = sc[(sc["missing_mode"] == mode) & (np.isclose(sc["missing_value"].astype(float), float(val)))]
        if sub.empty:
            continue
        r = sub.iloc[0]
        val_label = f"{int(val*100)}\\%" if val < 1 else f"{int(val)} canal(es)"
        rows.append(
            f"{MODE_LABEL.get(mode, mode)} & {val_label} & {int(r['n_pairs'])} & "
            f"{pct(r['median_rel_improve_mae'], signed=True)} & {pct(r['a_win_rate_mae'])} & "
            f"{pct(r['mean_rel_improve_mae'], signed=True)} \\\\"
        )
    write(
        TABLES / "ch4_scenario_summary_descriptive.tex",
        r"""
\begin{table}[htbp]
\centering
\small
\caption{Resumen por patrón y severidad de pérdida para MAE. Cada fila reporta la mejora mediana de TRSS frente a MNE, la tasa de victoria (proporción de pares donde TRSS obtiene menor MAE) y la mejora media como lectura complementaria.}
\label{tab:ch4_scenario_summary_descriptive}
\begin{tabular}{@{}llrrr r@{}}
\toprule
Patrón & Severidad & $n$ & Mej. med. (\%) & Victoria (\%) & Mej. media (\%) \\
\midrule
""" + "\n".join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""",
    )

    # Complexity symbols table.
    write(
        TABLES / "ch4_complexity_symbols.tex",
        r"""
\begin{table}[htbp]
\centering
\small
\caption{Símbolos usados para interpretar la complejidad computacional.}
\label{tab:ch4_complexity_symbols}
\begin{tabular}{@{}llp{6.2cm}@{}}
\toprule
Símbolo & Significado & Uso en el análisis \\
\midrule
$N$ & Número de canales EEG & Determina el tamaño del sistema espacial. \\
$T$ & Número de muestras temporales & Determina cuántas columnas/instantes se reconstruyen. \\
$E$ & Número de aristas del grafo & Controla el costo de operaciones dispersas sobre la topología espacial. \\
$K$ & Iteraciones del resolvedor & Afecta el costo de TRSS fijo para una configuración dada. \\
$H$ & Configuraciones evaluadas & Solo aplica a búsqueda/calibración de hiperparámetros, no al costo de una reconstrucción ya fijada. \\
\bottomrule
\end{tabular}
\end{table}
""",
    )

    # Temporal contribution table from ablation CSV.
    full = ablation[ablation["variant"] == "TRSS-Full"]
    no_temp = ablation[ablation["variant"] == "TRSS-NoTemporal"]
    rows = []
    for metric in ["mae", "rmse", "dtw", "lsd"]:
        if metric not in ablation.columns:
            continue
        merged = full[["iteration", "dataset", "missing_ratio", metric]].merge(
            no_temp[["iteration", "dataset", "missing_ratio", metric]],
            on=["iteration", "dataset", "missing_ratio"], suffixes=("_full", "_notemporal")
        ).dropna()
        if merged.empty:
            continue
        lower_better = metric in {"mae", "rmse", "dtw", "lsd"}
        if lower_better:
            imp = (merged[f"{metric}_notemporal"] - merged[f"{metric}_full"]) / merged[f"{metric}_notemporal"].replace(0, np.nan)
        else:
            imp = (merged[f"{metric}_full"] - merged[f"{metric}_notemporal"]) / merged[f"{metric}_notemporal"].replace(0, np.nan)
        rows.append(
            f"{METRIC_LABEL.get(metric, metric)} & {pct(np.nanmedian(imp), signed=True)} & {pct(np.nanmean(imp), signed=True)} & {pct(np.nanmean(imp > 0))} \\\\"
        )
    write(
        TABLES / "ch4_temporal_component_summary.tex",
        r"""
\begin{table}[htbp]
\centering
\small
\caption{Contribución descriptiva del término temporal dentro de TRSS. La comparación retira el término temporal y mide cuánto cambia el desempeño relativo del modelo completo.}
\label{tab:ch4_temporal_component_summary}
\begin{tabular}{@{}lrrr@{}}
\toprule
Métrica & Mej. med. (\%) & Mej. media (\%) & Victoria (\%) \\
\midrule
""" + "\n".join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""",
    )


def select_representative_cases(raw: pd.DataFrame) -> pd.DataFrame:
    use = raw[(raw["dataset"] == "mne_sample_w0") & (raw["method"].isin(["mne_interpolate_bads_spline", "trss_default"]))].copy()
    keys = ["dataset", "missing_mode", "missing_value", "seed", "bad_idx"]
    pivot = use.pivot_table(index=keys, columns="method", values=["mae", "nrmse", "lsd", "params"], aggfunc="first")
    # Flatten columns.
    pivot.columns = [f"{a}_{b}" for a, b in pivot.columns]
    pivot = pivot.reset_index().dropna(subset=["mae_mne_interpolate_bads_spline", "mae_trss_default"])
    pivot["mae_improvement"] = (pivot["mae_mne_interpolate_bads_spline"] - pivot["mae_trss_default"]) / pivot["mae_mne_interpolate_bads_spline"]
    pivot["abs_improvement"] = pivot["mae_improvement"].abs()

    selected: list[pd.Series] = []
    labels: list[str] = []
    roles: list[str] = []

    def add(role: str, label: str, row: pd.Series) -> None:
        key = tuple(row[k] for k in keys)
        if any(tuple(r[k] for k in keys) == key for r in selected):
            return
        selected.append(row)
        labels.append(label)
        roles.append(role)

    add("TRSS favorable", "Mayor mejora MAE", pivot.sort_values("mae_improvement", ascending=False).iloc[0])
    add("MNE favorable", "TRSS peor caso MAE", pivot.sort_values("mae_improvement", ascending=True).iloc[0])
    add("Empate práctico", "Mejora absoluta mínima", pivot.sort_values("abs_improvement", ascending=True).iloc[0])
    severe = pivot[(pivot["missing_mode"] == "nearby") & (np.isclose(pivot["missing_value"].astype(float), 0.4))].copy()
    if not severe.empty:
        median = severe["mae_improvement"].median()
        severe["dist_median"] = (severe["mae_improvement"] - median).abs()
        add("Pérdida cercana severa", "Escenario cercano 40\\% mediano", severe.sort_values("dist_median").iloc[0])
    random_high = pivot[(pivot["missing_mode"] == "random") & (np.isclose(pivot["missing_value"].astype(float), 0.4))].copy()
    if len(selected) < 4 and not random_high.empty:
        add("Pérdida aleatoria severa", "Escenario aleatorio 40\\%", random_high.sort_values("abs_improvement").iloc[0])

    out = pd.DataFrame(selected).reset_index(drop=True)
    out["role"] = roles
    out["selection_rule"] = labels
    out["dataset_label"] = out["dataset"].map(DATASET_LABEL).fillna(out["dataset"])
    out["missing_label"] = out["missing_mode"].map(MODE_LABEL).fillna(out["missing_mode"])
    out["bad_idx_list"] = out["bad_idx"].apply(parse_bad_idx)
    out["target_idx"] = out["bad_idx_list"].apply(lambda xs: xs[0] if xs else -1)
    out.to_csv(TABLES / "ch4_representative_cases.csv", index=False)

    rows = []
    for _, r in out.iterrows():
        sev = f"{int(float(r['missing_value'])*100)}\\%" if float(r["missing_value"]) < 1 else f"{int(float(r['missing_value']))} canal(es)"
        rows.append(
            f"{tex_escape(r['role'])} & {tex_escape(r['dataset_label'])} & {tex_escape(r['missing_label'])} & {sev} & "
            f"{int(r['seed'])} & {int(r['target_idx'])} & {pct(r['mae_improvement'], signed=True)} & {tex_escape(r['selection_rule'])} \\\\"
        )
    write(
        TABLES / "ch4_representative_cases.tex",
        r"""
\begin{table}[htbp]
\centering
\scriptsize
\setlength{\tabcolsep}{2pt}
\caption{Casos representativos seleccionados de forma reproducible para inspección temporal y espectral. La mejora se calcula en MAE para TRSS fijo frente a MNE; valores negativos indican que MNE fue mejor en ese caso.}
\label{tab:ch4_representative_cases}
\begin{tabular}{@{}p{2.0cm}p{1.45cm}p{1.35cm}p{1.25cm}ccrp{2.2cm}@{}}
\toprule
Rol & Dataset & Patrón & Severidad & Semilla & Canal & Mej. MAE (\%) & Regla \\
\midrule
""" + "\n".join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""",
    )
    return out


def generate_metric_profile(data: dict[str, pd.DataFrame]) -> None:
    robust = data["robust"]
    metrics = ["mae", "rmse", "nrmse", "dtw", "snr", "lsd", "coherence_mean", "corr_mean", "r2", "runtime_s"]
    df = robust.query("method_a == 'trss_default' and method_b == 'mne_interpolate_bads_spline' and metric in @metrics").copy()
    df["order"] = df["metric"].map({m: i for i, m in enumerate(metrics)})
    df = df.sort_values("order")
    quality = df[df["metric"] != "runtime_s"].copy()
    vals = quality["median_improvement"].to_numpy() * 100
    labels = [METRIC_LABEL[m] for m in quality["metric"]]
    colors = [OKABE["blue"] if v >= 0 else OKABE["orange"] for v in vals]
    fig, ax = plt.subplots(figsize=(6.7, 3.15), constrained_layout=True)
    y = np.arange(len(vals))
    ax.barh(y, vals, color=colors, alpha=0.9)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("Mejora mediana (%)")
    ax.set_title("Calidad de reconstrucción")
    ax.grid(axis="x", color="#dddddd", lw=0.55)
    ax.set_xlim(min(-8, np.nanmin(vals)-5), max(22, np.nanmax(vals)+8))
    for yy, v in zip(y, vals):
        ha = "left" if v >= 0 else "right"
        dx = 0.6 if v >= 0 else -0.6
        ax.text(v + dx, yy, f"{v:+.1f}%", ha=ha, va="center", fontsize=7.4)

    fig.savefig(FIGURES / "ch4_metric_profile_descriptive.pdf", bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


def generate_scenario_summary_figure(data: dict[str, pd.DataFrame]) -> None:
    sc = data["scenario_wr"].query("method_a == 'trss_default' and method_b == 'mne_interpolate_bads_spline'").copy()
    modes = ["nearby", "edge", "random", "high_variance"]
    values = sorted(sc["missing_value"].astype(float).unique())
    # Keep common ordered values for readability.
    ordered_values = [v for v in [0.1, 0.3, 0.4, 1.0, 2.0] if any(np.isclose(values, v))]
    mat = np.full((len(modes), len(ordered_values)), np.nan)
    text = [["" for _ in ordered_values] for _ in modes]
    for i, mode in enumerate(modes):
        for j, val in enumerate(ordered_values):
            row = sc[(sc["missing_mode"] == mode) & (np.isclose(sc["missing_value"].astype(float), val))]
            if row.empty:
                continue
            r = row.iloc[0]
            imp = float(r["median_rel_improve_mae"]) * 100
            wr = float(r["a_win_rate_mae"]) * 100
            n = int(r["n_pairs"])
            mat[i, j] = imp
            text[i][j] = f"{imp:+.1f}%\nWR {wr:.0f}%\nn={n}"
    fig, ax = plt.subplots(figsize=(7.1, 3.5), constrained_layout=True)
    im = ax.imshow(mat, cmap="YlGnBu", vmin=0, vmax=45)
    ax.set_yticks(np.arange(len(modes)))
    ax.set_yticklabels([MODE_LABEL.get(m, m) for m in modes])
    ax.set_xticks(np.arange(len(ordered_values)))
    xlabels = [f"{int(v*100)}%" if v < 1 else f"{int(v)} canal" for v in ordered_values]
    ax.set_xticklabels(xlabels)
    ax.set_xlabel("Severidad de pérdida")
    ax.set_title("Escenarios de pérdida: mejora MAE y tasa de victoria")
    for i in range(len(modes)):
        for j in range(len(ordered_values)):
            if text[i][j]:
                ax.text(j, i, text[i][j], ha="center", va="center", fontsize=7.5, color="black")
    cbar = fig.colorbar(im, ax=ax, shrink=0.88)
    cbar.set_label("Mejora mediana MAE (%)")
    fig.savefig(FIGURES / "ch4_scenario_summary_descriptive.pdf", bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


def generate_temporal_component_figure(data: dict[str, pd.DataFrame]) -> None:
    ablation = data["ablation"]
    full = ablation[ablation["variant"] == "TRSS-Full"]
    no_temp = ablation[ablation["variant"] == "TRSS-NoTemporal"]
    metrics = ["mae", "rmse", "dtw", "lsd"]
    vals = []
    labels = []
    for metric in metrics:
        merged = full[["iteration", "dataset", "missing_ratio", metric]].merge(
            no_temp[["iteration", "dataset", "missing_ratio", metric]],
            on=["iteration", "dataset", "missing_ratio"], suffixes=("_full", "_notemporal")
        ).dropna()
        if merged.empty:
            continue
        imp = (merged[f"{metric}_notemporal"] - merged[f"{metric}_full"]) / merged[f"{metric}_notemporal"].replace(0, np.nan)
        vals.append(np.nanmedian(imp)*100)
        labels.append(METRIC_LABEL.get(metric, metric))
    fig, ax = plt.subplots(figsize=(5.6, 2.8), constrained_layout=True)
    colors = [OKABE["blue"] if v >= 0 else OKABE["orange"] for v in vals]
    ax.bar(labels, vals, color=colors, alpha=0.9)
    ax.axhline(0, color="black", lw=0.8)
    ax.set_ylabel("Mejora mediana (%)")
    ax.set_title("Aporte descriptivo del término temporal")
    ax.grid(axis="y", color="#dddddd", lw=0.55)
    if vals:
        pad = max(abs(float(v)) for v in vals) * 0.22
        ax.set_ylim(min(0, min(vals) - pad), max(vals) + pad)
    for x, v in enumerate(vals):
        ax.text(x, v + (0.25 if v >= 0 else -0.25), f"{v:+.1f}%", ha="center", va="bottom" if v >= 0 else "top", fontsize=8)
    fig.savefig(FIGURES / "ch4_temporal_component_contribution.pdf", bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


def generate_decision_figure() -> None:
    rows = [
        ("Pérdida cercana severa", "TRSS", "regularidad temporal"),
        ("Pérdida periférica alta", "TRSS", "vecindario local insuficiente"),
        ("Señal suave / baja pérdida", "MNE", "prior espacial suficiente"),
        ("Procesamiento masivo", "MNE", "menor costo"),
        ("Análisis offline difícil", "TRSS posible", "mejor reconstrucción"),
    ]
    fig, ax = plt.subplots(figsize=(7.1, 2.05), constrained_layout=True)
    ax.axis("off")
    ax.set_title("Frontera práctica de uso: TRSS frente a MNE", fontweight="bold", pad=8)
    y0 = 0.78
    for i, (cond, method, reason) in enumerate(rows):
        y = y0 - i*0.145
        color = OKABE["blue"] if "TRSS" in method else OKABE["green"]
        ax.text(0.02, y, cond, ha="left", va="center", fontsize=9)
        ax.text(0.48, y, method, ha="center", va="center", fontsize=9, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.25", fc=color, ec=color, alpha=0.16))
        ax.text(0.70, y, reason, ha="left", va="center", fontsize=9, color="#333333")
    ax.text(0.02, 0.91, "Condición", fontweight="bold", fontsize=9)
    ax.text(0.48, 0.91, "Decisión", fontweight="bold", fontsize=9, ha="center")
    ax.text(0.70, 0.91, "Razón", fontweight="bold", fontsize=9)
    fig.savefig(FIGURES / "ch4_decision_boundary_trss_mne.pdf", bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


@dataclass
class PreparedMNE:
    evoked: object
    positions: np.ndarray
    ch_names: list[str]
    sfreq: float
    adjacency: np.ndarray


def prepare_mne_sample() -> PreparedMNE:
    if not MNE_RAW.exists():
        raise FileNotFoundError(MNE_RAW)
    raw = mne.io.read_raw_fif(MNE_RAW, preload=True, verbose=False)
    raw.filter(1, 30, picks="eeg", fir_design="firwin", verbose=False)
    events = mne.find_events(raw, stim_channel="STI 014", verbose=False)
    picks = mne.pick_types(raw.info, meg=False, eeg=True, eog=False, stim=False, exclude=[])
    epochs = mne.Epochs(raw, events, {"Auditivo izquierdo": 1}, tmin=-0.2, tmax=0.5,
                        picks=picks, baseline=(None, 0), preload=True, verbose=False)
    evoked = epochs.average()
    positions = np.array([ch["loc"][:3] for ch in evoked.info["chs"]], dtype=float)
    # Replace non-finite positions with zero-centered fallback if needed.
    finite = np.isfinite(positions).all(axis=1)
    if not finite.all():
        positions[~finite] = 0.0
    graph = build_graph("knng", positions, k=4, sigma=1.0)
    adj = graph["adjacency"].toarray() if hasattr(graph["adjacency"], "toarray") else np.asarray(graph["adjacency"])
    return PreparedMNE(evoked=evoked, positions=positions, ch_names=evoked.ch_names, sfreq=float(evoked.info["sfreq"]), adjacency=adj)


def reconstruct_case(prep: PreparedMNE, case: pd.Series) -> dict[str, np.ndarray | str | int | float]:
    bad_idx = [idx for idx in parse_bad_idx(case["bad_idx"]) if 0 <= idx < len(prep.ch_names)]
    if not bad_idx:
        bad_idx = [int(case.get("target_idx", 0))]
    target = bad_idx[0]
    bad_names = [prep.ch_names[i] for i in bad_idx]

    evoked_mne = prep.evoked.copy()
    evoked_mne.info["bads"] = bad_names
    try:
        evoked_mne.interpolate_bads(reset_bads=False, method=dict(eeg="spline"), origin="auto", verbose=False)
    except Exception:
        evoked_mne.interpolate_bads(reset_bads=False, method="spline", origin="auto", verbose=False)

    data_missing = prep.evoked.data.T.copy()
    data_missing[:, bad_idx] = np.nan
    params = json.loads(case.get("params_trss_default", "{}")) if isinstance(case.get("params_trss_default", "{}"), str) else {}
    alpha = float(params.get("alpha", 0.8))
    beta = float(params.get("beta", 0.15))
    lr = float(params.get("lr", 0.05))
    n_iter = int(params.get("n_iter", 120))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = interpolate_signals("trss", data_missing, adjacency=prep.adjacency, alpha=alpha, beta=beta, lr=lr, n_iter=n_iter)
    trss = np.asarray(res["reconstructed"]).T
    return {
        "target_idx": target,
        "target_name": prep.ch_names[target],
        "original": prep.evoked.data[target].copy(),
        "mne": evoked_mne.data[target].copy(),
        "trss": trss[target].copy(),
        "times_ms": prep.evoked.times * 1000.0,
        "sfreq": prep.sfreq,
    }


def generate_representative_signal_figures(cases: pd.DataFrame) -> None:
    prep = prepare_mne_sample()
    # Use at most four cases to keep the figure readable.
    cases = cases.head(4).copy()
    reconstructions = []
    for _, case in cases.iterrows():
        reconstructions.append((case, reconstruct_case(prep, case)))

    fig, axes = plt.subplots(len(reconstructions), 1, figsize=(7.3, 1.35*len(reconstructions)), sharex=True, constrained_layout=True)
    if len(reconstructions) == 1:
        axes = [axes]
    for ax, (case, rec) in zip(axes, reconstructions):
        times = rec["times_ms"]
        scale = 1e6
        ax.plot(times, rec["original"]*scale, color="black", lw=1.8, label="Original")
        ax.plot(times, rec["mne"]*scale, color=OKABE["green"], lw=1.4, ls="--", label="MNE")
        ax.plot(times, rec["trss"]*scale, color=OKABE["blue"], lw=1.4, ls="-.", label="TRSS")
        ax.axvline(0, color="#777777", lw=0.7, ls=":")
        ax.axhline(0, color="#BBBBBB", lw=0.5)
        sev = f"{int(float(case['missing_value'])*100)}%" if float(case["missing_value"]) < 1 else f"{int(float(case['missing_value']))} canal(es)"
        title = f"{case['role']}: {MODE_LABEL.get(case['missing_mode'], case['missing_mode'])} {sev}, canal {rec['target_name']}, ΔMAE {pct(case['mae_improvement'], signed=True)}%"
        ax.set_title(title, loc="left", fontsize=7.7)
        ax.set_ylabel("µV")
        ax.grid(True, color="#E5E5E5", lw=0.45)
    axes[-1].set_xlabel("Tiempo respecto del estímulo (ms)")
    axes[0].legend(loc="upper right", ncol=3, frameon=False)
    fig.savefig(FIGURES / "ch4_representative_timeseries.pdf", bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)

    fig, axes = plt.subplots(len(reconstructions), 1, figsize=(7.3, 1.35*len(reconstructions)), sharex=True, constrained_layout=True)
    if len(reconstructions) == 1:
        axes = [axes]
    for ax, (case, rec) in zip(axes, reconstructions):
        fs = float(rec["sfreq"])
        nperseg = min(256, len(rec["original"]))
        for label, key, color, style in [
            ("Original", "original", "black", "-"),
            ("MNE", "mne", OKABE["green"], "--"),
            ("TRSS", "trss", OKABE["blue"], "-."),
        ]:
            f, pxx = welch(np.asarray(rec[key], dtype=float), fs=fs, nperseg=nperseg, noverlap=nperseg//2)
            mask = f <= 45
            ax.semilogy(f[mask], pxx[mask], color=color, ls=style, lw=1.4, label=label)
        sev = f"{int(float(case['missing_value'])*100)}%" if float(case["missing_value"]) < 1 else f"{int(float(case['missing_value']))} canal(es)"
        ax.set_title(f"{case['role']}: {MODE_LABEL.get(case['missing_mode'], case['missing_mode'])} {sev}", loc="left", fontsize=7.7)
        ax.set_ylabel("PSD")
        ax.grid(True, which="both", color="#E5E5E5", lw=0.45)
    axes[-1].set_xlabel("Frecuencia (Hz)")
    axes[0].legend(loc="upper right", ncol=3, frameon=False)
    fig.savefig(FIGURES / "ch4_psd_original_vs_interpolated.pdf", bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


def main() -> None:
    data = load_sources()
    generate_descriptive_tables(data)
    cases = select_representative_cases(data["raw"])
    generate_metric_profile(data)
    generate_scenario_summary_figure(data)
    generate_temporal_component_figure(data)
    generate_decision_figure()
    generate_representative_signal_figures(cases)
    manifest = {
        "tables": [
            "ch4_descriptive_trss_mne.tex",
            "ch4_scenario_summary_descriptive.tex",
            "ch4_complexity_symbols.tex",
            "ch4_temporal_component_summary.tex",
            "ch4_representative_cases.tex",
            "ch4_representative_cases.csv",
        ],
        "figures": [
            "ch4_metric_profile_descriptive.pdf",
            "ch4_scenario_summary_descriptive.pdf",
            "ch4_temporal_component_contribution.pdf",
            "ch4_decision_boundary_trss_mne.pdf",
            "ch4_representative_timeseries.pdf",
            "ch4_psd_original_vs_interpolated.pdf",
        ],
    }
    write(LOGS / "cap4_v3_artifacts_manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
