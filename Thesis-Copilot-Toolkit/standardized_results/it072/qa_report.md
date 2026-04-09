# QA Report: it72_few_missing_2ch_synthetic

## Status: NO-GO

## Datasets
synthetic_16ch

## Summary
- Total rows: 24
- Methods tested: 8
- Graphs: 1
- Missing scenarios: 1
- Best method: mean (MAE=4.0763e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      4.4411e-01
- Instant median MAE: 4.9821e-01
- Gain:               10.9%
- p-value:            4.0453e-01
- Decision:           **NO-GO**

## Method Coverage
- mean: n=3 rows
- nearest: n=3 rows
- linear: n=3 rows
- tikhonov: n=3 rows
- gsp: n=3 rows
- temporal_laplacian: n=3 rows
- graph_time_tikhonov: n=3 rows
- tv: n=3 rows

## Proxy Note
Datasets reales o sintéticos estándar.

Generated: 2026-04-06T05:59:23.122773
