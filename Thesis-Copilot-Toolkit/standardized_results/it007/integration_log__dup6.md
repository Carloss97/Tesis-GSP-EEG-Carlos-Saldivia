# Integration Log — it07b_knn_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: KNN graphs (k=3 and k=5) on all 3 synthetic datasets — KNN topology analysis

## Go/No-Go Criteria

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

- Best method: **mean** (MAE = 0.0659)
- Best instant baseline MAE: 0.0659
- RMSE improvement: 24.7% at missing_ratio=0.3
- Significant contrast: mae_trss_vs_tikhonov (p=1.78e-03)

## Datasets

synthetic_alpha, synthetic_beta, synthetic_broad

## Note

KNN graphs are widely used in practice. n=2 graphs × 3 datasets = 6 per group. TV family shows 16-24% family RMSE gain.