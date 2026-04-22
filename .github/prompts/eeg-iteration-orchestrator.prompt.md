---
description: 'Master orchestrator for EEG-GSP iterative experiments. Runs agents in strict order: Runner → Stats QA → Viz/Tables → Integrator. Evaluates Go/No-Go gate before manuscript integration.'
agent: agent
tools:
  - run_in_terminal
  - read_file
  - write_file
  - create_file
  - list_directory
argument-hint: 'dataset=<name> scenarios=<list> seeds=<range> iteration_tag=<tag> objective=<text>'
---

# EEG Iteration Orchestrator

## Mission

Coordinate one full experimental iteration across the four specialized agents in strict order.
Emit a structured iteration report and enforce the Go/No-Go gate before any manuscript integration.

## Required Inputs

| Field | Type | Example |
|-------|------|---------|
| `dataset` | string | `synthetic_alpha`, `physionet_eegmmidb`, `all` |
| `scenarios` | list | `["10pct","20pct","30pct"]`, `["1ch_random","2ch_nearby"]` or `"all"` |
| `seeds` | range | `0-29` (10–30 seeds recommended) |
| `iteration_tag` | string | `it01`, `it02_tv_focus` |
| `objective` | string | Short free-text goal for this iteration |
| `normalize` (optional) | bool or env | `true` or set `NORMALIZE_DATASETS=1` (writes to `results_normalized_*`) |
| `missing_mode` (optional) | string | `random` (default) or `nearby` (spatially-adjacent removals) |

## Strict Execution Order

```
Phase 1 ── Runner Agent       (eeg-runner-agent.prompt.md)
Phase 2 ── Stats QA Agent     (eeg-stats-qa-agent.prompt.md)
Phase 3 ── Viz/Tables Agent   (eeg-viz-tables-agent.prompt.md)
Phase 4 ── Integrator Agent   (eeg-writer-integrator-agent.prompt.md)   ← only on Go
```

**Never skip a phase. Never run Integrator on a No-Go iteration.**

## Phase Contracts

### Phase 1 — Runner Agent

**Entry contract (inputs the orchestrator passes):**
- `iteration_tag`, `dataset`, `scenarios`, `seeds`
- Working directory: `Thesis-Copilot-Toolkit/`

Note: the orchestrator may include `normalize` and `missing_mode` in the inputs; the Runner must record these in `*_run_metadata.json` (fields: `normalization`, `missing_mode`).

**Exit contract (artefacts the Runner must produce):**
- `results/<iteration_tag>_raw.csv` — one row per (dataset, graph, method, scenario, seed)
- `results/<iteration_tag>_run_metadata.json` — reproducibility metadata
- Console summary with total rows, datasets covered, missing/errored combinations

The raw CSV should carry the extended metric set used by the current pipeline (`mae`, `rmse`, `snr`, `dtw`, `lsd`, `coherence_mean`) and the serialized reconstructed signal when available.

When `run_schedule_in_batches.py` is used, the orchestrator must expect canonical graph names in the batch files and allow the pilot runner to normalize legacy aliases before execution.

**Failure condition:** If the CSV is missing or has fewer rows than `(|datasets| × |graphs| × |methods| × |scenarios| × |seeds|) × 0.80`, halt and report Phase 1 failure.

### Phase 2 — Stats QA Agent

**Entry contract:**
- `results/<iteration_tag>_raw.csv` from Phase 1

**Exit contract:**
- `results/<iteration_tag>_stats.csv` — per-(method, scenario) mean ± std, CI95 for MAE, RMSE, SNR, LSD, coherence_mean (and DTW if available)
- `results/<iteration_tag>_significance.csv` — Wilcoxon/Mann-Whitney p-values for key contrasts
- `results/<iteration_tag>_qa_report.md` — checklist of QA tests passed/failed

**Failure condition:** Any QA gate flagged as FAIL (see Stats QA agent criteria).

### Phase 3 — Viz/Tables Agent

**Entry contract:**
- `results/<iteration_tag>_raw.csv`
- `results/<iteration_tag>_stats.csv`
- `results/<iteration_tag>_significance.csv`

**Exit contract:**
All artefacts saved under `results/<iteration_tag>_figures/` and `results/<iteration_tag>_tables/`:
- `<dataset>_familia_metricas_promedio.pdf` (2x3 family means for MAE/RMSE/DTW/SNR/LSD/coherence_mean)
- `<dataset>_familia_metricas_dispersion.pdf` (2x3 family dispersion for the same metrics)
- `<dataset>_combinacion_detallada_mae.pdf`
- `<dataset>_combinacion_detallada_rmse.pdf`
- `<dataset>_combinacion_detallada_dtw.pdf`
- `<dataset>_combinacion_detallada_snr.pdf`
- `<dataset>_combinacion_detallada_lsd.pdf`
- `<dataset>_combinacion_detallada_coherence_mean.pdf`
- `tbl01_main_comparison.tex` — LaTeX table: method vs scenario, MAE/RMSE/SNR
- `tbl02_significance.tex` — LaTeX table: key pairwise p-values

**Failure condition:** Any mandatory figure or table is missing.

### Phase 4 — Writer/Integrator Agent

**Entry contract (only reached on Go):**
- All Phase 3 artefacts
- `results/<iteration_tag>_qa_report.md`
- Target document sections to update

**Exit contract:**
- Updated LaTeX sections in `paper/ieee/sections/` and `thesis/usm/chapters/`
- Figures copied to `paper/ieee/figures/` and `thesis/usm/figures/`
- Tables copied to `paper/ieee/tables/` and `thesis/usm/tables/`
- `results/<iteration_tag>_integration_log.md` — traceability record

## Go/No-Go Gate

Evaluate after Phase 3. Decision is **Go** only when ALL criteria pass:

| # | Criterion | Threshold | Source |
|---|-----------|-----------|--------|
| G1 | MAE best method ≤ MAE best baseline | strict `<` | `_stats.csv` |
| G2 | RMSE improvement vs baseline | ≥ 5 % reduction | `_stats.csv` |
| G3 | At least one key contrast significant | p < 0.05 Bonferroni-adjusted | `_significance.csv` |
| G4 | CI95 widths are finite and non-degenerate | all CI widths > 0 | `_stats.csv` |
| G5 | No QA gate marked FAIL | 0 failures | `_qa_report.md` |
| G6 | All mandatory figures and tables present | For each dataset: 8 figures (6 combinations + 2 family summaries) + 2 tables per iteration | Phase 3 artefacts |
| G7 | Fewer than 10 % of combinations errored | < 10 % error rate | `_run_metadata.json` |

### Verdict emission

```
[ORCHESTRATOR] Iteration: <iteration_tag>
Objective   : <objective>
Dataset(s)  : <dataset>
Seeds       : <seeds>
──────────────────────────────
G1 MAE improvement        : PASS / FAIL
G2 RMSE improvement       : PASS / FAIL
G3 Significance           : PASS / FAIL
G4 CI95 non-degenerate    : PASS / FAIL
G5 QA gates               : PASS / FAIL
G6 Mandatory artefacts    : PASS / FAIL
G7 Error rate             : PASS / FAIL
──────────────────────────────
DECISION: GO ✓  /  NO-GO ✗
```

On **No-Go**: stop. Document reason in `results/<iteration_tag>_nogo_report.md`.
On **Go**: delegate to Phase 4 (Integrator).

## Iteration Naming Convention

- Tags must be lowercase, alphanumeric + underscores: `it01`, `it02_tv`, `it03_physionet`.
- Never reuse a tag. Append suffix `_retry` if re-running a failed iteration.

## File Locations Reference

| Artefact type | Location |
|---------------|----------|
| Raw CSV | `Thesis-Copilot-Toolkit/results/<tag>_raw.csv` |
| Stats CSV | `Thesis-Copilot-Toolkit/results/<tag>_stats.csv` |
| Significance CSV | `Thesis-Copilot-Toolkit/results/<tag>_significance.csv` |
| QA report | `Thesis-Copilot-Toolkit/results/<tag>_qa_report.md` |
| Figures | `Thesis-Copilot-Toolkit/results/<tag>_figures/` |
| Tables | `Thesis-Copilot-Toolkit/results/<tag>_tables/` |
| No-Go report | `Thesis-Copilot-Toolkit/results/<tag>_nogo_report.md` |
| Integration log | `Thesis-Copilot-Toolkit/results/<tag>_integration_log.md` |
| Paper figures | `Thesis-Copilot-Toolkit/paper/ieee/figures/` |
| Paper tables | `Thesis-Copilot-Toolkit/paper/ieee/tables/` |
| Thesis figures | `Thesis-Copilot-Toolkit/thesis/usm/figures/` |
| Thesis tables | `Thesis-Copilot-Toolkit/thesis/usm/tables/` |

## Operational Notes

- Use small iterations (10–30 seeds) for rapid feedback. Scale to 50–100 seeds for final runs.
- One iteration = one `iteration_tag`. Do not mix tags.
- All paths are relative to the repository root.
- Language: figures/tables captions in English (paper) and Spanish (thesis).
- Results from No-Go iterations are retained in `results/` for diagnostics but never cited in the manuscript.
