# Integration Log — it02

**Decision**: GO ✓
**Date**: 2026-04-05
**Iteration tag**: it02
**Objective**: TV/Time methods on synthetic_broad — corrected per-scenario RMSE comparison (G2 median-based)

## Go/No-Go Criteria

| Criterion | Result |
|-----------|--------|
| G1 MAE improvement | PASS |
| G2 RMSE improvement | PASS |
| G3 Significance | PASS |
| G4 CI95 non-degenerate | PASS |
| G5 QA gates | PASS |
| G6 Mandatory artefacts | PASS |
| G7 Error rate | PASS |

## Artefacts Produced

### Raw Results
- `results/it02_raw.csv` (704 rows)
- `results/it02_run_metadata.json`

### Statistics
- `results/it02_stats.csv`
- `results/it02_significance.csv`
- `results/it02_qa_report.md` (overall: PASS)

### Figures (6)
- `results/it02_figures/fig01_mae_by_method.pdf`
- `results/it02_figures/fig02_rmse_boxplot.pdf`
- `results/it02_figures/fig03_snr_heatmap.pdf`
- `results/it02_figures/fig04_dtw_comparison.pdf`
- `results/it02_figures/fig05_tv_vs_instant_family.pdf`
- `results/it02_figures/fig06_scenario_sensitivity.pdf`

### Tables (2)
- `results/it02_tables/tbl01_main_comparison.tex`
- `results/it02_tables/tbl02_significance.tex`

### Manuscript Integration
- Appended to: `paper/ieee/sections/results.tex`
- Appended to: `thesis/usm/chapters/04_experimentos_y_resultados.tex`
- Figures copied to: `paper/ieee/figures/` and `thesis/usm/figures/`
- Tables copied to: `paper/ieee/tables/` and `thesis/usm/tables/`

## Key Results

- Best method: **directed_tv** (MAE = 0.0772)
- Best instant baseline MAE: 0.0831
- RMSE improvement (TV/Time vs instant): 5.9%
- Significant contrast: mae_trss_vs_tikhonov (p=8.59e-05)

## INS-13 Disclaimer

Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.