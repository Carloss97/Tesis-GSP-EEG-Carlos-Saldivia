# Integration Log — it03_synthetic_beta

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: TV/Time methods on synthetic_beta (beta band 13-30 Hz) — all scenarios

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

- Best method: **gsmooth** (MAE = 0.0657)
- Best instant baseline MAE: 0.0657
- RMSE improvement: 5.2% at missing_ratio=0.4
- Significant contrast: mae_trss_vs_tikhonov (p=8.90e-04)

## Datasets

synthetic_beta

## Note

Beta band EEG synthetic dataset. TV family expected to win at high missing rates.