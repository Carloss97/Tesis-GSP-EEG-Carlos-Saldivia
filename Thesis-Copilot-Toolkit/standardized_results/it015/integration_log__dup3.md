# Integration Log — it15b_gaussian_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Gaussian kernel graph (sigma=1) on all 3 synthetic datasets

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

- Best method: **trss** (MAE = 0.0651)
- Best instant baseline MAE: 0.0652
- RMSE improvement: 29.0% at mr=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=1.35e-03)