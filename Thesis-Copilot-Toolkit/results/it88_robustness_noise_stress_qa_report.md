# QA Report: it88_robustness_noise_stress

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy

## Summary
- Total rows: 336
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 3
- Best method: trss (MAE=2.3651e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.1209e-01
- Instant median MAE: 2.4571e-01
- Gain:               13.7%
- p-value:            6.1505e-14
- Decision:           **GO**

## Method Coverage
- mean: n=48 rows
- nearest: n=48 rows
- tikhonov: n=48 rows
- temporal_laplacian: n=48 rows
- graph_time_tikhonov: n=48 rows
- tv: n=48 rows
- trss: n=48 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:04:48.280908