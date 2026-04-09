# Integration Log — it21_all_datasets_family

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: All 4 datasets pooled — family-level G2 comparison across synthetic and real EEG

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

- Best method: **mean** (MAE = 0.0624)
- Best instant baseline MAE: 0.0624
- RMSE improvement: 25.4% at mr=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=9.04e-06)