# Integration Log — it11_physionet_high_missing

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Physionet real EEG — high missing rate (40%) only, where TV family shows advantage

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

- Best method: **gsmooth** (MAE = 1.3e-05)
- Best instant baseline MAE: 1.3e-05
- RMSE improvement: 14.3% at mr=0.4
- Significant contrast: mae_trss_vs_tikhonov (p=1.09e-03)