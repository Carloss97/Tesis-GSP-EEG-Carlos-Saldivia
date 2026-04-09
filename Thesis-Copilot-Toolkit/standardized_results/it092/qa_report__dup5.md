# QA Report: it92_robustness_low_missing_stability

## Status: GO

## Datasets
synthetic_32ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 336
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 2
- Best method: trss (MAE=1.3820e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.3255e-06
- Instant median MAE: 8.8249e-06
- Gain:               17.0%
- p-value:            4.6338e-07
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

Generated: 2026-04-06T17:04:55.137629