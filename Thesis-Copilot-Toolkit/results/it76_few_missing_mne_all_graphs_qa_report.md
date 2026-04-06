# QA Report: it76_few_missing_mne_all_graphs

## Status: NO-GO

## Datasets
mne_sample_proxy

## Summary
- Total rows: 24
- Methods tested: 4
- Graphs: 3
- Missing scenarios: 2
- Best method: temporal_laplacian (MAE=1.4816e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.6457e-06
- Instant median MAE: 1.6579e-06
- Gain:               0.7%
- p-value:            2.9135e-01
- Decision:           **NO-GO**

## Method Coverage
- mean: n=6 rows
- tikhonov: n=6 rows
- temporal_laplacian: n=6 rows
- tv: n=6 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T06:24:44.533959
