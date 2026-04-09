# QA Report: it89_robustness_artifact_stress

## Status: GO

## Datasets
synthetic_16ch, bci_competition_proxy

## Summary
- Total rows: 336
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 3
- Best method: trss (MAE=2.5852e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.3172e-01
- Instant median MAE: 2.4811e-01
- Gain:               6.6%
- p-value:            3.6508e-09
- Decision:           **GO**

## Method Coverage
- mean: n=48 rows
- nearest: n=48 rows
- tikhonov: n=48 rows
- temporal_laplacian: n=48 rows
- graph_time_tikhonov: n=48 rows
- tv: n=48 rows
- trss: n=48 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:04:50.015354