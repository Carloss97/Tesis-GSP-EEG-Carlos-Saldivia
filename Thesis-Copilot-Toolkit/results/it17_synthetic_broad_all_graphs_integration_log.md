# Integration Log — it17_synthetic_broad_all_graphs

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: All 8 graph construction methods on synthetic_broad — topology comparison

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

- Best method: **directed_tv** (MAE = 0.0772)
- Best instant baseline MAE: 0.0831
- RMSE improvement: 21.5% at mr=0.4
- Significant contrast: mae_trss_vs_tikhonov (p=8.59e-05)