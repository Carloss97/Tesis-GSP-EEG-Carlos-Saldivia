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

## 1.1 Data normalization & dataset availability (policy)

During development we found two operational issues that must be explicit in the guide so results remain comparable and reproducible:

- Mixing normalized runs with non-normalized runs produces non-comparable metrics (example: MAE in µV vs. normalized RMS-based error). To avoid invalid comparisons, normalized executions MUST be isolated and clearly labeled.

- Local real datasets are available in most environments (`physionet_real`, `bci_iv2a_real_s1`, `bci_iv2a_real_s2`, `bci_iv2a_real_s3`, `mne_sample`). The orchestrator and runner should prefer these keys; proxies and synthetic datasets are FALLBACK only.

Policy (conventions):

- Naming / storage:
        - Keep original (raw) runs in `results/` and place normalized runs in a separate folder prefixed `results_normalized_<timestamp>/` or append `_norm` to the `iteration_tag` (example: `it123_norm`).
        - Do NOT mix normalized and non-normalized CSVs when aggregating or computing comparisons.

- Metadata:
        - Every run metadata file (`*_run_metadata.json`) MUST include a `"normalization"` field set to either `null` (no normalization) or the method name (e.g., `"rms"`).
        - When a missing-channel policy mode is applied, the metadata MUST include `"missing_mode"`: one of `"random"` or `"nearby"`.

- Execution flags (convention):
        - Use environment variables to request normalized runs: `NORMALIZE_DATASETS=1` and `NORM_METHOD=rms` (or other supported method). The Runner will then write outputs to the normalized results folder.
        - Use the orchestrator's availability check (or `base_mod.load_data_availability()`) to detect local real datasets and avoid proxies whenever possible.

- Scenarios and missing-channel patterns (supported formats):
        - Fractional: `0.1`, `0.2` (representing 10 %, 20 % missing channels)
        - Absolute counts: `"1ch"`, `"2ch"`, `"3ch"` (remove exactly N electrodes)
        - Mode qualifiers: combine with `_random` or `_nearby` (example: `"2ch_random"`, `"3ch_nearby"`). If the qualifier is omitted the default is `random`.
        - Runner implementations MUST record the `missing_mode` in the run metadata and support both random and spatially-adjacent (`nearby`) removals.

Rationale and impact:

- This policy ensures that statistical summaries, pairwise tests and ranking operations compare homogeneous groups (same normalization and same missing-mode). It also documents the presence of real, local datasets so the pipeline does not silently use proxies.

See `docs/normalization_and_dataset_policy.md` for concrete examples, recommended commands and metadata templates.

---

## 2. Required Iteration Fields

Every time you invoke the Orchestrator, supply all five fields:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `dataset` | string | Dataset key or `all` | `synthetic_alpha` |
| `scenarios` | list | Missing scenarios (ratio o count) | `["10pct","20pct","30pct"]` o `["1ch","2ch"]` |
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
| G6 | All mandatory figures + 2 tables present | v6: 9 figs + 2 tables, v7: 11 figs + 2 tables |
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


### Engine v7 (it71–it82): Nuevas figuras y artefactos
Cada iteración GO debe producir y citar los siguientes artefactos en el manuscrito:

#### Figuras (11 obligatorias)
| Key | Description |
|-----|-------------|
| fig01_mae_by_method | Bar plot: MAE mean ± CI95 per method |
| fig02_rmse_boxplot | Box plot: RMSE distribution across seeds |
| fig03_snr_heatmap | Heatmap: mean SNR (method × missing_ratio) |
| fig04_dtw_comparison | Bar plot: DTW top-10 methods |
| fig05_tv_vs_instant_family | Grouped line: TV/Time vs Instant — MAE and RMSE |
| fig06_scenario_sensitivity | Line plot: MAE vs missing_ratio for top-5 methods |
| fig07_signal_reconstruction | Signal real vs. reconstruction per interpolated electrode |
| fig08_temporal_error | Temporal error — MAE per time instant |
| fig09_topomap | 2D topomap of per-electrode reconstruction error |
| fig10_instant_vs_full | Instantaneous vs. full-signal reconstruction side-by-side (nuevo v7) |
| fig11_graph_topology | Graph topology comparison — same data, different graph structures (nuevo v7) |

#### Tablas (2)
| Key | Description |
|-----|-------------|
| tbl01_main_comparison | Main table: method × scenario, MAE/RMSE/SNR |
| tbl02_significance | Significance table: pairwise p-values |

#### Escenarios y datasets
- Fase 6 (it71–it80): Escenarios de 1, 2, 3 electrodos faltantes (no solo proporciones), en synthetic broadband, MNE Sample proxy (60ch/600Hz), y BCI Competition IV 2a proxy (22ch/250Hz).
- Fase 7 (it81–it82): Análisis de reconstrucción completa vs. instantánea.

#### Artefactos por iteración (GO):
- _raw.csv, _stats.csv, _significance.csv, _qa_report.md, _run_metadata.json, _integration_log.md
- 11 figuras PDF en paper/ieee/figures/ por iteración



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
#    → it02_tv_focus_figures/fig01_mae_by_method.pdf  ...fig11
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
| `synthetic_alpha` | Alpha 8–13 Hz | 19 | Histórica v6 |
| `synthetic_beta` | Beta 13–30 Hz | 19 | Histórica v6 |
| `synthetic_broad` | Broad 1–40 Hz | 16 | Histórica v6 |
| `synthetic_8ch` | Sintético baja densidad | 8 | Introducido en v7 |
| `synthetic_16ch` | Sintético densidad media | 16 | Introducido en v7 |
| `synthetic_32ch` | Sintético alta densidad | 32 | Introducido en v7 |
| `physionet_eegmmidb` | Motor imagery real | 64 | Requiere datos locales |
| `mne_sample_proxy` | Auditivo/visual proxy | 60 | Proxy sintético |
| `bci_competition_proxy` | Motor imagery proxy | 22 | Proxy sintético |
| `bci_competition_proxy_s2` | Motor imagery proxy (subject/session variant) | 22 | Variante usada en v7 |
| `all` | Todos los disponibles | — | Depende de la configuración |

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
`graph_time_tikhonov`, `trss`, `tv`, `temporal_laplacian`

Rationale: `temporal_laplacian` implements a product-graph spatio-temporal Laplacian regularizer (combines spatial Laplacian and temporal Laplacian) and is recommended for time-varying signals. See Jiang et al., 2021 (spatio-temporal / product-graph imputation) and Giraldo et al., 2022 (GraphTRSS / Sobolev temporal smoothness) for theoretical and empirical support.

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
│   ├── fig06_scenario_sensitivity.pdf
│   ├── fig07_signal_reconstruction.pdf
│   ├── fig08_temporal_error.pdf
│   ├── fig09_topomap.pdf
│   ├── fig10_instant_vs_full.pdf
│   └── fig11_graph_topology.pdf
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
| 2026-04-05 | Engine v4: 16 new iterations (it25-it40). Covers two-band analysis, per-dataset all-graph exhaustive, per-graph single-dataset (with 3 datasets for n≥3), strong-TV focus, per-scenario (mr=20%, mr=30%), physionet best-graph combos. |
| 2026-04-05 | it25_alpha_beta_two_bands — GO ✓: Alpha+beta (no broadband), family G2. mean MAE=0.0624, 25.6% RMSE gain, p=1.40e-06. |
| 2026-04-05 | it26_synthetic_beta_all_graphs — GO ✓: Synthetic beta band — all 8 graphs. gsmooth MAE=0.0657, 26.2% RMSE gain, p=8.90e-04. |
| 2026-04-05 | it27_synthetic_alpha_all_graphs — GO ✓: Synthetic alpha band — all 8 graphs. mean MAE=0.0589, 25.4% RMSE gain, p=4.46e-04. |
| 2026-04-05 | it28_nnk_3syn — GO ✓: NNK k=4 graph on 3 synthetic datasets. gsmooth MAE=0.0651, 22.7% RMSE gain, p=8.79e-06. |
| 2026-04-05 | it29_kalofolias_3syn — GO ✓: Kalofolias graph on 3 synthetic datasets. mean MAE=0.0659, 25.5% RMSE gain, p=3.66e-05. |
| 2026-04-05 | it30_knn_k5_3syn — GO ✓: KNN k=5 on 3 synthetic datasets. mean MAE=0.0659, 27.4% RMSE gain, p=8.19e-05. KNN k=5 slightly outperforms k=3 (it22b). |
| 2026-04-05 | it31_strong_tv_3syn — GO ✓: Strong TV (directed_tv, tv, trss) only on 3 synthetic. gsmooth MAE=0.0658, 26.0% RMSE gain, p=7.05e-10. |
| 2026-04-05 | it32_3syn_mr20_only — GO ✓: 3 synthetic, mr=20% only (moderate missing). mean MAE=0.1252, 26.0% RMSE gain, p=7.81e-08. |
| 2026-04-05 | it33_3syn_mr30_only — GO ✓: 3 synthetic, mr=30% only (high missing). directed_tv MAE=0.2026, 24.9% RMSE gain, p=1.23e-07. |
| 2026-04-05 | it34_physionet_kalofolias_gaussian — NO-GO: Physionet with kalofolias+gaussian, mr=30/40%. n<5 per group → QA-04 fails. |
| 2026-04-05 | it35_all4_kalofolias — GO ✓: All 4 datasets + kalofolias graph. mean MAE=0.0624, 25.0% RMSE gain, p=3.94e-03. |
| 2026-04-05 | it36_3syn_beta_low_missing — GO ✓: Synthetic beta, mr=10/20%. gsmooth MAE=0.0657, 26.2% RMSE gain, p=2.05e-04. |
| 2026-04-05 | it37_3syn_alpha_low_missing — GO ✓: Synthetic alpha, mr=10/20%. mean MAE=0.0589, 23.1% RMSE gain, p=5.09e-05. |
| 2026-04-05 | it38_broad_gaussian_kalofolias_nnk — GO ✓: synthetic_broad + 3 complementary graphs (Gaussian, Kalofolias, NNK). heat_diffusion_temporal MAE=0.0813, 22.1% RMSE gain, p=3.55e-03. |
| 2026-04-05 | it39_physionet_gaussian_nnk_knn — GO ✓: Physionet at mr=40%, best 3 graphs (gaussian, nnk, knn_k3). mean MAE=1.3e-05, 18.5% RMSE gain, p=5.97e-03. |
| 2026-04-05 | it40_3syn_all_mr_analysis — GO ✓: KNN k=3 and k=5 on 3 synthetic, all 4 missing rates. mean MAE=0.0659, 24.7% RMSE gain, p=1.78e-03. |

| 2026-04-05 | Engine v5: 20 new iterations (it41-it60). Covers multi-subject physionet (9 subjects × runs 4/8/12), multi-run pooled analysis, graph variants on physionet (gaussian, kalofolias, best-3), high/low missing rate split on physionet, strong-TV subset on physionet, all-datasets cross-graph analysis (gaussian, NNK, strong-TV), all-datasets high/low missing split, and exhaustive synthetic broadband analysis (mr splits, all-8-graphs × high-mr). GO count: 19/20. |
| 2026-04-05 | it41_physionet_multisubject_run4 — GO ✓: Physionet 9 subjects, run=4 motor imagery L/R, knn_k3. |
| 2026-04-05 | it42_physionet_run8_allsubj — GO ✓: Physionet 9 subjects, run=8 motor imagery hands/feet, knn_k3. |
| 2026-04-05 | it43_physionet_run12_allsubj — GO ✓: Physionet 9 subjects, run=12 motor imagery hands/feet, knn_k3. |
| 2026-04-05 | it44_physionet_allruns_allsubj — GO ✓: Physionet 9 subjects × 3 runs pooled, knn_k3. |
| 2026-04-05 | it45_physionet_multisubj_gaussian — GO ✓: Physionet 9 subjects, run=4, gaussian sigma=1 graph. |
| 2026-04-05 | it46_physionet_multisubj_kalofolias — GO ✓: Physionet 9 subjects, run=4, kalofolias graph. |
| 2026-04-05 | it47_physionet_multisubj_best3graphs — GO ✓: Physionet 9 subjects, run=4, 3 best graphs (knn_k3, gaussian, kalofolias). |
| 2026-04-05 | it48_physionet_multisubj_high_mr — GO ✓: Physionet 9 subjects, run=4, high missing rates 30%/40%. |
| 2026-04-05 | it49_physionet_multisubj_low_mr — GO ✓: Physionet 9 subjects, run=4, low missing rates 10%/20%. |
| 2026-04-05 | it50_physionet_multisubj_strong_tv — NO-GO ✗: Physionet 9 subjects, run=4, strong TV+instant subset comparison. |
| 2026-04-05 | it51_all_datasets_strong_tv — GO ✓: All 4 datasets — strong TV/Time + key instant methods. |
| 2026-04-05 | it52_all_datasets_gaussian_graph — GO ✓: All 4 datasets — Gaussian sigma=1 graph only. |
| 2026-04-05 | it53_all_datasets_nnk — GO ✓: All 4 datasets — NNK k=4 graph only. |
| 2026-04-05 | it54_all_datasets_high_mr — GO ✓: All 4 datasets — high missing rates 30%+40%. |
| 2026-04-05 | it55_all_datasets_low_mr — GO ✓: All 4 datasets — low missing rates 10%+20%. |
| 2026-04-05 | it56_3syn_mr10_only — GO ✓: Alpha+Beta+Broad synthetic — mr=10% only. |
| 2026-04-05 | it57_3syn_mr40_only — GO ✓: Alpha+Beta+Broad synthetic — mr=40% only. |
| 2026-04-05 | it58_broad_low_missing — GO ✓: Synthetic broadband — low missing rates 10%+20%. |
| 2026-04-05 | it59_broad_high_missing — GO ✓: Synthetic broadband — high missing rates 30%+40%. |
| 2026-04-05 | it60_broad_all_graphs_high_mr — GO ✓: Synthetic broadband — all 8 graphs × high missing rates 30%+40%. |


## Motor de Estadísticas v6 — Datasets Proxy Externos

**Activado en**: it61–it70  
**Novedad**: Soporte para datasets proxy de MNE Sample y BCI Competition IV 2a

### Nuevas funciones en data_loader.py
- `load_mne_sample_proxy(seed)`: 60 canales, 600 Hz, respuestas auditivas/visuales (proxy)
- `load_bci_competition_proxy(subject, session)`: 22 canales, 250 Hz, motor imagery (proxy)

### Nuevos tipos de figuras (fig07-fig09)
- `fig07_signal_reconstruction`: Señal original vs reconstrucción TV y Instant
- `fig08_temporal_error`: Error MAE por instante temporal con suavizado
- `fig09_topomap`: Mapa topográfico 2D de error por electrodo

### Iteraciones Fase 5 (it61-it70)
- it61-it63: MNE Sample proxy (60ch, auditivo/visual)
- it64-it67: BCI Competition IV 2a proxy (22ch, motor imagery)
- it68-it69: Combinación multi-dataset proxy
- it70: Los 5 datasets combinados (análisis final exhaustivo)

### Tabla de iteraciones Fase 5

| Fecha | Entrada |
|-------|---------|
| 2026-04-05 | it61_mne_sample_knn — GO ✓: MNE Sample proxy (60ch) kNN-k3, todos los MR. |
| 2026-04-05 | it62_mne_sample_all_graphs — GO ✓: MNE Sample proxy, 3 grafos (kNN, Gaussian, Kalofolias). |
| 2026-04-05 | it63_mne_sample_high_mr — GO ✓: MNE Sample proxy, alta pérdida (30-40%). |
| 2026-04-05 | it64_bci_competition_single_subj — GO ✓: BCI Competition IV 2a proxy, sujeto 1, kNN-k3. |
| 2026-04-05 | it65_bci_competition_multisubj — GO ✓: BCI Competition IV 2a proxy, 9 sujetos, kNN-k3. |
| 2026-04-05 | it66_bci_competition_gaussian — GO ✓: BCI Competition IV 2a proxy, 9 sujetos, grafo Gaussiano. |
| 2026-04-05 | it67_bci_competition_all_graphs — GO ✓: BCI Competition IV 2a proxy, sujeto 1, 3 grafos. |
| 2026-04-05 | it68_three_real_datasets — GO ✓: Tres datasets (PhysioNet+MNE+BCI proxy), kNN-k3. |
| 2026-04-05 | it69_mne_bci_high_mr — GO ✓: MNE Sample + BCI proxy, alta pérdida (30-40%). |
| 2026-04-05 | it70_all_five_datasets — GO ✓: Los 5 datasets combinados (análisis final exhaustivo). |

## Motor de Estadísticas v7 — Few-Electrode + Full-Signal

**Activado en**: it71–it82  
**Novedad**: escenarios de pocos electrodos faltantes (`1ch`, `2ch`, `3ch`) y análisis de reconstrucción instantánea vs señal completa.

### Iteraciones Fase 6 (it71-it80)

| Fecha | Entrada |
|-------|---------|
| 2026-04-06 | it71_few_missing_1ch_synthetic — NO-GO: 1ch faltante, synthetic_16ch, kNN-k3. |
| 2026-04-06 | it72_few_missing_2ch_synthetic — NO-GO: 2ch faltantes, synthetic_16ch, kNN-k3. |
| 2026-04-06 | it73_few_missing_1ch_mne_proxy — GO ✓: 1ch faltante, mne_sample_proxy, kNN-k3. |
| 2026-04-06 | it74_few_missing_2ch_mne_proxy — GO ✓: 2ch faltantes, mne_sample_proxy, kNN-k3. |
| 2026-04-06 | it75_few_missing_multi_synthetic — NO-GO: 1+2ch, synthetic_8/16/32ch. |
| 2026-04-06 | it76_few_missing_mne_all_graphs — NO-GO: mne_sample_proxy con varios grafos. |
| 2026-04-06 | it77_few_missing_bci_all_graphs — NO-GO: bci_competition_proxy con varios grafos. |
| 2026-04-06 | it78_few_missing_1ch_tv_focus — NO-GO: 1ch, 5 datasets, TV focus. |
| 2026-04-06 | it79_few_missing_2ch_tv_focus — NO-GO: 2ch, 5 datasets, TV focus. |
| 2026-04-06 | it80_few_missing_comprehensive — NO-GO: análisis integral 1+2+3ch. |

### Iteraciones Fase 7 parcial (it81-it82)

| Fecha | Entrada |
|-------|---------|
| 2026-04-06 | it81_instant_vs_full_synthetic — NO-GO: comparación instantánea vs full-signal en synthetic_16ch. |
| 2026-04-06 | it82_full_signal_recon_synthetic — NO-GO: reconstrucción de señal completa (all instants) en synthetic_16ch. |

### Iteraciones Fase 7 completación (it83-it87)

| Fecha | Entrada |
|-------|---------|
| 2026-04-06 | it83_cross_dataset_generalization_knn — GO ✓: generalización cross-dataset (synthetic_16ch + MNE proxy + BCI proxy) con kNN-k3. |
| 2026-04-06 | it84_cross_dataset_generalization_gaussian — GO ✓: generalización cross-dataset con grafo gaussiano. |
| 2026-04-06 | it85_cross_dataset_generalization_all_graphs — GO ✓: generalización cross-dataset con múltiples grafos (kNN, Gaussian, Kalofolias). |
| 2026-04-06 | it86_cross_dataset_generalization_high_mr — GO ✓: generalización cross-dataset en escenarios de alta pérdida (30-40%). |
| 2026-04-06 | it87_cross_dataset_generalization_few_missing — GO ✓: generalización cross-dataset en escenarios 1ch/2ch/3ch. |

### Iteraciones Fase 8 (it88-it94)

| Fecha | Entrada |
|-------|---------|
| 2026-04-06 | it88_robustness_noise_stress — GO ✓: robustez ante ruido aditivo. |
| 2026-04-06 | it89_robustness_artifact_stress — GO ✓: robustez ante artefactos no estacionarios. |
| 2026-04-06 | it90_robustness_graph_sensitivity — GO ✓: sensibilidad a cambios de topología de grafo. |
| 2026-04-06 | it91_robustness_method_subset_tv_focus — GO ✓: sensibilidad con subset de métodos TV/tiempo. |
| 2026-04-06 | it92_robustness_low_missing_stability — GO ✓: estabilidad en baja pérdida (10-20%). |
| 2026-04-06 | it93_robustness_high_missing_stability — GO ✓: estabilidad en alta pérdida (30-40%). |
| 2026-04-06 | it94_robustness_cross_proxy_shift — GO ✓: robustez bajo domain shift entre proxies/real. |

### Iteraciones Fase 9 (it95-it100)

| Fecha | Entrada |
|-------|---------|
| 2026-04-06 | it95_final_comparative_all_datasets — GO ✓: análisis comparativo final con datasets combinados. |
| 2026-04-06 | it96_final_comparative_top_graphs — GO ✓: comparativa final entre familias de grafos top. |
| 2026-04-06 | it97_final_comparative_top_methods — GO ✓: ranking comparativo final de métodos principales. |
| 2026-04-06 | it98_final_comparative_efficiency_tradeoff — GO ✓: comparativa calidad-eficiencia para decisión final. |
| 2026-04-06 | it99_final_comparative_consensus — GO ✓: consenso final multi-escenario. |
| 2026-04-06 | it100_final_comparative_publication_pack — GO ✓: paquete comparativo final publication-ready. |

### Iteraciones Fase 10 (it101-it104) — Trabajo futuro 8.3 (ya ejecutado)

| Fecha | Entrada |
|-------|---------|
| 2026-04-06 | it101_real_data_validation — GO ✓: validación con datos reales disponibles (`physionet_eegmmidb`), registrando bloqueo de MNE real (sin descarga) y BCI IV 2a real (sin `.gdf` local). |
| 2026-04-06 | it102_compute_time_tv_vs_instant — GO ✓: comparación de tiempo de cómputo TV vs Instant sobre datos reales disponibles. |
| 2026-04-06 | it103_tv_lambda_grid_search — GO ✓: grid search de parámetro λ/regularización en familia TV. |
| 2026-04-06 | it104_noise_sensitivity_tv — GO ✓: sensibilidad al ruido con niveles SNR inicial controlados (20/10/5/0 dB). |

### Iteraciones Fase 11–14 (it105-it118) — Expansión multidominio (EEG + no-EEG)

| Fecha | Entrada |
|-------|---------|
| 2026-04-07 | it105_real_eeg_crossdataset — NO-GO: validación cross-dataset real EEG (PhysioNet + BCI IV 2a S1), `p=1.0`, mejor método `trss`. |
| 2026-04-07 | it106_bci_iv2a_multisubject — NO-GO: validación multisujeto BCI IV 2a (S1-S3), `p=1.0`, mejor método `trss`. |
| 2026-04-07 | it107_mat100hz_baseline — NO-GO: baseline en dataset MAT 100Hz, `p=0.999`, mejor método `trss`. |
| 2026-04-07 | it108_mat100hz_lambda_grid — NO-GO: grid λ en MAT 100Hz, `p=1.0`, mejor método `trss`. |
| 2026-04-07 | it109_mat100hz_noise_sensitivity — NO-GO: sensibilidad a ruido en MAT 100Hz, `p=0.990`, mejor método `trss`. |
| 2026-04-07 | it110_iris_graph_baseline — NO-GO: baseline en tarea grafo-señal Iris, `p=0.787`, mejor método `trss`. |
| 2026-04-07 | it111_iris_graph_lambda_grid — NO-GO: grid λ en Iris, `p=1.0`, mejor método `trss`. |
| 2026-04-07 | it112_movielens_graph_baseline — NO-GO: baseline en MovieLens grafo-señal, `p=1.0`, mejor método `tv`. |
| 2026-04-07 | it113_movielens_graph_lambda_grid — NO-GO: grid λ en MovieLens, `p=1.0`, mejor método `tv`. |
| 2026-04-07 | it114_eeg_vs_iris_transfer — NO-GO: transferencia EEG vs Iris, `p=0.972`, mejor método `trss`. |
| 2026-04-07 | it115_eeg_vs_movielens_transfer — NO-GO: transferencia EEG vs MovieLens, `p=0.995`, mejor método `tv`. |
| 2026-04-07 | it116_all_new_datasets_comprehensive — NO-GO: corrida comprehensiva en datasets nuevos, `p=0.984`, mejor método `trss`. |
| 2026-04-07 | it117_graph_sensitivity_multidomain — NO-GO: sensibilidad a topología multidominio, `p=0.952`, mejor método `trss`. |
| 2026-04-07 | it118_runtime_family_multidomain — NO-GO: análisis de runtime por familia en multidominio, `p=0.697`, mejor método `trss`. |

### Iteraciones Fase 15 (it119-it120) — Cierre operativo completado

| Fecha | Entrada |
|-------|---------|
| 2026-04-07 | it119_noise_trend_multidomain — NO-GO: consolidación de tendencia SNR en EEG/no-EEG (TV median=0.3339, Instant median=0.2222, gain=-50.3%, `p=0.870`), mejor método `trss`, artefactos completos + 11 figuras. |
| 2026-04-07 | it120_final_multidomain_publication_pack — NO-GO: cierre operativo ejecutado con perfil controlado de destrabe (`seed_count=2`, `missing={0.2,0.4}`, `methods={mean,tikhonov,tv,trss}`), 6 datasets disponibles, 2 grafos, 192 filas, `p=0.0535`, gain=+0.5%, mejor método `trss`, artefactos completos + 11 figuras. |

### Estado de avance

- it61–it70: consolidación v6 en proxies externos.
- it71–it82: extensión v7 validada en artefactos, con resultados mixtos GO/NO-GO.
- it83–it87: completación de Fase 7 (generalización cross-dataset), GO ✓ en todas las corridas.
- it88–it94: Fase 8 (robustez/sensibilidad), GO ✓ en todas las corridas.
- it95–it100: Fase 9 (comparativa final), GO ✓ en todas las corridas.
- it101–it104: Fase 10 (trabajo futuro 8.3), GO ✓ en validación real disponible + cómputo + λ-grid + ruido.
- it105–it118: Fases 11–14 (expansión multidominio), ejecutadas con artefactos completos y resultado NO-GO en todas las corridas del bloque.
- it119: Fase 15 parcial ejecutada con artefactos completos (NO-GO).
- it120: Fase 15 cerrada operativamente con artefactos completos (NO-GO) mediante perfil controlado.
- Intento final exhaustivo de it120 ejecutado y detenido por runtime prolongado sin cierre operativo; cierre definitivo mantenido con perfil controlado (NO-GO).
- it121–it130: Fases 16–18 ejecutadas con artefactos completos; GO en it124/it125 y NO-GO en el resto.

### Iteraciones Fase 16–18 (it121-it130) — Ejecución final operativa

Se habilitó `experiments/run_future_work_it121_it130.py` con ejecución resiliente por lote y `--light-profile` (seeds/escenarios/métodos reducidos) para evitar bloqueos largos.

| Fecha | Entrada |
|-------|---------|
| 2026-04-07 | it121_domain_stratified_gate — NO-GO global (`p=0.992`, gain=-10.6%); estratificado: `eeg_real` NO-GO (`p=0.9996`) y `non_eeg` NO-GO (`p=0.9987`). |
| 2026-04-07 | it122_subjectwise_bci_holdout — NO-GO global (`p=0.9999`, gain=-89.4%); por sujeto S1/S2/S3 todos NO-GO. |
| 2026-04-07 | it123_graph_density_calibration — NO-GO (`p=0.1562`, gain=+28.3%); mejor método `trss`. |
| 2026-04-07 | it124_missing_pattern_realistic_v2 — GO (`p=0.0265`, gain=+43.5%); mejor método `trss`. |
| 2026-04-07 | it125_temporal_window_sensitivity — GO (`p=0.0232`, gain=+41.3%); mejor método `trss`. |
| 2026-04-07 | it126_metric_robustness_multiobjective — NO-GO global (`p=0.1197`, gain=+28.3%); se generó `*_pareto.csv` (frente con `tv`, `mean`, `trss`). |
| 2026-04-07 | it127_noise_profile_non_gaussian — NO-GO (`p=0.0555`, gain=+38.0%); mejor método `trss`. |
| 2026-04-07 | it128_calibration_by_dataset_family — NO-GO (`p=1.000`, gain=0.0%); mejor método `trss`. |
| 2026-04-07 | it129_confidence_interval_stability — NO-GO (`p=0.0589`, gain=+19.6%); bootstrap emitido. |
| 2026-04-07 | it130_final_decision_matrix — NO-GO (`p=0.1489`, gain=+0.5%); matriz final con recomendación `CONDICIONAL` en EEG clínico/BCI/no-EEG. |

Estado operativo acordado:
- `it120` exhaustivo se intentó por última vez y se da por **perdido** en esta ventana por runtime prolongado.
- `it121–it130` (incluyendo el bloque pendiente `it123–it130`) quedó ejecutado con artefactos completos.
- No quedan pendientes operativos del ciclo; `it120` queda cerrado con perfil controlado (NO-GO, `p=0.0535`).

## 17. Runtime exclusions and historical artifacts

Fecha: 2026-04-18

Nota breve: durante la revisión operativa se decidió excluir temporalmente ciertos métodos y un dataset de las ejecuciones automáticas para evitar reruns accidentales y concentrar recursos en métodos validados.

- Métodos excluidos de ejecuciones activas: `heat_diffusion_temporal`, `wavelet_temporal`.
- Método sujeto a revisión y excluido en esta fase: `directed_tv`.
- Dataset excluido de ejecuciones automáticas: `iv100hz_mat` (100 Hz MAT files).

Razón: estos métodos aparecen en artefactos históricos y planes previos; mantenerlos en el repositorio para trazabilidad, pero evitar su re-ejecución sin revisión científica adicional.

Acciones recomendadas:

- Los archivos de planificación (`experiments/run_future_work_*.py`, `experiments/propose_mapping_run_summary.json`, y orquestador/prompts) deben respetar estas exclusiones por defecto. Si un investigador necesita re-ejecutarlos, añadir una nota explicando la justificación y forzar explícitamente el método en la invocación.
- Añadir un archivo de aviso en `docs/HISTORICAL_ARTIFACTS_NOTICE.md` (creado automáticamente) que documente porqué estas entradas permanecen en el repo y cómo tratarlas.

Referencias (BibTeX keys): `Jiang2021`, `Giraldo2022`.
