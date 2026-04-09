# QA Report: it93_robustness_high_missing_stability

## Status: GO

## Datasets
synthetic_32ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 336
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 2
- Best method: trss (MAE=1.4920e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.8574e-06
- Instant median MAE: 9.7761e-06
- Gain:               19.6%
- p-value:            2.4926e-07
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

Generated: 2026-04-06T17:04:56.791858