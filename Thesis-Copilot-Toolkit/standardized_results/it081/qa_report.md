# QA Report: it81_instant_vs_full_synthetic

## Status: NO-GO

## Datasets
synthetic_16ch

## Summary
- Total rows: 20
- Methods tested: 5
- Graphs: 1
- Missing scenarios: 2
- Best method: mean (MAE=4.8602e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      5.1150e-01
- Instant median MAE: 5.0832e-01
- Gain:               -0.6%
- p-value:            9.0933e-01
- Decision:           **NO-GO**

## Method Coverage
- mean: n=4 rows
- tikhonov: n=4 rows
- temporal_laplacian: n=4 rows
- tv: n=4 rows
- graph_time_tikhonov: n=4 rows

## Proxy Note
Datasets reales o sintéticos estándar.

Generated: 2026-04-06T06:34:49.240314
