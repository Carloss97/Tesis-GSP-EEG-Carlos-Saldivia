---
description: 'Viz/Tables Agent for EEG-GSP experiments. Generates all mandatory figures and LaTeX tables from stats and significance CSVs. Outputs publication-ready PDFs and .tex table files for paper and thesis.'
agent: agent
tools:
  - run_in_terminal
  - read_file
  - write_file
  - create_file
  - list_directory
argument-hint: 'iteration_tag=<tag>'
---

# EEG Viz/Tables Agent

## Mission

Generate the complete set of mandatory figures and LaTeX tables for one iteration.
All artefacts must be publication-ready: correct labels, captions, axis names, and consistent styling.

## Entry Contract (inputs)

| Artefact | Path | Required |
|----------|------|----------|
| Raw CSV | `Thesis-Copilot-Toolkit/results/<tag>_raw.csv` | yes |
| Stats CSV | `Thesis-Copilot-Toolkit/results/<tag>_stats.csv` | yes |
| Significance CSV | `Thesis-Copilot-Toolkit/results/<tag>_significance.csv` | yes |

## Exit Contract (mandatory artefacts)

All outputs go to:
- Figures: `Thesis-Copilot-Toolkit/results/<tag>_figures/`
- Tables: `Thesis-Copilot-Toolkit/results/<tag>_tables/`

### Mandatory Figures (v6/v7)

Baseline v6: fig01–fig09. Extended v7: fig01–fig11.

| File | Content |
|------|---------|
| `fig01_mae_by_method.pdf` | Bar plot — MAE mean ± CI95 per method, grouped by dataset |
| `fig02_rmse_boxplot.pdf` | Box-and-whisker — RMSE distribution per method across seeds |
| `fig03_snr_heatmap.pdf` | Heatmap — mean SNR (method × scenario) |
| `fig04_dtw_comparison.pdf` | Bar plot — DTW mean ± std when available; alternate metric summary otherwise |
| `fig05_tv_vs_instant_family.pdf` | Grouped bar — TV/Time family vs Instant family, MAE and RMSE |
| `fig06_scenario_sensitivity.pdf` | Line plot — MAE vs scenario for top-5 methods |
| `fig07_signal_reconstruction.pdf` | Signal real vs reconstrucción por electrodo interpolado |
| `fig08_temporal_error.pdf` | Error temporal — MAE por instante |
| `fig09_topomap.pdf` | Topomap 2D de error por electrodo |
| `fig10_instant_vs_full.pdf` | Instantaneous vs full-signal reconstruction side-by-side |
| `fig11_graph_topology.pdf` | Graph topology comparison on same data |

### Mandatory Tables (2)

| File | Content |
|------|---------|
| `tbl01_main_comparison.tex` | LaTeX `tabular` — method × scenario, MAE/RMSE/SNR (mean ± std) |
| `tbl02_significance.tex` | LaTeX `tabular` — key pairwise p-values with significance markers |

## Execution Steps

### Step 0 — Setup

```python
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

tag = "<iteration_tag>"
RESULTS = Path("Thesis-Copilot-Toolkit/results")
FIG_DIR = RESULTS / f"{tag}_figures"
TBL_DIR = RESULTS / f"{tag}_tables"
FIG_DIR.mkdir(parents=True, exist_ok=True)
TBL_DIR.mkdir(parents=True, exist_ok=True)

raw_df   = pd.read_csv(RESULTS / f"{tag}_raw.csv")
stats_df = pd.read_csv(RESULTS / f"{tag}_stats.csv")
# Load run metadata for normalization and missing_mode traceability
import json
meta_path = RESULTS / f"{tag}_run_metadata.json"
if meta_path.exists():
    with open(meta_path, "r") as mf:
        meta = json.load(mf)
else:
    meta = {}

normalization = meta.get("normalization", None)
missing_mode = meta.get("missing_mode", "random")

# Ensure stats CSV matches the run's normalization; fail if mixed
if "normalization" in stats_df.columns:
    norms = pd.unique(stats_df["normalization"].dropna())
    if len(norms) > 1:
        raise RuntimeError(f"Mixed normalization values in stats CSV: {norms}. Aborting to avoid invalid comparisons.")
else:
    # Propagate metadata for downstream traceability
    stats_df["normalization"] = normalization
    stats_df["missing_mode"] = missing_mode
sig_df   = pd.read_csv(RESULTS / f"{tag}_significance.csv")
scenario_col = "scenario_label" if "scenario_label" in stats_df.columns else "missing_ratio"

# Clean errored rows from raw
if "error" in raw_df.columns:
    raw_df = raw_df[raw_df["error"].isna()]

TV_TIME  = {"graph_time_tikhonov", "trss", "tv"}
PALETTE  = "tab10"
FIG_SIZE = (10, 5)
DPI      = 150

sns.set_theme(style="whitegrid", font_scale=1.1)
norm_suffix = f" (normalized: {normalization})" if normalization else ""
```

### Step 1 — fig01: MAE by method (bar + CI95)

```python
mae = stats_df[stats_df["metric"] == "mae"].copy()
order = mae.groupby("method")["mean"].mean().sort_values().index.tolist()

fig, ax = plt.subplots(figsize=FIG_SIZE)
x = np.arange(len(order))
bar_w = 0.6
means = [mae[mae["method"]==m]["mean"].mean() for m in order]
errs  = [(mae[mae["method"]==m]["mean"].mean() - mae[mae["method"]==m]["ci95_lo"].mean(),
          mae[mae["method"]==m]["ci95_hi"].mean() - mae[mae["method"]==m]["mean"].mean())
         for m in order]
errs_lo = [e[0] for e in errs]
errs_hi = [e[1] for e in errs]
colors = ["#e07b54" if m in TV_TIME else "#5b8db8" for m in order]
ax.bar(x, means, width=bar_w, color=colors, edgecolor="black", linewidth=0.5)
ax.errorbar(x, means, yerr=[errs_lo, errs_hi], fmt="none", color="black", capsize=4)
ax.set_xticks(x); ax.set_xticklabels(order, rotation=40, ha="right")
ax.set_ylabel("MAE (mean ± CI95)")
ax.set_title("Mean Absolute Error by Method")
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor="#e07b54", label="TV/Time"),
                   Patch(facecolor="#5b8db8", label="Instant")]
ax.legend(handles=legend_elements, loc="upper left")
fig.tight_layout()
fig.savefig(FIG_DIR / "fig01_mae_by_method.pdf", dpi=DPI)
plt.close(fig)
print("[fig01] saved")
```

### Step 2 — fig02: RMSE boxplot

```python
order_rmse = (raw_df.groupby("method")["rmse"].median().sort_values().index.tolist())
fig, ax = plt.subplots(figsize=FIG_SIZE)
data_list = [raw_df[raw_df["method"]==m]["rmse"].dropna().values for m in order_rmse]
bp = ax.boxplot(data_list, labels=order_rmse, patch_artist=True, notch=False, showfliers=False)
colors = ["#e07b54" if m in TV_TIME else "#5b8db8" for m in order_rmse]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)
ax.set_xticklabels(order_rmse, rotation=40, ha="right")
ax.set_ylabel("RMSE")
ax.set_title("RMSE Distribution by Method (seeds)")
fig.tight_layout()
fig.savefig(FIG_DIR / "fig02_rmse_boxplot.pdf", dpi=DPI)
plt.close(fig)
print("[fig02] saved")
```

### Step 3 — fig03: SNR heatmap (method × scenario)

```python
snr = stats_df[stats_df["metric"] == "snr"].copy()
pivot = snr.pivot_table(index="method", columns=scenario_col, values="mean")
fig, ax = plt.subplots(figsize=(8, max(4, len(pivot) * 0.35)))
sns.heatmap(pivot, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=0.3,
            cbar_kws={"label": "SNR (dB)"}, ax=ax)
ax.set_title("Mean SNR — Method × Scenario")
ax.set_xlabel("Scenario")
ax.set_ylabel("Method")
fig.tight_layout()
fig.savefig(FIG_DIR / "fig03_snr_heatmap.pdf", dpi=DPI)
plt.close(fig)
print("[fig03] saved")
```

### Step 4 — fig04: DTW comparison (or alternate if DTW unavailable)

```python
fig, ax = plt.subplots(figsize=FIG_SIZE)
if "dtw" in stats_df["metric"].unique():
    dtw = stats_df[stats_df["metric"] == "dtw"].copy()
    top10 = dtw.groupby("method")["mean"].mean().sort_values().head(10).index.tolist()
    dtw_top = dtw[dtw["method"].isin(top10)]
    order_dtw = dtw_top.groupby("method")["mean"].mean().sort_values().index.tolist()
    x = np.arange(len(order_dtw))
    means_dtw = [dtw_top[dtw_top["method"]==m]["mean"].mean() for m in order_dtw]
    stds_dtw  = [dtw_top[dtw_top["method"]==m]["std"].mean() for m in order_dtw]
    colors = ["#e07b54" if m in TV_TIME else "#5b8db8" for m in order_dtw]
    ax.bar(x, means_dtw, width=0.6, color=colors, edgecolor="black", linewidth=0.5)
    ax.errorbar(x, means_dtw, yerr=stds_dtw, fmt="none", color="black", capsize=4)
    ax.set_xticks(x); ax.set_xticklabels(order_dtw, rotation=40, ha="right")
    ax.set_ylabel("DTW (mean ± std)")
    ax.set_title("DTW — Top-10 Methods")
else:
    alt = stats_df[stats_df["metric"] == "mae"].groupby("method")["mean"].mean().sort_values().head(10)
    x = np.arange(len(alt.index))
    colors = ["#e07b54" if m in TV_TIME else "#5b8db8" for m in alt.index]
    ax.bar(x, alt.values, width=0.6, color=colors, edgecolor="black", linewidth=0.5)
    ax.set_xticks(x); ax.set_xticklabels(alt.index, rotation=40, ha="right")
    ax.set_ylabel("MAE (mean)")
    ax.set_title("MAE — Top-10 Methods (DTW unavailable)")
fig.tight_layout()
fig.savefig(FIG_DIR / "fig04_dtw_comparison.pdf", dpi=DPI)
plt.close(fig)
print("[fig04] saved")
```

### Step 5 — fig05: TV/Time vs Instant family (MAE and RMSE)

```python
for metric in ["mae", "rmse"]:
    s = stats_df[stats_df["metric"] == metric].copy()
    s["family"] = s["method"].apply(lambda m: "TV/Time" if m in TV_TIME else "Instant")
    fam_stats = s.groupby(["family", scenario_col])["mean"].mean().reset_index()
    fam_std   = s.groupby(["family", scenario_col])["std"].mean().reset_index()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for ax, metric in zip(axes, ["mae", "rmse"]):
    s = stats_df[stats_df["metric"] == metric].copy()
    s["family"] = s["method"].apply(lambda m: "TV/Time" if m in TV_TIME else "Instant")
    fam = s.groupby(["family",scenario_col]).agg(mean=("mean","mean"), std=("std","mean")).reset_index()
    for fam_name, grp in fam.groupby("family"):
        color = "#e07b54" if fam_name == "TV/Time" else "#5b8db8"
        ax.plot(grp[scenario_col], grp["mean"], "o-", color=color, label=fam_name)
        ax.fill_between(grp[scenario_col],
                        grp["mean"] - grp["std"], grp["mean"] + grp["std"],
                        alpha=0.2, color=color)
    ax.set_xlabel("Scenario"); ax.set_ylabel(metric.upper())
    ax.set_title(f"{metric.upper()} — TV/Time vs Instant")
    ax.legend()

fig.tight_layout()
fig.savefig(FIG_DIR / "fig05_tv_vs_instant_family.pdf", dpi=DPI)
plt.close(fig)
print("[fig05] saved")
```

### Step 6 — fig06: Scenario sensitivity (top-5 methods)

```python
mae = stats_df[stats_df["metric"] == "mae"].copy()
top5 = mae.groupby("method")["mean"].mean().sort_values().head(5).index.tolist()
fig, ax = plt.subplots(figsize=FIG_SIZE)
palette = sns.color_palette(PALETTE, n_colors=len(top5))
for method, color in zip(top5, palette):
    sub = mae[mae["method"] == method].sort_values(scenario_col)
    ax.plot(sub[scenario_col], sub["mean"], "o-", color=color, label=method)
    ax.fill_between(sub[scenario_col], sub["ci95_lo"], sub["ci95_hi"], alpha=0.15, color=color)
ax.set_xlabel("Scenario")
ax.set_ylabel("MAE (mean ± CI95)")
ax.set_title("MAE Sensitivity to Scenario — Top-5 Methods")
ax.legend(fontsize=9)
fig.tight_layout()
fig.savefig(FIG_DIR / "fig06_scenario_sensitivity.pdf", dpi=DPI)
plt.close(fig)
print("[fig06] saved")
```

### Step 7 — tbl01: Main comparison LaTeX table

```python
mae_s  = stats_df[stats_df["metric"]=="mae"]
rmse_s = stats_df[stats_df["metric"]=="rmse"]
snr_s  = stats_df[stats_df["metric"]=="snr"]

ratios = sorted(stats_df[scenario_col].unique())
method_mae_avg = mae_s.groupby("method")["mean"].mean()
methods_ordered = method_mae_avg.sort_values().index.tolist()

def scenario_label(v):
    if isinstance(v, (int, float, np.floating)) and 0 < float(v) < 1:
        return f"{int(round(float(v)*100))}\\%"
    return str(v)

col_spec = "l" + "".join(["c" * 3 for _ in ratios])
header_top = "\\multicolumn{1}{c}{}" + "".join(
    [f" & \\multicolumn{{3}}{{c}}{{{scenario_label(r)}}}" for r in ratios]) + " \\\\"
header_sub = "Method" + " & MAE & RMSE & SNR" * len(ratios) + " \\\\"

rows_tex = []
for m in methods_ordered:
    row = m.replace("_", "\\_")
    for r in ratios:
        mae_row  = mae_s[(mae_s["method"]==m)  & (mae_s[scenario_col]==r)]
        rmse_row = rmse_s[(rmse_s["method"]==m) & (rmse_s[scenario_col]==r)]
        snr_row  = snr_s[(snr_s["method"]==m)   & (snr_s[scenario_col]==r)]
        def fmt(df_r, col="mean", std_col="std"):
            if df_r.empty: return "--"
            return f"${df_r[col].values[0]:.3f}_{{\pm{df_r[std_col].values[0]:.3f}}}$"
        row += f" & {fmt(mae_row)} & {fmt(rmse_row)} & {fmt(snr_row)}"
    rows_tex.append(row + " \\\\")

tex = [
    "% Auto-generated by eeg-viz-tables-agent",
    f"% Iteration: {tag}",
    "\\begin{table}[ht]",
    "\\centering",
    f"\\caption{{EEG channel reconstruction — MAE, RMSE, SNR by method and scenario (mean $\\pm$ std). Iteration: \\texttt{{{tag}}}.}}",
    f"\\label{{tab:main_comparison_{tag}}}",
    "\\small",
    f"\\begin{{tabular}}{{{col_spec}}}",
    "\\toprule",
    header_top,
    "\\cmidrule(lr){" + "} \\cmidrule(lr){".join(
        [f"{2+i*3}-{4+i*3}" for i in range(len(ratios))]) + "}",
    header_sub,
    "\\midrule",
] + rows_tex + [
    "\\bottomrule",
    "\\end{tabular}",
    "\\end{table}",
]

with open(TBL_DIR / "tbl01_main_comparison.tex", "w") as f:
    f.write("\n".join(tex))
print("[tbl01] saved")
```

### Step 8 — tbl02: Significance LaTeX table

```python
sig_clean = sig_df[["test_id","metric","group_a","group_b","p_value","decision"]].copy()
sig_clean["p_value"] = sig_clean["p_value"].apply(
    lambda p: f"${p:.2e}$" if pd.notna(p) else "--")
sig_clean["sig"] = sig_df["decision"].apply(
    lambda d: "\\textbf{*}" if d == "reject_H0" else "")

tex2 = [
    "% Auto-generated by eeg-viz-tables-agent",
    f"% Iteration: {tag}",
    "\\begin{table}[ht]",
    "\\centering",
    f"\\caption{{Statistical significance of key pairwise comparisons (Bonferroni-adjusted, $\\alpha=0.05/n$). Iteration: \\texttt{{{tag}}}.}}",
    f"\\label{{tab:significance_{tag}}}",
    "\\begin{tabular}{lllllr}",
    "\\toprule",
    "Test ID & Metric & Group A & Group B & $p$-value & Decision \\\\",
    "\\midrule",
]
for _, row in sig_clean.iterrows():
    tex2.append(
        f"{row['test_id'].replace('_','-')} & {row['metric'].upper()} & "
        f"{row['group_a']} & {row['group_b']} & {row['p_value']} & "
        f"{'Reject $H_0$' if 'reject' in str(row['decision']) else 'Fail to reject'} {row['sig']} \\\\")
tex2 += [
    "\\bottomrule",
    "\\end{tabular}",
    "\\end{table}",
]
with open(TBL_DIR / "tbl02_significance.tex", "w") as f:
    f.write("\n".join(tex2))
print("[tbl02] saved")
```

### Step 9 — Validate all artefacts and emit summary

```python
required_figs = [
    "fig01_mae_by_method.pdf", "fig02_rmse_boxplot.pdf", "fig03_snr_heatmap.pdf",
    "fig04_dtw_comparison.pdf", "fig05_tv_vs_instant_family.pdf", "fig06_scenario_sensitivity.pdf",
    "fig07_signal_reconstruction.pdf", "fig08_temporal_error.pdf", "fig09_topomap.pdf",
]
required_figs_v7 = [
    "fig10_instant_vs_full.pdf", "fig11_graph_topology.pdf",
]
required_tbls = ["tbl01_main_comparison.tex", "tbl02_significance.tex"]

is_v7_iteration = tag.startswith("it7") or tag.startswith("it8")
required_all = required_figs + required_figs_v7 if is_v7_iteration else required_figs
missing_figs = [f for f in required_all if not (FIG_DIR / f).exists()]
missing_tbls = [t for t in required_tbls if not (TBL_DIR / t).exists()]

status = "OK" if not missing_figs and not missing_tbls else "FAIL"
print(f"\n[Viz/Tables] {tag}: {status}")
if missing_figs: print(f"  Missing figures: {missing_figs}")
if missing_tbls: print(f"  Missing tables: {missing_tbls}")
if status == "OK":
    print(f"  Figures: {FIG_DIR}")
    print(f"  Tables : {TBL_DIR}")
```

## Figure Style Requirements

- Font size ≥ 10 pt in all axis labels and legends.
- Axis labels must name both the quantity and unit (e.g. `MAE (a.u.)`, `Missing Ratio`).
- All PDFs must be vector format (matplotlib `Agg` backend with `.pdf` suffix).
- Color palette: orange `#e07b54` for TV/Time methods, blue `#5b8db8` for Instant methods — consistent across all figures.
- No Spanish text in figure labels or captions (figures go into the English paper).

## Table Style Requirements

- All LaTeX tables use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`).
- Caption must include the `iteration_tag` for traceability.
- Label format: `tab:<content>_<tag>`.
- Numeric values formatted to 3 decimal places.
- Mean ± std formatted as `$x.xxx_{\pm y.yyy}$`.
- p-values in scientific notation: `$p.ppe\pm qq$`.
