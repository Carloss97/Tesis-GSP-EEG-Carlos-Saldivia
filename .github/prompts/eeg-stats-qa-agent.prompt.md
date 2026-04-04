---
description: 'Stats QA Agent for EEG-GSP experiments. Validates statistical quality of raw results: computes descriptive stats, confidence intervals, significance tests, and emits a QA report with Go/No-Go flags for each criterion.'
agent: agent
tools:
  - run_in_terminal
  - read_file
  - write_file
  - create_file
  - list_directory
argument-hint: 'iteration_tag=<tag>'
---

# EEG Stats QA Agent

## Mission

Compute descriptive statistics, confidence intervals, and significance tests from the raw
results CSV produced by the Runner Agent.
Emit a QA report with a clear PASS/FAIL verdict for each statistical gate.

## Entry Contract (inputs)

| Artefact | Path | Required |
|----------|------|----------|
| Raw CSV | `Thesis-Copilot-Toolkit/results/<tag>_raw.csv` | yes |
| Run metadata | `Thesis-Copilot-Toolkit/results/<tag>_run_metadata.json` | yes |

Required CSV columns: `dataset`, `graph`, `method`, `missing_ratio`, `seed`, `mae`, `rmse`, `snr`, `dtw`

## Exit Contract (artefacts produced)

| Artefact | Path | Description |
|----------|------|-------------|
| Stats CSV | `results/<tag>_stats.csv` | Per-(method, scenario) mean, std, CI95 for all metrics |
| Significance CSV | `results/<tag>_significance.csv` | Pairwise p-values for key contrasts |
| QA Report | `results/<tag>_qa_report.md` | Markdown checklist of all QA gates |

## Execution Steps

### Step 1 — Load and validate raw data

```python
import pandas as pd
import numpy as np
from pathlib import Path

RESULTS = Path("Thesis-Copilot-Toolkit/results")
tag = "<iteration_tag>"

df = pd.read_csv(RESULTS / f"{tag}_raw.csv")

# Drop errored rows
if "error" in df.columns:
    df_clean = df[df["error"].isna()].copy()
else:
    df_clean = df.copy()

metrics = ["mae", "rmse", "snr", "dtw"]
assert all(m in df_clean.columns for m in metrics), "Missing metric columns"
```

### Step 2 — Compute descriptive statistics and CI95

```python
from scipy import stats as scipy_stats

def ci95(x):
    x = x.dropna()
    if len(x) < 2:
        return np.nan, np.nan
    se = scipy_stats.sem(x)
    ci = scipy_stats.t.interval(0.95, df=len(x)-1, loc=x.mean(), scale=se)
    return ci[0], ci[1]

rows = []
for (method, missing_ratio), grp in df_clean.groupby(["method", "missing_ratio"]):
    for m in metrics:
        vals = grp[m].dropna()
        lo, hi = ci95(vals)
        rows.append({
            "method": method,
            "missing_ratio": missing_ratio,
            "metric": m,
            "mean": vals.mean(),
            "std": vals.std(ddof=1),
            "median": vals.median(),
            "ci95_lo": lo,
            "ci95_hi": hi,
            "n": len(vals),
        })

stats_df = pd.DataFrame(rows)
stats_df.to_csv(RESULTS / f"{tag}_stats.csv", index=False)
```

### Step 3 — Significance tests

Run the following key contrasts using Mann-Whitney U (unpaired) or Wilcoxon signed-rank (paired):

| test_id | metric | group_a | group_b | test |
|---------|--------|---------|---------|------|
| `mae_trss_vs_tikhonov` | mae | trss | tikhonov | Mann-Whitney U |
| `mae_bgsrp_vs_tikhonov` | mae | bgsrp | tikhonov | Mann-Whitney U |
| `mae_tv_family_vs_instant` | mae | tv_time family | instant family | Wilcoxon |
| `rmse_trss_vs_tikhonov` | rmse | trss | tikhonov | Mann-Whitney U |
| `dtw_tv_family_vs_instant` | dtw | tv_time family | instant family | Wilcoxon |

TV/Time methods: `graph_time_tikhonov`, `trss`, `tv`
Instant methods: all others

Apply Bonferroni correction for multiple comparisons (alpha = 0.05 / n_tests).

```python
from scipy.stats import mannwhitneyu, wilcoxon

TV_TIME = {"graph_time_tikhonov", "trss", "tv"}
alpha = 0.05
n_tests = 5  # update if more contrasts are added
bonferroni_alpha = alpha / n_tests

sig_rows = []

def mwu(a_vals, b_vals, test_id, metric, group_a, group_b):
    a = a_vals.dropna().values
    b = b_vals.dropna().values
    if len(a) < 3 or len(b) < 3:
        return {"test_id": test_id, "metric": metric, "group_a": group_a,
                "group_b": group_b, "p_value": np.nan, "decision": "insufficient_data"}
    stat, p = mannwhitneyu(a, b, alternative="two-sided")
    decision = "reject_H0" if p < bonferroni_alpha else "fail_to_reject_H0"
    return {"test_id": test_id, "metric": metric, "group_a": group_a,
            "group_b": group_b, "statistic": stat, "p_value": p, "decision": decision}

for metric in ["mae", "rmse"]:
    a = df_clean[df_clean["method"] == "trss"][metric]
    b = df_clean[df_clean["method"] == "tikhonov"][metric]
    sig_rows.append(mwu(a, b, f"{metric}_trss_vs_tikhonov", metric, "trss", "tikhonov"))

for metric in ["mae", "dtw"]:
    a = df_clean[df_clean["method"].isin(TV_TIME)][metric]
    b = df_clean[~df_clean["method"].isin(TV_TIME)][metric]
    sig_rows.append(mwu(a, b, f"{metric}_tv_family_vs_instant", metric, "tv_time", "instant"))

sig_df = pd.DataFrame(sig_rows)
sig_df.to_csv(RESULTS / f"{tag}_significance.csv", index=False)
```

### Step 4 — QA Gates

Evaluate each gate and record PASS/FAIL:

| Gate ID | Check | PASS condition |
|---------|-------|----------------|
| QA-01 | No missing values in stats CSV | 0 NaN in mean/std columns |
| QA-02 | CI95 widths are positive and finite | `ci95_hi > ci95_lo` for all rows |
| QA-03 | All methods present for primary metric (MAE) | Each expected method has ≥ 1 row |
| QA-04 | N ≥ 5 per (method, scenario) | `n >= 5` in all stats rows |
| QA-05 | At least one contrast significant (Bonferroni) | ≥ 1 row in `significance.csv` with `decision=reject_H0` |
| QA-06 | TV/Time family MAE < best instant MAE (median) | `median_tv < median_instant` |
| QA-07 | No duplicate (method, missing_ratio) rows in stats CSV | 0 duplicates |

```python
gates = {}

# QA-01
gates["QA-01"] = "PASS" if stats_df[["mean","std"]].isna().sum().sum() == 0 else "FAIL"

# QA-02
gates["QA-02"] = "PASS" if (stats_df["ci95_hi"] > stats_df["ci95_lo"]).all() else "FAIL"

# QA-03
expected_methods = df_clean["method"].unique()
present = stats_df[stats_df["metric"]=="mae"]["method"].unique()
gates["QA-03"] = "PASS" if set(expected_methods) <= set(present) else "FAIL"

# QA-04
gates["QA-04"] = "PASS" if (stats_df["n"] >= 5).all() else "FAIL"

# QA-05
if not sig_df.empty and "decision" in sig_df.columns:
    gates["QA-05"] = "PASS" if (sig_df["decision"] == "reject_H0").any() else "FAIL"
else:
    gates["QA-05"] = "FAIL"

# QA-06
mae_stats = stats_df[stats_df["metric"] == "mae"]
tv_median = mae_stats[mae_stats["method"].isin(TV_TIME)]["median"].min()
instant_median = mae_stats[~mae_stats["method"].isin(TV_TIME)]["median"].min()
gates["QA-06"] = "PASS" if (not np.isnan(tv_median) and tv_median < instant_median) else "FAIL"

# QA-07
dups = stats_df.duplicated(subset=["method","missing_ratio","metric"]).sum()
gates["QA-07"] = "PASS" if dups == 0 else "FAIL"
```

### Step 5 — Write QA Report

```python
overall = "PASS" if all(v == "PASS" for v in gates.values()) else "FAIL"

lines = [
    f"# Stats QA Report — {tag}",
    "",
    f"**Overall: {overall}**",
    "",
    "## QA Gates",
    "",
    "| Gate | Description | Status |",
    "|------|-------------|--------|",
    f"| QA-01 | No missing values in stats | {gates['QA-01']} |",
    f"| QA-02 | CI95 widths positive/finite | {gates['QA-02']} |",
    f"| QA-03 | All methods present in MAE stats | {gates['QA-03']} |",
    f"| QA-04 | N ≥ 5 per (method, scenario) | {gates['QA-04']} |",
    f"| QA-05 | ≥ 1 contrast significant (Bonferroni) | {gates['QA-05']} |",
    f"| QA-06 | TV/Time MAE < best instant MAE | {gates['QA-06']} |",
    f"| QA-07 | No duplicate stats rows | {gates['QA-07']} |",
    "",
    "## Top Methods by MAE (median across scenarios)",
    "",
    "| Rank | Method | MAE median | MAE mean | MAE std |",
    "|------|--------|-----------|----------|---------|",
]

top = (stats_df[stats_df["metric"]=="mae"]
       .groupby("method")["median"].min()
       .sort_values()
       .reset_index())
for i, row in top.iterrows():
    mean_val = stats_df[(stats_df["metric"]=="mae") & (stats_df["method"]==row["method"])]["mean"].mean()
    std_val  = stats_df[(stats_df["metric"]=="mae") & (stats_df["method"]==row["method"])]["std"].mean()
    lines.append(f"| {i+1} | {row['method']} | {row['median']:.4f} | {mean_val:.4f} | {std_val:.4f} |")

lines += [
    "",
    "## Significance Summary",
    "",
    sig_df[["test_id","metric","group_a","group_b","p_value","decision"]].to_markdown(index=False),
    "",
    "## Interpretation Note",
    "",
    "- TV/Time family: `graph_time_tikhonov`, `trss`, `tv`.",
    "- Bonferroni-adjusted alpha: {:.4f}.".format(bonferroni_alpha),
    "- INS-13 status: proxy Python-only — do not claim 1:1 MATLAB/GSPBox equivalence.",
]

with open(RESULTS / f"{tag}_qa_report.md", "w") as f:
    f.write("\n".join(lines))

print(f"[Stats QA] {tag}: overall={overall}")
for g, v in gates.items():
    print(f"  {g}: {v}")
```

## Output Interpretation

- A single **FAIL** gate blocks the Go/No-Go decision in the Orchestrator.
- QA-06 FAIL means the TV/Time advantage is not confirmed in this iteration — investigate scenario coverage and seeds.
- QA-05 FAIL means no statistically significant contrast found — consider increasing seed count.

## Language and Formatting Requirements

- All file content (CSV headers, report text) in English.
- p-values formatted as scientific notation with 3 significant digits.
- Round all float metrics to 4 decimal places in CSV and report tables.
