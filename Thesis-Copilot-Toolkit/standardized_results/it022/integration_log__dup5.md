# Integration Log — it22b_knn_k3_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: KNN k=3 graph on all 3 synthetic datasets — minimal nearest-neighbor topology

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

- Best method: **gsmooth** (MAE = 0.0653)
- Best instant baseline MAE: 0.0653
- RMSE improvement: 21.5% at mr=0.1
- Significant contrast: rmse_tv_family_vs_instant (p=3.78e-05)