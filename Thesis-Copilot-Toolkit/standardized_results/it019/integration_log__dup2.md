# Integration Log — it19_synthetic_beta_high_missing

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Synthetic beta band — high missing scenarios (30%, 40%) deep-dive

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

- Best method: **heat_diffusion_temporal** (MAE = 0.203)
- Best instant baseline MAE: 0.2039
- RMSE improvement: 23.4% at mr=0.3
- Significant contrast: mae_trss_vs_tikhonov (p=2.73e-03)