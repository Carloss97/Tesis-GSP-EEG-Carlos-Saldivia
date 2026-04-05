# Integration Log — it32_3syn_mr20_only

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Moderate missing rate (20%) on 3 synthetic datasets — single scenario deep-dive

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

- Best method: **mean** (MAE = 0.1252)
- Best instant baseline MAE: 0.1252
- RMSE improvement: 26.0% at mr=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=7.81e-08)