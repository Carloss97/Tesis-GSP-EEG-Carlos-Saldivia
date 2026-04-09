# Integration Log — it33_3syn_mr30_only

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Moderate-high missing rate (30%) on 3 synthetic datasets — single scenario deep-dive

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

- Best method: **directed_tv** (MAE = 0.2026)
- Best instant baseline MAE: 0.2039
- RMSE improvement: 24.9% at mr=0.3
- Significant contrast: mae_trss_vs_tikhonov (p=1.23e-07)