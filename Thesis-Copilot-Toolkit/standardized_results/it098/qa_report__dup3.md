# QA Report: it98_final_comparative_efficiency_tradeoff

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy

## Summary
- Total rows: 420
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 3
- Best method: trss (MAE=2.4802e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.2664e-01
- Instant median MAE: 2.4131e-01
- Gain:               6.1%
- p-value:            4.8477e-14
- Decision:           **GO**

## Method Coverage
- mean: n=60 rows
- nearest: n=60 rows
- tikhonov: n=60 rows
- temporal_laplacian: n=60 rows
- graph_time_tikhonov: n=60 rows
- tv: n=60 rows
- trss: n=60 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:05:05.370564