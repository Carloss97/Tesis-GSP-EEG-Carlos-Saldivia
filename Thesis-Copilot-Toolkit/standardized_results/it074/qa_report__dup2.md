# QA Report: it74_few_missing_2ch_mne_proxy

## Status: GO

## Datasets
mne_sample_proxy

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: temporal_laplacian (MAE=1.7011e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.7502e-06
- Instant median MAE: 2.1790e-06
- Gain:               19.7%
- p-value:            5.2338e-03
- Decision:           **GO**

## Method Coverage
- mean: n=2 rows
- nearest: n=2 rows
- linear: n=2 rows
- tikhonov: n=2 rows
- temporal_laplacian: n=2 rows
- graph_time_tikhonov: n=2 rows
- tv: n=2 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T06:11:38.776050
