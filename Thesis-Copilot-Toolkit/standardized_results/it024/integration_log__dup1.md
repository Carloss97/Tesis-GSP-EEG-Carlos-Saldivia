# Integration Log — it24_physionet_all_scenarios

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Physionet real EEG — all 4 missing scenarios, family-level comparison

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

- Best method: **directed_tv** (MAE = 2e-06)
- Best instant baseline MAE: 2e-06
- RMSE improvement: 14.3% at mr=0.4
- Significant contrast: mae_trss_vs_tikhonov (p=6.02e-04)