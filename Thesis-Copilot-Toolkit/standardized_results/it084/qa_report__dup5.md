# QA Report: it84_cross_dataset_generalization_gaussian

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 189
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 3
- Best method: trss (MAE=1.6929e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.9842e-06
- Instant median MAE: 9.2777e-06
- Gain:               13.9%
- p-value:            4.8185e-04
- Decision:           **GO**

## Method Coverage
- mean: n=27 rows
- nearest: n=27 rows
- tikhonov: n=27 rows
- temporal_laplacian: n=27 rows
- graph_time_tikhonov: n=27 rows
- tv: n=27 rows
- trss: n=27 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:04:41.599964