# Integration Log — it12_vknng_knng_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: VKNNG (variable k-NN) + KNNG (k-NN Gaussian) graphs on 3 synthetic datasets

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

- Best method: **gsmooth** (MAE = 0.0657)
- Best instant baseline MAE: 0.0657
- RMSE improvement: 26.2% at mr=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=4.29e-03)