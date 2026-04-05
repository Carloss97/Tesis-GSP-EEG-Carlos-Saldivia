# Integration Log — it16b_vknng_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: VKNNG (variable k-NN, alpha=1, kmin=2, kmax=8) on all 3 synthetic datasets

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

- Best method: **tv** (MAE = 0.0655)
- Best instant baseline MAE: 0.0657
- RMSE improvement: 26.8% at mr=0.2
- Significant contrast: rmse_tv_family_vs_instant (p=4.87e-05)