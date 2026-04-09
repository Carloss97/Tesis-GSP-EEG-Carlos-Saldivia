# QA Report: it73_few_missing_1ch_mne_proxy

## Status: GO

## Datasets
mne_sample_proxy

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: temporal_laplacian (MAE=1.2467e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.4415e-06
- Instant median MAE: 1.9010e-06
- Gain:               24.2%
- p-value:            2.0932e-02
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

Generated: 2026-04-06T06:05:34.955898
