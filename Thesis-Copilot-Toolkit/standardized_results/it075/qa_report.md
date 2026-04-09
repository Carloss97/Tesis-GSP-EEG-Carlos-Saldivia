# QA Report: it75_few_missing_multi_synthetic

## Status: NO-GO

## Datasets
synthetic_16ch, synthetic_32ch, synthetic_8ch

## Summary
- Total rows: 60
- Methods tested: 5
- Graphs: 1
- Missing scenarios: 2
- Best method: mean (MAE=4.1723e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      5.4917e-01
- Instant median MAE: 4.4003e-01
- Gain:               -24.8%
- p-value:            9.6991e-01
- Decision:           **NO-GO**

## Method Coverage
- mean: n=12 rows
- nearest: n=12 rows
- tikhonov: n=12 rows
- temporal_laplacian: n=12 rows
- tv: n=12 rows

## Proxy Note
Datasets reales o sintéticos estándar.

Generated: 2026-04-06T06:12:49.194021
