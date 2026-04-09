# QA Report: it83_cross_dataset_generalization_knn

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 189
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 3
- Best method: trss (MAE=1.5756e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.3372e-06
- Instant median MAE: 8.7233e-06
- Gain:               15.9%
- p-value:            1.6128e-04
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

Generated: 2026-04-06T17:04:39.815669