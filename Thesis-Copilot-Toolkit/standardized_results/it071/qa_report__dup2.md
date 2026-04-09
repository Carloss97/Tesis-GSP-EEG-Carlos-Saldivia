# QA Report: it71_few_missing_1ch_synthetic

## Status: NO-GO

## Datasets
synthetic_16ch

## Summary
- Total rows: 24
- Methods tested: 8
- Graphs: 1
- Missing scenarios: 1
- Best method: mean (MAE=3.8237e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      4.2933e-01
- Instant median MAE: 5.1805e-01
- Gain:               17.1%
- p-value:            9.1927e-02
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

Generated: 2026-04-06T05:59:11.981997
