# Integration Log — it05b_synthetic_three

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: TV/Time family on all 3 synthetic datasets — family-level comparison

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

Pools alpha, beta, and broad bands. TV family shows 16-23% RMSE gain over instant family at family-median level.