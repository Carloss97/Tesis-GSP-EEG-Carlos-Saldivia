# Integration Log — it25_alpha_beta_two_bands

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Two-band analysis (alpha 8-13Hz + beta 13-30Hz) — no broadband EEG

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
- RMSE improvement: 25.6% at mr=0.3
- Significant contrast: mae_trss_vs_tikhonov (p=1.40e-06)