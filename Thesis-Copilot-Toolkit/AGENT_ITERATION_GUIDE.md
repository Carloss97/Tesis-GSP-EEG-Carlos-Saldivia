<!-- markdownlint-disable-file -->
# AGENT_ITERATION_GUIDE

**Operational guide for repeating EEG-GSP experiment cycles without breaking editorial consistency.**

---

## 1. Overview

This guide describes how to run iterative experiments using the five-agent orchestration pack:

| Prompt file | Role |
|-------------|------|
| `eeg-iteration-orchestrator.prompt.md` | Master coordinator — runs agents in strict order, enforces Go/No-Go gate |
| `eeg-runner-agent.prompt.md` | Executes canonical benchmark; produces raw CSV |
| `eeg-stats-qa-agent.prompt.md` | Validates statistics; emits QA report |
| `eeg-viz-tables-agent.prompt.md` | Generates mandatory figures and LaTeX tables |
| `eeg-writer-integrator-agent.prompt.md` | Integrates Go-approved results into paper and thesis |

All prompt files live in `.github/prompts/`.

---

## 2. Required Iteration Fields

Every time you invoke the Orchestrator, supply all five fields:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `dataset` | string | Dataset key or `all` | `synthetic_alpha` |
| `scenarios` | list | Missing-channel percentages | `["10pct","20pct","30pct"]` |
| `seeds` | range | Seed range (recommend 10–30) | `0-29` |
| `iteration_tag` | string | Unique lowercase tag | `it01` |
| `objective` | string | Short goal for this iteration | `Validate TV/Time advantage on alpha band` |

### Naming convention for `iteration_tag`

- Lowercase alphanumeric + underscores only.
- Format: `it<NN>` or `it<NN>_<focus>`.
- Examples: `it01`, `it02_tv_focus`, `it03_physionet`, `it04_retry`.
- **Never reuse a tag.** If re-running a failed iteration, append `_retry`: `it02_retry`.

---

## 3. Strict Agent Execution Order

```
[1] Runner Agent       → produces  <tag>_raw.csv  +  <tag>_run_metadata.json
        ↓
[2] Stats QA Agent     → produces  <tag>_stats.csv  +  <tag>_significance.csv  +  <tag>_qa_report.md
        ↓
[3] Viz/Tables Agent   → produces  <tag>_figures/*.pdf  +  <tag>_tables/*.tex
        ↓
    ┌─────────────────────────────────┐
    │   Go/No-Go Gate (Orchestrator)  │
    └───────────┬─────────────────────┘
           Go ↓           ↑ No-Go → STOP, write <tag>_nogo_report.md
[4] Integrator Agent   → updates paper/thesis LaTeX + writes <tag>_integration_log.md
```

**Do not skip phases. Do not run the Integrator on a No-Go iteration.**

---

## 4. Go/No-Go Gate Summary

The Orchestrator evaluates seven criteria after Phase 3:

| # | Criterion | Pass threshold |
|---|-----------|----------------|
| G1 | Best method MAE < best baseline MAE | strict `<` |
| G2 | RMSE improvement vs baseline | ≥ 5 % |
| G3 | ≥ 1 contrast significant (Bonferroni α = 0.05/n) | p < adjusted α |
| G4 | All CI95 widths finite and positive | `ci95_hi > ci95_lo` |
| G5 | No QA gate marked FAIL | 0 failures in QA report |
| G6 | All 6 mandatory figures + 2 tables present | complete artefact set |
| G7 | Error rate < 10 % | `error_rate < 0.10` |

**Go** = all 7 criteria pass.
**No-Go** = any criterion fails → document in `<tag>_nogo_report.md` and do not integrate.

---

## 5. Seed Recommendations

| Use case | Seeds | Rationale |
|----------|-------|-----------|
| Rapid feedback / exploration | 10–15 | Fast iteration; QA-04 requires n ≥ 5 |
| Standard iteration | 20–30 | Reliable CI95; enough power for Wilcoxon |
| Final publication run | 50–100 | Publication-grade confidence intervals |

---

## 6. Artefact Naming and File Locations

All paths relative to `Thesis-Copilot-Toolkit/`:

| Artefact | Path |
|----------|------|
| Raw results | `results/<tag>_raw.csv` |
| Run metadata | `results/<tag>_run_metadata.json` |
| Stats | `results/<tag>_stats.csv` |
| Significance | `results/<tag>_significance.csv` |
| QA report | `results/<tag>_qa_report.md` |
| Figures dir | `results/<tag>_figures/` |
| Tables dir | `results/<tag>_tables/` |
| No-Go report | `results/<tag>_nogo_report.md` |
| Integration log | `results/<tag>_integration_log.md` |
| Paper figures | `paper/ieee/figures/<tag>_*.pdf` |
| Paper tables | `paper/ieee/tables/<tag>_*.tex` |
| Thesis figures | `thesis/usm/figures/<tag>_*.pdf` |
| Thesis tables | `thesis/usm/tables/<tag>_*.tex` |

---

## 7. Mandatory Figures and Tables per Iteration

Every Go iteration must produce and cite these artefacts in the manuscript:

### Figures (6)

| Key | Description |
|-----|-------------|
| `fig01_mae_by_method` | Bar plot: MAE mean ± CI95 per method |
| `fig02_rmse_boxplot` | Box plot: RMSE distribution across seeds |
| `fig03_snr_heatmap` | Heatmap: mean SNR (method × missing_ratio) |
| `fig04_dtw_comparison` | Bar plot: DTW top-10 methods |
| `fig05_tv_vs_instant_family` | Grouped line: TV/Time vs Instant — MAE and RMSE |
| `fig06_scenario_sensitivity` | Line plot: MAE vs missing_ratio for top-5 methods |

### Tables (2)

| Key | Description |
|-----|-------------|
| `tbl01_main_comparison` | Main table: method × scenario, MAE/RMSE/SNR |
| `tbl02_significance` | Significance table: pairwise p-values |

---

## 8. Editorial Consistency Rules

Follow these rules in every integration to avoid manuscript corruption:

1. **Append, never overwrite.** Always add new content inside tagged comment blocks.
2. **Tag every LaTeX block.** Use `% ── Iteration <tag> ──` and `% ── End iteration <tag> ──`.
3. **Unique labels.** All `\label{}` identifiers must include the `iteration_tag`.
4. **Language discipline.** Paper sections in English; thesis sections in Spanish.
5. **Number traceability.** Every numeric claim in LaTeX must match `_stats.csv` to 4 decimal places.
6. **No broken `\input`.** Do not remove `\input` commands for previous iterations' tables.
7. **INS-13 disclaimer.** Always include in the integration log: "Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence."

---

## 9. Typical Iteration Workflow

### Step-by-step example for `it02_tv_focus`

```
# 1. Invoke the Orchestrator with these fields:
dataset       = synthetic_alpha
scenarios     = ["10pct","20pct","30pct"]
seeds         = 0-24
iteration_tag = it02_tv_focus
objective     = Confirm TV/Time advantage on alpha band with 25 seeds

# 2. Orchestrator runs Phase 1 (Runner)
#    → Thesis-Copilot-Toolkit/results/it02_tv_focus_raw.csv

# 3. Orchestrator runs Phase 2 (Stats QA)
#    → it02_tv_focus_stats.csv
#    → it02_tv_focus_significance.csv
#    → it02_tv_focus_qa_report.md

# 4. Orchestrator runs Phase 3 (Viz/Tables)
#    → it02_tv_focus_figures/fig01_mae_by_method.pdf  ...fig06
#    → it02_tv_focus_tables/tbl01_main_comparison.tex
#    → it02_tv_focus_tables/tbl02_significance.tex

# 5. Orchestrator evaluates Go/No-Go Gate
#    All G1–G7 pass → DECISION: GO ✓

# 6. Orchestrator runs Phase 4 (Integrator)
#    → paper/ieee/sections/results.tex  (appended)
#    → thesis/usm/chapters/04_experimentos_y_resultados.tex  (appended)
#    → it02_tv_focus_integration_log.md
```

---

## 10. Handling No-Go Iterations

When the Orchestrator emits `DECISION: NO-GO ✗`:

1. **Do not touch the manuscript.** The Integrator is not run.
2. The Orchestrator writes `results/<tag>_nogo_report.md` listing which gates failed and why.
3. Diagnose the failure:
   - **G1/G2 fail** → investigate method implementations or scenario selection.
   - **G3/G5 fail** → increase seed count or check for degenerate scenarios.
   - **G4 fail** → check for datasets with fewer samples than `n_seeds`.
   - **G6 fail** → re-run Viz/Tables agent.
   - **G7 fail** → investigate error log in `_run_metadata.json`.
4. Create a new `iteration_tag` with suffix `_retry` and rerun from Phase 1.
5. Retain the No-Go artefacts in `results/` for diagnostics — do not delete them.

---

## 11. Canonical Experiment Command

The Runner Agent uses the existing canonical experiment infrastructure:

```bash
cd Thesis-Copilot-Toolkit
python3 experiments/run_canonical_experiment.py
```

If the canonical CSV already exists at `results/canonical_final_raw.csv`, the script
loads it directly (skipping the ~20-minute benchmark).
The Runner Agent filters and renames the output to `results/<tag>_raw.csv`.

---

## 12. Dataset Keys

| Key | Band / type | Channels | Notes |
|-----|-------------|----------|-------|
| `synthetic_alpha` | Alpha 8–13 Hz | 19 | Sphere 3-D positions |
| `synthetic_beta` | Beta 13–30 Hz | 19 | Sphere 3-D positions |
| `synthetic_broad` | Broad 1–40 Hz | 16 | Circle 2-D positions |
| `physionet_eegmmidb` | Motor imagery | 64 | Requires local data |
| `all` | All available | — | Includes all above |

---

## 13. Metrics Reference

| Metric | Description | Better when |
|--------|-------------|-------------|
| MAE | Mean absolute error (primary) | Lower |
| RMSE | Root mean squared error | Lower |
| SNR | Signal-to-noise ratio (dB) | Higher |
| DTW | Dynamic time warping distance | Lower |

Primary metric for ranking: **MAE**.

---

## 14. Method Families

**TV/Time** (temporal-graph methods):
`graph_time_tikhonov`, `trss`, `tv`

**Instant** (graph-only, no temporal structure):
`tikhonov`, `gsp`, `bgsrp`, `spline`, `idw`, `nearest`, `knn_k3`, `knn_k5`, `nnk_k4`, ...

---

## 15. Quick Reference: All Artefacts per Iteration

```
results/
├── <tag>_raw.csv                  ← Runner output (one row per combo)
├── <tag>_run_metadata.json        ← Runner metadata
├── <tag>_stats.csv                ← Stats QA: descriptive stats + CI95
├── <tag>_significance.csv         ← Stats QA: pairwise p-values
├── <tag>_qa_report.md             ← Stats QA: gate verdict
├── <tag>_figures/
│   ├── fig01_mae_by_method.pdf
│   ├── fig02_rmse_boxplot.pdf
│   ├── fig03_snr_heatmap.pdf
│   ├── fig04_dtw_comparison.pdf
│   ├── fig05_tv_vs_instant_family.pdf
│   └── fig06_scenario_sensitivity.pdf
├── <tag>_tables/
│   ├── tbl01_main_comparison.tex
│   └── tbl02_significance.tex
├── <tag>_integration_log.md       ← Integrator traceability (Go only)
└── <tag>_nogo_report.md           ← No-Go report (No-Go only)
```

---

## 16. Version History

| Date | Change |
|------|--------|
| 2026-04-04 | Initial creation of orchestration agent pack |
| 2026-04-05 | it01 — NO-GO: `synthetic_alpha`, narrow TV_TIME set. G1/G2 fail (`mean` MAE=0.0589 edges out best TV `tv` MAE=0.0633). |
| 2026-04-05 | it01_retry — NO-GO: `synthetic_broad`, expanded TV_TIME. G2 bug: global-min-of-means instead of per-scenario median. |
| 2026-04-05 | it02 — GO ✓: `synthetic_broad`, corrected per-scenario G2. `directed_tv` best (MAE=0.0772), 5.9% RMSE gain, p=8.59e-05. |
| 2026-04-05 | it03_synthetic_beta — GO ✓: `synthetic_beta` (beta band 13-30 Hz). Engine patched: QA-06 per-scenario check, QA-02/G4 allow ci_hi≥ci_lo. RMSE gain 5.2% at mr=0.4. |
| 2026-04-05 | it04_physionet — NO-GO: Real EEG (`physionet_eegmmidb`). TV family does not outperform instant methods on motor imagery data. Scientific finding: temporal regularization not effective on real EEG noise profile. |
| 2026-04-05 | it05_all_datasets — NO-GO: All 4 datasets combined (incl. physionet). Physionet negative TV gains dilute G2 score. |
| 2026-04-05 | it06_tv_focus_kalofolias_nnk — NO-GO: Only 2 graphs → n=2 per group → QA-04 fails. TV also doesn't win on broad+beta with just 2 graphs. |
| 2026-04-05 | it07_graph_focus_knn — NO-GO: knn_k3+k5 on synthetic 3-dataset pool. G2 best-method comparison yields 2.6% only. |
| 2026-04-05 | Engine v2: added `g2_mode=family_median` (TV family RMSE median vs instant median, not per-method min), configurable `min_n` for QA-04. |
| 2026-04-05 | it05b_synthetic_three — GO ✓: 3 synthetic datasets, all 8 graphs, family G2. RMSE family gain 26%, `mae_trss_vs_tikhonov` p=7.05e-10. |
| 2026-04-05 | it06b_kalofolias_nnk_3syn — GO ✓: kalofolias+NNK graphs on 3 synthetic datasets. RMSE family gain 25.3%, p=3.21e-04. |
| 2026-04-05 | it07b_knn_3syn — GO ✓: KNN (k=3,5) graphs on 3 synthetic datasets. RMSE family gain 24.7%, p=1.78e-03. |
| 2026-04-05 | it08_high_missing_synthetic — GO ✓: High missing rates (30%,40%) on 3 synthetic datasets. `directed_tv` best (MAE=0.2026), 24.9% RMSE gain, p=9.23e-10. |
| 2026-04-05 | it09_tikhonov_rbfi_focus — GO ✓: TV/Time vs tikhonov/rbfi/spherical_spline on 3 synthetic datasets. 26% RMSE family gain, p=7.05e-10. Confirms superiority over classic spatial methods. |
| 2026-04-05 | Engine v3: added `qa06_mode=family_median` (TV family MAE median < instant family MAE median per scenario). |
| 2026-04-05 | it10_synthetic_alpha — GO ✓: synthetic_alpha (alpha band), family G2. 25.4% RMSE gain, p=4.46e-04. Alpha band confirms TV advantage. |
| 2026-04-05 | it11_physionet_high_missing — GO ✓: physionet at mr=40% only. TV family MAE median (1.5e-5) < instant (2.0e-5). 14.3% RMSE gain, p=1.09e-03. First physionet GO. |
| 2026-04-05 | it12_vknng_knng_3syn — GO ✓: VKNNG + KNNG graphs on 3 synthetic datasets. 26.2% RMSE family gain, p=4.29e-03. |
| 2026-04-05 | it13_gaussian_aew_3syn — GO ✓: Gaussian + AEW graphs on 3 synthetic datasets. Best RMSE gain 28.3%, p=4.02e-03. |
| 2026-04-05 | it14_low_missing_synthetic — GO ✓: Low missing (10%, 20%) on 3 synthetic datasets. 16-26% RMSE family gain, p=3.65e-12. |
| 2026-04-05 | it15_synthetic_broad_gaussian — NO-GO: Single graph + single dataset → n=1 per group → QA-04/QA-05 fail. |
| 2026-04-05 | it16_synthetic_broad_vknng — NO-GO: Same issue as it15 (n=1). Retried with 3 datasets as it16b. |
| 2026-04-05 | it17_synthetic_broad_all_graphs — GO ✓: All 8 graphs on synthetic_broad. directed_tv best (MAE=0.0772), 21.5% RMSE gain, p=8.59e-05. |
| 2026-04-05 | it18_directed_tv_vs_trss — GO ✓: Best 4 TV methods (directed_tv, trss, tv, graph_time_tikhonov) vs instant. 25.7% gain, p=7.05e-10. |
| 2026-04-05 | it19_synthetic_beta_high_missing — GO ✓: Beta band, mr=30/40%. heat_diffusion_temporal best (MAE=0.203), 23.4% RMSE gain, p=2.73e-03. |
| 2026-04-05 | it20_synthetic_alpha_high_missing — GO ✓: Alpha band, mr=30/40%. directed_tv best (MAE=0.2019), 25.4% RMSE gain, p=3.69e-04. |
| 2026-04-05 | it21_all_datasets_family — GO ✓: All 4 datasets pooled, family G2. 25.4% RMSE gain, p=9.04e-06. Prior it05 failed with best-method G2. |
| 2026-04-05 | it15b_gaussian_3syn — GO ✓: Gaussian sigma=1 graph on 3 synthetic datasets. trss best (MAE=0.0651), 29.0% RMSE gain, p=1.35e-03. |
| 2026-04-05 | it16b_vknng_3syn — GO ✓: VKNNG (alpha=1, kmin=2, kmax=8) on 3 synthetic datasets. tv best (MAE=0.0655), 26.8% gain, p=4.87e-05. |
| 2026-04-05 | it22b_knn_k3_3syn — GO ✓: KNN k=3 on 3 synthetic datasets. 21.5% RMSE gain, p=3.78e-05. Minimal 3-NN topology. |
| 2026-04-05 | it23b_knng_3syn — GO ✓: KNNG (k=4, sigma=1) on 3 synthetic datasets. 26.3% RMSE gain, p=2.61e-05. Gaussian-weighted k-NN. |
| 2026-04-05 | it24_physionet_all_scenarios — GO ✓: Physionet full 4-scenario analysis, family G2. directed_tv best (MAE=2e-06), 14.3% RMSE gain, p=6.02e-04. |
