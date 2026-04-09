# Integration Log — it23b_knng_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: KNNG (k-NN Gaussian, k=4, sigma=1) on all 3 synthetic datasets

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

- Best method: **gsmooth** (MAE = 0.0658)
- Best instant baseline MAE: 0.0658
- RMSE improvement: 26.3% at mr=0.2
- Significant contrast: rmse_tv_family_vs_instant (p=2.61e-05)