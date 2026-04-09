# Integration Log — it38_broad_gaussian_kalofolias_nnk

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: synthetic_broad with 3 complementary graphs: Gaussian, Kalofolias, NNK

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

- Best method: **heat_diffusion_temporal** (MAE = 0.0813)
- Best instant baseline MAE: 0.0831
- RMSE improvement: 22.1% at mr=0.4
- Significant contrast: mae_trss_vs_tikhonov (p=3.55e-03)