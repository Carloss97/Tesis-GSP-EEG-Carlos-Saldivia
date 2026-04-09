# Integration Log — it29_kalofolias_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Kalofolias graph learning on 3 synthetic datasets

## Go/No-Go

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

- Best method: **mean** (MAE = 0.0659)
- Best instant baseline MAE: 0.0659
- RMSE improvement: 25.5% at mr=0.4
- Significant contrast: mae_trss_vs_tikhonov (p=3.66e-05)