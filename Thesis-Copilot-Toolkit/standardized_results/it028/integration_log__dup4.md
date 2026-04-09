# Integration Log — it28_nnk_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: NNK k=4 (non-negative kernel) graph on 3 synthetic datasets

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

- Best method: **gsmooth** (MAE = 0.0651)
- Best instant baseline MAE: 0.0651
- RMSE improvement: 22.7% at mr=0.2
- Significant contrast: rmse_tv_family_vs_instant (p=8.79e-06)