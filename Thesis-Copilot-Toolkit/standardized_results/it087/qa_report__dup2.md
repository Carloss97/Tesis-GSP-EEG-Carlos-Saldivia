# QA Report: it87_cross_dataset_generalization_few_missing

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 189
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 3
- Best method: trss (MAE=1.7037e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.9192e-06
- Instant median MAE: 9.1921e-06
- Gain:               13.8%
- p-value:            1.3147e-03
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

Generated: 2026-04-06T17:04:46.658624