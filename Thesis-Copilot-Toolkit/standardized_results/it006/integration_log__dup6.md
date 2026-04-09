# Integration Log — it06b_kalofolias_nnk_3syn

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Kalofolias + NNK graphs on all 3 synthetic datasets — learnable graph topology

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
- RMSE improvement: 25.3% at missing_ratio=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=3.21e-04)

## Datasets

synthetic_alpha, synthetic_beta, synthetic_broad

## Note

Kalofolias (learnable graph by Kalofolias et al.) and NNK (non-negative kernel) graph construction methods. n=2 graphs × 3 datasets = 6 per group.