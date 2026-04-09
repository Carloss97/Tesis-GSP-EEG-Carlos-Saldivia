# Integration Log — it08_high_missing_synthetic

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: High missing-channel scenarios (30% and 40%) — TV/Time advantage most pronounced

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

- Best method: **directed_tv** (MAE = 0.2026)
- Best instant baseline MAE: 0.2039
- RMSE improvement: 24.9% at missing_ratio=0.3
- Significant contrast: mae_trss_vs_tikhonov (p=9.23e-10)

## Datasets

synthetic_alpha, synthetic_beta, synthetic_broad

## Note

TV methods show greatest advantage under high missing-channel rates. Family RMSE gain exceeds 20% at these scenarios.