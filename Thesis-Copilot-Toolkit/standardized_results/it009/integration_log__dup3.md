# Integration Log — it09_tikhonov_rbfi_focus

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: TV/Time vs classic spatial methods: tikhonov, rbfi_tps, rbfi_mq, spherical_spline

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

## Key Results

- Best method: **gsmooth** (MAE = 0.0658)
- Best instant baseline MAE: 0.0658
- RMSE improvement: 26.0% at missing_ratio=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=7.05e-10)

## Datasets

synthetic_alpha, synthetic_beta, synthetic_broad

## Note

Classic spatial interpolation methods (Tikhonov, RBF, spherical spline) are strong baselines. This iteration quantifies their gap with temporal-graph methods.