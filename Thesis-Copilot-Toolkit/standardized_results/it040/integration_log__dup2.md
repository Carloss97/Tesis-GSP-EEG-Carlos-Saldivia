# Integration Log — it40_3syn_all_mr_analysis

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: KNN graphs (k=3 and k=5) on 3 synthetic datasets — full missing rate comparison

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
- RMSE improvement: 24.7% at mr=0.3
- Significant contrast: mae_trss_vs_tikhonov (p=1.78e-03)