# QA Report: it91_robustness_method_subset_tv_focus

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy

## Summary
- Total rows: 180
- Methods tested: 6
- Graphs: 1
- Missing scenarios: 3
- Best method: trss (MAE=2.2486e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.0935e-01
- Instant median MAE: 2.4715e-01
- Gain:               15.3%
- p-value:            6.3005e-08
- Decision:           **GO**

## Method Coverage
- mean: n=30 rows
- tikhonov: n=30 rows
- temporal_laplacian: n=30 rows
- graph_time_tikhonov: n=30 rows
- tv: n=30 rows
- trss: n=30 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:04:53.414163