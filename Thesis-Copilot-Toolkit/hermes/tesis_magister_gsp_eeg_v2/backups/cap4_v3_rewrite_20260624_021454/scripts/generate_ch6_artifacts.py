#!/usr/bin/env python3
"""Generate thesis-ready Chapter 6 artifacts from repository result CSVs.

The thesis workspace remains self-contained after this script runs: selected
source CSVs are copied into tables/, LaTeX tables are regenerated, and vector
PDF figures are written into figures/.
"""
from __future__ import annotations

from pathlib import Path
import json
import shutil

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

OKABE = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "red": "#D55E00",
    "purple": "#CC79A7",
    "cyan": "#56B4E9",
    "yellow": "#F0E442",
    "black": "#000000",
    "gray": "#666666",
}

plt.rcParams.update({
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

THESIS = Path(__file__).resolve().parents[1]
TOOLKIT = THESIS.parents[1]
TABLES = THESIS / "tables"
FIGURES = THESIS / "figures"
TABLES.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)

SRC = TOOLKIT / "results" / "trss_vs_mne_bads_extensive"
ROBUST = SRC / "robust_stats"

CSV_SOURCES = {
    "ch6_summary_overall_balanced.csv": SRC / "summary_overall_balanced.csv",
    "ch6_pairwise_comparisons_balanced.csv": SRC / "pairwise_comparisons_balanced.csv",
    "ch6_robust_pairwise_summary.csv": ROBUST / "robust_pairwise_summary.csv",
    "ch6_robust_by_dataset.csv": ROBUST / "robust_by_dataset.csv",
    "ch6_robust_by_missing_scenario.csv": ROBUST / "robust_by_missing_scenario.csv",
    "ch6_mae_winrate_by_scenario_balanced.csv": SRC / "mae_winrate_by_scenario_balanced.csv",
    "ch6_ablation_real_data_extended_results.csv": TOOLKIT / "results" / "ablation_real_data_extended_results.csv",
    "ch6_phase2_microbench_latency.csv": TOOLKIT / "results" / "tablas_resumen" / "phase2_microbench_latency.csv",
}

for dst, src in CSV_SOURCES.items():
    if not src.exists():
        raise FileNotFoundError(src)
    shutil.copy2(src, TABLES / dst)

# Copy generated benchmark figures for archival consistency.
for src_name, dst_name in [
    ("nrmse_boxplot_balanced.pdf", "ch6_boxplot_nrmse_balanced.pdf"),
    ("runtime_boxplot_balanced.pdf", "ch6_boxplot_runtime_balanced.pdf"),
    ("tuned_winrate_heatmap_balanced.pdf", "ch6_heatmap_tuned_winrate_balanced.pdf"),
]:
    src = SRC / "figures" / src_name
    if src.exists():
        shutil.copy2(src, FIGURES / dst_name)

summary = pd.read_csv(TABLES / "ch6_summary_overall_balanced.csv")
robust = pd.read_csv(TABLES / "ch6_robust_pairwise_summary.csv")
by_dataset = pd.read_csv(TABLES / "ch6_robust_by_dataset.csv")
by_scenario = pd.read_csv(TABLES / "ch6_robust_by_missing_scenario.csv")
abl = pd.read_csv(TABLES / "ch6_ablation_real_data_extended_results.csv")
micro = pd.read_csv(TABLES / "ch6_phase2_microbench_latency.csv")
derived = pd.read_csv(SRC / "derived_balanced.csv")
optuna_final = pd.read_csv(TOOLKIT / "results_optuna_final" / "optuna_best_results.csv")

METHOD_LABELS = {
    "mne_interpolate_bads_spline": "MNE spline",
    "trss_default": "TRSS fijo",
    "trss_cv_tuned_seed0": "TRSS calibrado",
    "trss_oracle_grid": "TRSS oráculo",
}

METRIC_LABELS = {
    "mae": "MAE",
    "rmse": "RMSE",
    "nrmse": "NRMSE",
    "dtw": "DTW",
    "snr": "SNR",
    "lsd": "LSD",
    "corr_mean": "Correlación",
    "runtime_s": "Tiempo",
    "coherence_mean": "Coherencia",
    "r2": "$R^2$",
}


def pct(x: float, decimals: int = 1) -> str:
    return f"{100 * float(x):.{decimals}f}\\%"


def signed_pct(x: float, decimals: int = 1) -> str:
    val = 100 * float(x)
    if abs(val) < 0.5 * (10 ** -decimals):
        val = 0.0
    sign = "+" if val > 0 else ""
    return f"{sign}{val:.{decimals}f}\\%"


def pct_num(x: float, decimals: int = 1) -> str:
    return f"{100 * float(x):.{decimals}f}"


def signed_num(x: float, decimals: int = 1) -> str:
    val = 100 * float(x)
    if abs(val) < 0.5 * (10 ** -decimals):
        val = 0.0
    sign = "+" if val > 0 else ""
    return f"{sign}{val:.{decimals}f}"


def ci_num(lo: float, hi: float, decimals: int = 1) -> str:
    return f"[{signed_num(lo, decimals)}, {signed_num(hi, decimals)}]"


def sci(x: float, digits: int = 2) -> str:
    x = float(x)
    if x == 0:
        return "0"
    exp = int(np.floor(np.log10(abs(x))))
    mant = x / (10 ** exp)
    return f"${mant:.{digits}f}\\times 10^{{{exp}}}$"


def scaled_1e5(x: float, digits: int = 2) -> str:
    return f"{float(x) * 1e5:.{digits}f}"


def dec(x: float, digits: int = 3) -> str:
    return f"{float(x):.{digits}f}"


def qfmt(x: float) -> str:
    x = float(x)
    if x < 1e-3:
        exp = int(np.floor(np.log10(x)))
        mant = x / (10 ** exp)
        return f"${mant:.1f}\\times 10^{{{exp}}}$"
    return f"{x:.3f}"


def tex_table(path: Path, body: str) -> None:
    path.write_text(body.strip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Table 0: experimental phase map.
# ---------------------------------------------------------------------------
phase_strata = derived[["dataset", "missing_mode", "missing_value"]].drop_duplicates().shape[0]
phase_cases = derived[["dataset", "missing_mode", "missing_value", "seed"]].drop_duplicates().shape[0]
phase_methods = derived["method"].nunique()
phase_rows = len(derived)
phase_opt_methods = optuna_final["method"].nunique()
phase_opt_datasets = optuna_final["dataset"].nunique()
phase_opt_rows = len(optuna_final)
phase_abl_variants = abl["variant"].nunique()
phase_abl_datasets = abl["dataset"].nunique()
tex_table(
    TABLES / "ch6_phase_map.tex",
    rf"""
\begin{{table}}[htbp]
\centering
\small
\caption{{Relación entre fases experimentales y evidencia usada en los capítulos prácticos.}}
\label{{tab:ch6_phase_map}}
\begin{{tabular}}{{@{{}}p{{2.8cm}}p{{4.2cm}}p{{4.4cm}}@{{}}}}
\toprule
Fase & Alcance verificable & Uso principal \\
\midrule
Implementación y cribado & 18 métodos; {len(micro)} con microbenchmark & Cobertura metodológica y descarte inicial. \\
Optimización final & {phase_opt_methods} finalistas, {phase_opt_datasets} bases reales, {phase_opt_rows} filas & Selección de familias competitivas. \\
Confirmatoria TRSS--MNE & {phase_strata} estratos, {phase_cases} pares, {phase_methods} variantes, {phase_rows} evaluaciones & Inferencia principal de capítulos 6--8. \\
Ablación temporal & {phase_abl_variants} variantes, {phase_abl_datasets} bases, {len(abl)} evaluaciones & Aporte del término temporal. \\
\bottomrule
\end{{tabular}}
\end{{table}}
""",
)

# ---------------------------------------------------------------------------
# Objective/evidence matrix used by Chapter 8.
# ---------------------------------------------------------------------------
tex_table(
    TABLES / "ch8_objective_evidence_matrix.tex",
    r"""
\begin{table}[htbp]
\centering
\small
\caption{Matriz de cumplimiento de objetivos e hipótesis.}
\label{tab:ch8_objective_evidence}
\begin{tabular}{@{}p{2.4cm}p{5.4cm}p{3.7cm}@{}}
\toprule
Elemento & Evidencia principal & Estado \\
\midrule
Objetivo general & Benchmark GSP/TRSS contra MNE con métricas de error, morfología, espectro y tiempo. & Cumplido con conclusión condicional. \\
OE1 & Sistema modular, 18 métodos, Optuna y artefactos trazables. & Cumplido. \\
OE2 & Métricas primarias y auxiliares; análisis por base, patrón, severidad y ablación. & Cumplido; evidencia ERP es cualitativa. \\
OE3 & Tablas, figuras, CSV copiados, bitácora y validador. & Cumplido. \\
H1 & TRSS mejora MAE, NRMSE y correlación; no domina LSD ni tiempo. & Respaldada con alcance acotado. \\
H2 & MNE gana o empata en señales suaves, pocos canales y restricciones de latencia. & Respaldada como ventaja práctica. \\
\bottomrule
\end{tabular}
\end{table}
""",
)

# ---------------------------------------------------------------------------
# Table 1: overall deployable/oracle summary.
# ---------------------------------------------------------------------------
summary_order = ["mne_interpolate_bads_spline", "trss_default", "trss_cv_tuned_seed0", "trss_oracle_grid"]
summary = summary.set_index("method").loc[summary_order].reset_index()
rows = []
for _, r in summary.iterrows():
    label = METHOD_LABELS[r["method"]]
    rows.append(
        f"{label} & {sci(r['mae_median'])} & {dec(r['nrmse_mean'],3)} & {dec(r['snr_mean'],2)} & "
        f"{dec(r['lsd_mean'],3)} & {dec(r['corr_mean'],3)} & {dec(r['r2_mean'],3)} & {dec(r['runtime_s_median'],4)} \\\\"
    )
tex_table(
    TABLES / "ch6_global_summary.tex",
    r"""
\begin{table}[htbp]
\centering
\footnotesize
\caption{Resumen global del benchmark confirmatorio balanceado contra MNE-Python. Las métricas de error se calculan solo sobre canales artificialmente ocultos. El oráculo usa verdad de terreno para seleccionar hiperparámetros y se reporta únicamente como cota superior no desplegable.}
\label{tab:ch6_global_summary}
\begin{tabular}{@{}lrrrrrrr@{}}
\toprule
Método & MAE med. $\downarrow$ & NRMSE $\downarrow$ & SNR $\uparrow$ & LSD $\downarrow$ & Corr. $\uparrow$ & $R^2$ $\uparrow$ & Tiempo med. (s) $\downarrow$ \\
\midrule
""" + "\n".join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""",
)

# ---------------------------------------------------------------------------
# Table 2: robust pairwise TRSS vs MNE.
# ---------------------------------------------------------------------------
headline = robust[
    robust["method_a"].isin(["trss_default", "trss_cv_tuned_seed0"])
    & robust["method_b"].eq("mne_interpolate_bads_spline")
    & robust["metric"].isin(["mae", "nrmse", "lsd", "corr_mean", "runtime_s"])
].copy()
metric_order = {"mae": 0, "nrmse": 1, "lsd": 2, "corr_mean": 3, "runtime_s": 4}
method_order = {"trss_default": 0, "trss_cv_tuned_seed0": 1}
headline["_order"] = headline["method_a"].map(method_order) * 10 + headline["metric"].map(metric_order)
headline = headline.sort_values("_order")
rows = []
for _, r in headline.iterrows():
    rows.append(
        f"{METHOD_LABELS[r['method_a']]} & {METRIC_LABELS[r['metric']]} & "
        f"{signed_num(r['median_improvement'])} & {ci_num(r['boot_median_improvement_ci_low'], r['boot_median_improvement_ci_high'])} & "
        f"{pct_num(r['win_rate'])} & {qfmt(r['p_fdr_bh'])} & {dec(r['paired_rank_biserial'],2)} " + r"\\"
    )
tex_table(
    TABLES / "ch6_robust_main.tex",
    r"""
\begin{table}[htbp]
\centering
\footnotesize
\caption[Comparación robusta TRSS--MNE]{Comparación robusta de TRSS frente a MNE-Python. La mejora mediana positiva favorece a TRSS; en tiempo, valores negativos indican mayor costo computacional de TRSS. Los intervalos son bootstrap jerárquicos al 95\%.}
\label{tab:ch6_robust_main}
\begin{tabular}{@{}llrrrrr@{}}
\toprule
Método & Métrica & Mej. (\%) & IC95 (\%) & Victoria (\%) & $q_{BH}$ & Efecto \\
\midrule
""" + "\n".join(rows[:5]) + r"""
\addlinespace
""" + "\n".join(rows[5:]) + r"""
\bottomrule
\end{tabular}
\end{table}
""",
)

# ---------------------------------------------------------------------------
# Table 2b: complete metric portfolio for TRSS default.
# ---------------------------------------------------------------------------
portfolio_metrics = ["mae", "rmse", "nrmse", "dtw", "snr", "lsd", "coherence_mean", "corr_mean", "r2", "runtime_s"]
portfolio = robust[
    robust["method_a"].eq("trss_default")
    & robust["method_b"].eq("mne_interpolate_bads_spline")
    & robust["metric"].isin(portfolio_metrics)
].copy()
portfolio["_order"] = portfolio["metric"].map({m: i for i, m in enumerate(portfolio_metrics)})
portfolio = portfolio.sort_values("_order")
rows = []
for _, r in portfolio.iterrows():
    rows.append(
        f"{METRIC_LABELS.get(r['metric'], r['metric'])} & {signed_num(r['median_improvement'])} & "
        f"{ci_num(r['boot_median_improvement_ci_low'], r['boot_median_improvement_ci_high'])} & "
        f"{pct_num(r['win_rate'])} & {qfmt(r['p_fdr_bh'])} & {dec(r['paired_rank_biserial'],2)} " + r"\\"
    )
tex_table(
    TABLES / "ch6_metric_portfolio.tex",
    r"""
\begin{table}[htbp]
\centering
\footnotesize
\caption{Portafolio completo de métricas confirmatorias para TRSS fijo frente a MNE. La mejora mediana positiva favorece a TRSS después de ajustar la dirección de cada métrica; valores negativos favorecen a MNE.}
\label{tab:ch6_metric_portfolio}
\begin{tabular}{@{}lrrrrr@{}}
\toprule
Métrica & Mej. (\%) & IC95 (\%) & Victoria (\%) & $q_{BH}$ & Efecto \\
\midrule
""" + "\n".join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""",
)

# Visual portfolio: quality metrics and runtime are shown on separate axes so
# the runtime outlier does not collapse the quality bars. The runtime panel uses
# horizontal bars; labels are outside bars and the title contains no numeric
# annotation, avoiding the previous overlap between the title and value label.
quality_metrics = [m for m in portfolio_metrics if m != "runtime_s"]
quality = portfolio.set_index("metric").loc[quality_metrics].reset_index()
runtime_row = portfolio.set_index("metric").loc["runtime_s"]
fig, (ax, ax2) = plt.subplots(
    1, 2, figsize=(7.6, 3.75),
    gridspec_kw={"width_ratios": [3.0, 1.55], "wspace": 0.44},
    constrained_layout=True,
)
y = np.arange(len(quality))
vals = quality["median_improvement"].to_numpy() * 100
cols = [OKABE["blue"] if v >= 0 else OKABE["orange"] for v in vals]
ax.barh(y, vals, color=cols, alpha=0.9)
ax.axvline(0, color="black", lw=0.9)
ax.set_yticks(y)
ax.set_yticklabels([METRIC_LABELS[m] for m in quality["metric"]], fontsize=8.6)
ax.set_xlabel("Mejora mediana de calidad (%)")
ax.grid(axis="x", color="#dddddd", linewidth=0.6)
lo = min(-8, float(np.nanmin(vals)) - 4)
hi = max(23, float(np.nanmax(vals)) + 7)
ax.set_xlim(lo, hi)
for yy, v, win in zip(y, vals, quality["win_rate"].to_numpy()*100):
    ha = "left" if v >= 0 else "right"
    dx = 0.9 if v >= 0 else -0.9
    ax.text(v + dx, yy, f"{v:+.1f}%", va="center", ha=ha, fontsize=7.8)
ax.set_title("Métricas de calidad", fontsize=10.5, pad=8)
# Runtime panel: horizontal log-scale bars keep labels separated from title.
time_summary = summary.set_index("method").loc[["mne_interpolate_bads_spline", "trss_default"]]
rt_vals = time_summary["runtime_s_median"].to_numpy()
rt_labels = ["MNE", "TRSS"]
yp = np.arange(len(rt_vals))
ax2.barh(yp, rt_vals, color=[OKABE["green"], OKABE["blue"]], alpha=0.9, height=0.42)
ax2.set_xscale("log")
ax2.set_yticks(yp)
ax2.set_yticklabels(rt_labels, fontsize=8.8)
ax2.set_xlabel("segundos/caso", labelpad=4)
ax2.set_title("Costo temporal", fontsize=10.5, pad=10)
ax2.minorticks_off()
ax2.grid(False)
ax2.grid(axis="x", which="major", color="#dddddd", linewidth=0.55)
max_rt = float(np.nanmax(rt_vals))
min_rt = float(np.nanmin(rt_vals))
ax2.set_xlim(min_rt/1.8, max_rt*2.9)
for yy, v in zip(yp, rt_vals):
    ax2.text(v*1.18, yy, f"{v:.3f}s", ha="left", va="center", fontsize=8.0)
ratio = rt_vals[1] / rt_vals[0]
ax2.text(0.06, 0.88, f"TRSS ≈ {ratio:.1f}×", transform=ax2.transAxes,
         ha="left", va="top", fontsize=8.2, color="#555555",
         bbox=dict(facecolor="white", edgecolor="none", alpha=0.82, pad=1.6))
fig.savefig(FIGURES / "ch6_metric_portfolio_improvement.pdf", bbox_inches="tight", pad_inches=0.04)
plt.close(fig)

# ---------------------------------------------------------------------------
# Table 3: dataset-level MAE stratification.
# ---------------------------------------------------------------------------
ds = by_dataset[
    by_dataset["method"].eq("trss_default")
    & by_dataset["metric"].eq("mae")
].copy()
ds = ds.sort_values("median_improvement", ascending=False)
pretty_ds = {
    "synthetic_rough": "Sintético rugoso",
    "mne_sample_w0": "MNE Sample",
    "physionet_s1_r4_w0": "PhysioNet S1",
    "physionet_s2_r4_w0": "PhysioNet S2",
    "synthetic_smooth": "Sintético suave",
}
rows = []
for _, r in ds.iterrows():
    rows.append(
        f"{pretty_ds.get(r['dataset'], r['dataset'])} & {int(r['n'])} & {pct(r['win_rate'])} & "
        f"{signed_pct(r['median_improvement'])} & {sci(r['mne_median'])} / {sci(r['trss_median'])} \\\\"
    )
tex_table(
    TABLES / "ch6_by_dataset_mae.tex",
    r"""
\begin{table}[htbp]
\centering
\small
\caption{Estratificación por conjunto de datos para TRSS fijo frente a MNE en MAE. La ventaja no es homogénea: TRSS mejora en datos reales y en el régimen sintético rugoso, pero pierde cuando la señal sintética satisface fuertemente el supuesto de suavidad espacial.}
\label{tab:ch6_by_dataset_mae}
\begin{tabular}{@{}lrrrr@{}}
\toprule
Conjunto de datos & $n$ & Tasa victoria & Mejora mediana & MAE MNE / TRSS \\
\midrule
""" + "\n".join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""",
)

# ---------------------------------------------------------------------------
# Table 4: selected missing-scenario MAE strata.
# ---------------------------------------------------------------------------
sc = by_scenario[
    by_scenario["method"].eq("trss_default")
    & by_scenario["metric"].eq("mae")
].copy()
mode_label = {"nearby": "Cercano/agrupado", "edge": "Borde/periférico", "high_variance": "Alta varianza", "random": "Aleatorio"}
value_label = {"1": "1 canal", "2": "2 canales", "0.1": "10\\%", "0.3": "30\\%", "0.4": "40\\%"}
selected_keys = [
    ("nearby", 0.4), ("nearby", 0.3), ("edge", 0.4), ("edge", 0.1),
    ("high_variance", 0.4), ("high_variance", 0.1), ("random", 0.4), ("nearby", 2.0),
]
rows = []
for mode, val in selected_keys:
    row = sc[(sc["missing_mode"].eq(mode)) & (np.isclose(sc["missing_value"].astype(float), val))]
    if row.empty:
        continue
    r = row.iloc[0]
    rows.append(
        f"{mode_label.get(mode, mode)} & {value_label.get(str(val).rstrip('0').rstrip('.'), str(val))} & {int(r['n'])} & "
        f"{pct(r['win_rate'])} & {signed_pct(r['median_improvement'])} & {scaled_1e5(r['mne_median'])} / {scaled_1e5(r['trss_median'])} \\\\"
    )
tex_table(
    TABLES / "ch6_selected_scenarios_mae.tex",
    r"""
\begin{table}[htbp]
\centering
\footnotesize
\caption{Escenarios representativos para TRSS fijo frente a MNE en MAE. La mejora aumenta en pérdidas agrupadas o periféricas de alta severidad, mientras que escenarios de pocos canales cercanos pueden producir empate práctico.}
\label{tab:ch6_selected_scenarios_mae}
\begin{tabular}{@{}llrrrr@{}}
\toprule
Patrón & Severidad & $n$ & Victoria & Mejora & MAE MNE/TRSS ($10^{-5}$) \\
\midrule
""" + "\n".join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""",
)

# ---------------------------------------------------------------------------
# Table 5: computational complexity and observed runtime.
# ---------------------------------------------------------------------------
rob_time = headline[headline["metric"].eq("runtime_s")].set_index("method_a")
mne_time = summary.set_index("method").loc["mne_interpolate_bads_spline", "runtime_s_median"]
trss_time = summary.set_index("method").loc["trss_default", "runtime_s_median"]
trss_tuned_time = summary.set_index("method").loc["trss_cv_tuned_seed0", "runtime_s_median"]
tex_table(
    TABLES / "ch6_runtime_complexity.tex",
    rf"""
\begin{{table}}[htbp]
\centering
\small
\caption{{Complejidad computacional e implementación observada. $N$ es el número de canales, $T$ el número de muestras temporales, $E$ el número de aristas del grafo y $K$ el número de iteraciones del resolvedor.}}
\label{{tab:ch6_runtime_complexity}}
\begin{{tabular}}{{@{{}}p{{2.6cm}}p{{3.9cm}}p{{3.2cm}}r@{{}}}}
\toprule
Método & Operación dominante & Complejidad asintótica orientativa & Mediana (s/caso) \\
\midrule
MNE spline & Sistema global regularizado y aplicación a muestras & $O(N^3) + O(NT)$ & {float(mne_time):.4f} \\
TRSS fijo & Iteraciones sobre grafo espacio--temporal disperso & $O(K(ET + NT))$ & {float(trss_time):.4f} \\
TRSS calibrado & Igual a TRSS fijo más selección de hiperparámetros & $O(HK(ET + NT))$ & {float(trss_tuned_time):.4f} \\
\bottomrule
\end{{tabular}}
\end{{table}}
""",
)

# ---------------------------------------------------------------------------
# Figure 1: robust improvement with CIs.
# ---------------------------------------------------------------------------
fig_data = headline[headline["metric"].isin(["mae", "nrmse", "lsd", "corr_mean"])].copy()
fig_data["metric_label"] = fig_data["metric"].map(METRIC_LABELS)
metrics = ["mae", "nrmse", "lsd", "corr_mean"]
x = np.arange(len(metrics))
width = 0.36
fig, ax = plt.subplots(figsize=(6.6, 3.2))
for i, method in enumerate(["trss_default", "trss_cv_tuned_seed0"]):
    sub = fig_data[fig_data["method_a"].eq(method)].set_index("metric").loc[metrics]
    y = sub["median_improvement"].to_numpy() * 100
    lo = sub["boot_median_improvement_ci_low"].to_numpy() * 100
    hi = sub["boot_median_improvement_ci_high"].to_numpy() * 100
    yerr = np.vstack([y - lo, hi - y])
    ax.bar(x + (i - 0.5) * width, y, width, label=METHOD_LABELS[method], color=[OKABE["blue"], OKABE["orange"]][i], alpha=0.88)
    ax.errorbar(x + (i - 0.5) * width, y, yerr=yerr, fmt="none", ecolor="black", elinewidth=0.8, capsize=2)
ax.axhline(0, color="black", lw=0.8)
ax.set_xticks(x)
ax.set_xticklabels([METRIC_LABELS[m] for m in metrics])
ax.set_ylabel("Mejora mediana frente a MNE (%)")
ax.legend(frameon=False, ncol=2, loc="upper left")
ax.grid(axis="y", color="#dddddd", linewidth=0.6)
ax.set_ylim(min(-15, ax.get_ylim()[0]), max(24, ax.get_ylim()[1]))
fig.tight_layout()
fig.savefig(FIGURES / "ch6_robust_improvement_ci.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 2: dataset stratification for MAE.
# ---------------------------------------------------------------------------
ds_plot = ds.copy()
ds_plot["label"] = ds_plot["dataset"].map(pretty_ds).fillna(ds_plot["dataset"])
ds_plot = ds_plot.sort_values("median_improvement")
colors = [OKABE["red"] if v < 0 else OKABE["blue"] for v in ds_plot["median_improvement"]]
fig, ax = plt.subplots(figsize=(6.8, 3.2))
ypos = np.arange(len(ds_plot))
ax.barh(ypos, ds_plot["median_improvement"] * 100, color=colors, alpha=0.88)
ax.axvline(0, color="black", lw=0.8)
ax.set_yticks(ypos)
ax.set_yticklabels(ds_plot["label"])
ax.set_xlabel("Mejora mediana de MAE frente a MNE (%)")
for y, (_, r) in zip(ypos, ds_plot.iterrows()):
    xval = r["median_improvement"] * 100
    ax.text(xval + (1.4 if xval >= 0 else -1.4), y, f"{r['win_rate']*100:.0f}%", va="center", ha="left" if xval >= 0 else "right", fontsize=8)
ax.set_xlim(ds_plot["median_improvement"].min()*100 - 8, ds_plot["median_improvement"].max()*100 + 11)
ax.text(0.98, 0.04, "etiqueta = tasa de victoria", transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color=OKABE["gray"])
ax.grid(axis="x", color="#dddddd", linewidth=0.6)
fig.tight_layout()
fig.savefig(FIGURES / "ch6_dataset_mae_improvement.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 3: scenario heatmap.
# ---------------------------------------------------------------------------
heat = sc.copy()
mode_order = ["random", "nearby", "edge", "high_variance"]
val_order = [1.0, 2.0, 0.1, 0.3, 0.4]
mode_names = [mode_label[m] for m in mode_order]
val_names = ["1 canal", "2 canales", "10%", "30%", "40%"]
mat = np.full((len(mode_order), len(val_order)), np.nan)
ann_win = np.full(mat.shape, np.nan)
for i, m in enumerate(mode_order):
    for j, v in enumerate(val_order):
        row = heat[(heat["missing_mode"].eq(m)) & (np.isclose(heat["missing_value"].astype(float), v))]
        if not row.empty:
            mat[i, j] = row.iloc[0]["median_improvement"] * 100
            ann_win[i, j] = row.iloc[0]["win_rate"] * 100
fig, ax = plt.subplots(figsize=(6.9, 3.55))
max_abs = np.nanmax(np.abs(mat))
im = ax.imshow(mat, cmap="RdBu", vmin=-max_abs, vmax=max_abs, aspect="auto")
ax.set_xticks(np.arange(len(val_order)))
ax.set_xticklabels(val_names)
ax.set_yticks(np.arange(len(mode_order)))
ax.set_yticklabels(mode_names)
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        if np.isfinite(mat[i, j]):
            txt_color = "white" if abs(mat[i, j]) > 0.45 * max_abs else "black"
            ax.text(j, i, f"{mat[i,j]:+.0f}%\n{ann_win[i,j]:.0f}%", ha="center", va="center", fontsize=8.2, color=txt_color, fontweight="bold")
cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cb.set_label("Mejora mediana MAE (%)")
ax.set_xlabel("Severidad de pérdida")
ax.set_ylabel("Patrón de canales faltantes")
ax.text(0.5, -0.24, "Cada celda: primera línea = mejora mediana; segunda línea = tasa de victoria", transform=ax.transAxes, ha="center", va="top", fontsize=8.5, color=OKABE["gray"])
fig.tight_layout()
fig.savefig(FIGURES / "ch6_scenario_heatmap_mae.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 4: runtime/MAE trade-off.
# ---------------------------------------------------------------------------
plot = summary.copy()
plot["label"] = plot["method"].map(METHOD_LABELS)
fig, ax = plt.subplots(figsize=(6.4, 3.7))
colors = {
    "mne_interpolate_bads_spline": OKABE["green"],
    "trss_default": OKABE["blue"],
    "trss_cv_tuned_seed0": OKABE["orange"],
    "trss_oracle_grid": OKABE["purple"],
}
markers = {
    "mne_interpolate_bads_spline": "o",
    "trss_default": "s",
    "trss_cv_tuned_seed0": "^",
    "trss_oracle_grid": "D",
}
for _, r in plot.iterrows():
    method = r["method"]
    ax.scatter(r["runtime_s_median"], r["mae_median"] * 1e6, s=92,
               color=colors.get(method, OKABE["gray"]), marker=markers.get(method, "o"),
               edgecolor="black", linewidth=0.6, zorder=3, label=r["label"])
ax.set_xscale("log")
ax.set_xlabel("Tiempo mediano por caso (s, escala log)")
ax.set_ylabel("MAE mediana ($10^{-6}$)")
ax.set_xlim(plot["runtime_s_median"].min()*0.55, plot["runtime_s_median"].max()*1.85)
ax.set_ylim(plot["mae_median"].min()*1e6 - 0.45, plot["mae_median"].max()*1e6 + 1.0)
ax.grid(True, which="both", color="#dddddd", linewidth=0.6)
ax.legend(frameon=False, loc="upper right", fontsize=8.2)
fig.tight_layout()
fig.savefig(FIGURES / "ch6_runtime_mae_tradeoff.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 4b: clean NRMSE and runtime boxplots.
# ---------------------------------------------------------------------------
box_methods = ["mne_interpolate_bads_spline", "trss_default", "trss_cv_tuned_seed0", "trss_oracle_grid"]
box_labels = ["MNE", "TRSS fijo", "TRSS calib.", "Oráculo"]
box_df = derived[derived["method"].isin(box_methods)].copy()
box_df["method"] = pd.Categorical(box_df["method"], categories=box_methods, ordered=True)
box_df = box_df.sort_values("method")
# NRMSE
fig, ax = plt.subplots(figsize=(6.4, 3.2))
data = [box_df.loc[box_df["method"].eq(m), "nrmse"].dropna().to_numpy() for m in box_methods]
bp = ax.boxplot(data, tick_labels=box_labels, patch_artist=True, widths=0.55, showfliers=False)
for patch, color in zip(bp["boxes"], [OKABE["green"], OKABE["blue"], OKABE["orange"], OKABE["purple"]]):
    patch.set_facecolor(color); patch.set_alpha(0.35); patch.set_linewidth(1.0)
for key in ["whiskers", "caps", "medians"]:
    for line in bp[key]: line.set_linewidth(1.1)
ax.set_ylabel("NRMSE en canales ocultos")
ax.set_xlabel("Método")
ax.grid(axis="y", color="#dddddd", linewidth=0.6)
ax.text(0.98, 0.96, "menor es mejor", transform=ax.transAxes, ha="right", va="top", fontsize=8.5, color=OKABE["gray"])
fig.tight_layout()
fig.savefig(FIGURES / "ch6_boxplot_nrmse_balanced.pdf", bbox_inches="tight")
plt.close(fig)
# Runtime
fig, ax = plt.subplots(figsize=(6.4, 3.2))
data = [box_df.loc[box_df["method"].eq(m), "runtime_s"].dropna().to_numpy() for m in box_methods]
bp = ax.boxplot(data, tick_labels=box_labels, patch_artist=True, widths=0.55, showfliers=False)
for patch, color in zip(bp["boxes"], [OKABE["green"], OKABE["blue"], OKABE["orange"], OKABE["purple"]]):
    patch.set_facecolor(color); patch.set_alpha(0.35); patch.set_linewidth(1.0)
for key in ["whiskers", "caps", "medians"]:
    for line in bp[key]: line.set_linewidth(1.1)
ax.set_yscale("log")
ax.set_ylabel("Tiempo por caso (s, log)")
ax.set_xlabel("Método")
ax.grid(axis="y", which="both", color="#dddddd", linewidth=0.6)
ax.text(0.98, 0.96, "menor es mejor", transform=ax.transAxes, ha="right", va="top", fontsize=8.5, color=OKABE["gray"])
fig.tight_layout()
fig.savefig(FIGURES / "ch6_boxplot_runtime_balanced.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 5: ablation temporal term, TRSS-Full vs TRSS-NoTemporal.
# ---------------------------------------------------------------------------
idx = ["iteration", "dataset", "missing_ratio"]
full = abl[abl["variant"].eq("TRSS-Full")].set_index(idx)
no_temp = abl[abl["variant"].eq("TRSS-NoTemporal")].set_index(idx)
metrics = ["mae", "rmse", "dtw", "lsd", "snr", "coherence_mean"]
directions = {"mae": "lower", "rmse": "lower", "dtw": "lower", "lsd": "lower", "snr": "higher", "coherence_mean": "higher"}
vals, wins = [], []
for m in metrics:
    a = full[m].astype(float)
    b = no_temp[m].astype(float)
    if directions[m] == "higher":
        imp = (a - b) / b.abs()
    else:
        imp = (b - a) / b.abs()
    vals.append(float(imp.median() * 100))
    wins.append(float((imp > 0).mean() * 100))
fig, ax = plt.subplots(figsize=(6.8, 3.25))
colors = [OKABE["blue"] if v >= 0 else OKABE["red"] for v in vals]
xx = np.arange(len(metrics))
ax.bar(xx, vals, color=colors, alpha=0.88)
ax.axhline(0, color="black", lw=0.8)
ax.set_xticks(xx)
ax.set_xticklabels([METRIC_LABELS[m] for m in metrics], rotation=0)
ax.set_ylabel("Mejora mediana vs.\nsin término temporal (%)")
ax.set_ylim(min(0, min(vals)-2), max(vals)+8)
for x0, v, w in zip(xx, vals, wins):
    ax.text(x0, v + (1.0 if v >= 0 else -1.0), f"{w:.0f}%", ha="center", va="bottom" if v >= 0 else "top", fontsize=8)
ax.text(0.98, 0.96, "etiqueta = tasa de victoria", transform=ax.transAxes, ha="right", va="top", fontsize=8, color=OKABE["gray"])
ax.grid(axis="y", color="#dddddd", linewidth=0.6)
fig.tight_layout()
fig.savefig(FIGURES / "ch6_ablation_temporal_component.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Experiment log / evidence bridge.
# ---------------------------------------------------------------------------
def get_row(method: str, metric: str) -> pd.Series:
    return robust[(robust["method_a"].eq(method)) & (robust["method_b"].eq("mne_interpolate_bads_spline")) & (robust["metric"].eq(metric))].iloc[0]

mae_default = get_row("trss_default", "mae")
nrmse_default = get_row("trss_default", "nrmse")
lsd_default = get_row("trss_default", "lsd")
time_default = get_row("trss_default", "runtime_s")
mae_tuned = get_row("trss_cv_tuned_seed0", "mae")

log = f"""# Bitácora de evidencia para capítulos 6--8

## Contribución práctica en una frase
TRSS mejora la reconstrucción de canales EEG ocultos frente a la interpolación estándar de MNE en métricas de amplitud y ajuste temporal, especialmente en regímenes difíciles, pero no domina la fidelidad espectral LSD y exige mayor tiempo de cómputo.

## Benchmark confirmatorio TRSS vs MNE
- **Fuente:** `results/trss_vs_mne_bads_extensive/derived_balanced.csv` y `robust_stats/robust_pairwise_summary.csv`.
- **Tamaño:** 100 estratos, 300 casos pareados y 3300 evaluaciones crudas; 2700 de ellas corresponden a variantes TRSS de grilla o perfiles alternativos.
- **Método de referencia:** `MNE interpolate_bads(method='spline')`.
- **Resultado principal TRSS fijo:** MAE mejora mediana {mae_default['median_improvement']*100:.1f}% (IC95 {mae_default['boot_median_improvement_ci_low']*100:.1f}, {mae_default['boot_median_improvement_ci_high']*100:.1f}), tasa de victoria {mae_default['win_rate']*100:.1f}%, qBH={mae_default['p_fdr_bh']:.2e}.
- **NRMSE:** mejora mediana {nrmse_default['median_improvement']*100:.1f}%, tasa de victoria {nrmse_default['win_rate']*100:.1f}%.
- **LSD:** mejora mediana {lsd_default['median_improvement']*100:.1f}%, tasa de victoria {lsd_default['win_rate']*100:.1f}%; este resultado favorece a MNE y debe aparecer como caveat.
- **Tiempo:** mejora mediana {time_default['median_improvement']*100:.1f}%; TRSS es más lento que MNE, aunque sigue en escala sub-segundo por ventana.
- **TRSS calibrado:** MAE mejora mediana {mae_tuned['median_improvement']*100:.1f}%, tasa de victoria {mae_tuned['win_rate']*100:.1f}%; la calibración no cambia la conclusión central.

## Figuras generadas
- `figures/ch6_robust_improvement_ci.pdf`: mejoras medianas con IC95.
- `figures/ch6_dataset_mae_improvement.pdf`: heterogeneidad por conjunto de datos.
- `figures/ch6_scenario_heatmap_mae.pdf`: patrón/severidad de pérdida.
- `figures/ch6_runtime_mae_tradeoff.pdf`: compromiso precisión--tiempo.
- `figures/ch6_ablation_temporal_component.pdf`: contribución del término temporal.

## Tablas generadas
- `tables/ch6_phase_map.tex`: relación entre fase exploratoria, optimización final, confirmatoria y ablación.
- `tables/ch6_global_summary.tex`: resumen global MNE/TRSS fijo/TRSS calibrado/oráculo.
- `tables/ch6_robust_main.tex`: Wilcoxon, bootstrap y efectos para TRSS vs MNE.
- `tables/ch6_metric_portfolio.tex`: portafolio completo de métricas confirmatorias para TRSS fijo.
- `tables/ch6_by_dataset_mae.tex`: estratificación por conjunto de datos.
- `tables/ch6_selected_scenarios_mae.tex`: escenarios representativos por patrón y severidad.
- `tables/ch6_runtime_complexity.tex`: complejidad y tiempo mediano.
- `tables/ch8_objective_evidence_matrix.tex`: matriz de cumplimiento de objetivos e hipótesis.

## Decisión narrativa
Usar una conclusión condicional. TRSS se justifica cuando el objetivo es reconstrucción precisa bajo pérdida agrupada, periférica o severa; MNE sigue siendo preferible para preprocesamiento estándar rápido y para señales donde el supuesto de suavidad espacial es dominante.
"""
(TABLES / "ch6_experiment_log.md").write_text(log, encoding="utf-8")

manifest = {
    "generated_tables": sorted([p.name for p in TABLES.glob("ch6_*.tex")] + ["ch8_objective_evidence_matrix.tex"]),
    "copied_csvs": sorted(CSV_SOURCES.keys()),
    "generated_figures": sorted(p.name for p in FIGURES.glob("ch6_*.pdf")),
    "source_root": str(TOOLKIT),
}
(TABLES / "ch6_artifact_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

print(json.dumps(manifest, indent=2, ensure_ascii=False))
