# Integration Log — it20_synthetic_alpha_high_missing

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Synthetic alpha band — high missing scenarios (30%, 40%) deep-dive

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

- Best method: **directed_tv** (MAE = 0.2019)
- Best instant baseline MAE: 0.2125
- RMSE improvement: 25.4% at mr=0.3
- Significant contrast: mae_trss_vs_tikhonov (p=3.69e-04)