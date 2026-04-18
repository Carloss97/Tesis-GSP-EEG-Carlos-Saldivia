**Aviso de artefacto histórico:** Este archivo contiene resultados que hacen referencia a métodos/datasets ahora excluidos de ejecuciones activas. Ver [Thesis-Copilot-Toolkit/docs/HISTORICAL_ARTIFACTS_NOTICE.md](Thesis-Copilot-Toolkit/docs/HISTORICAL_ARTIFACTS_NOTICE.md).

# Integration Log — it18_directed_tv_vs_trss

**Decision**: GO ✓
**Date**: 2026-04-05
**Objective**: Best TV methods (directed_tv, trss, tv, graph_time_tikhonov) vs instant family — focused comparison

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
- RMSE improvement: 25.7% at mr=0.2
- Significant contrast: mae_trss_vs_tikhonov (p=7.05e-10)