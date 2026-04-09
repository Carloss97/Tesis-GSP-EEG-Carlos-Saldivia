# Integration Log — it14_low_missing_synthetic

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Low missing-channel scenarios (10% and 20%) — TV/Time advantage at mild degradation

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
- Significant contrast: mae_trss_vs_tikhonov (p=3.65e-12)