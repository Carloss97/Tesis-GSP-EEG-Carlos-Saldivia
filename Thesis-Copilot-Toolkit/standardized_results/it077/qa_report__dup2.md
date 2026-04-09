# QA Report: it77_few_missing_bci_all_graphs

## Status: NO-GO

## Datasets
bci_competition_proxy

## Summary
- Total rows: 24
- Methods tested: 4
- Graphs: 3
- Missing scenarios: 2
- Best method: mean (MAE=6.5941e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.2640e-06
- Instant median MAE: 6.5941e-06
- Gain:               -10.2%
- p-value:            9.8261e-01
- Decision:           **NO-GO**

## Method Coverage
- mean: n=6 rows
- tikhonov: n=6 rows
- temporal_laplacian: n=6 rows
- tv: n=6 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T06:25:23.788991
