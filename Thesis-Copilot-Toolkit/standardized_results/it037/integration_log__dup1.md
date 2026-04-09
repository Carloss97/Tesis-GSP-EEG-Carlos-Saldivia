# Integration Log — it37_3syn_alpha_low_missing

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Synthetic alpha band — low missing scenarios (10%, 20%)

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

- Best method: **mean** (MAE = 0.0589)
- Best instant baseline MAE: 0.0589
- RMSE improvement: 23.1% at mr=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=5.09e-05)