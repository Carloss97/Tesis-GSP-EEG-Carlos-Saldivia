# Integration Log — it31_strong_tv_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Strong TV methods only (directed_tv, tv, trss) vs instant — focused comparison

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
- RMSE improvement: 26.0% at mr=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=7.05e-10)