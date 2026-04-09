# QA Report: it94_robustness_cross_proxy_shift

## Status: GO

## Datasets
mne_sample_proxy, bci_competition_proxy, physionet_eegmmidb

## Summary
- Total rows: 336
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 2
- Best method: trss (MAE=1.2496e-05)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      8.3485e-06
- Instant median MAE: 9.1758e-06
- Gain:               9.0%
- p-value:            5.3323e-04
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

Generated: 2026-04-06T17:04:58.520267