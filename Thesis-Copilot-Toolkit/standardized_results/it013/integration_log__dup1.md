# Integration Log — it13_gaussian_aew_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Gaussian kernel + AEW (Adaptive Edge Weighting) graphs on 3 synthetic datasets

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

- Best method: **gsmooth** (MAE = 0.0656)
- Best instant baseline MAE: 0.0656
- RMSE improvement: 28.3% at mr=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=4.02e-03)