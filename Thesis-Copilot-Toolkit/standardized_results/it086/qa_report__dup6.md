# QA Report: it86_cross_dataset_generalization_high_mr

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 252
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 2
- Best method: trss (MAE=1.6649e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.7048e-06
- Instant median MAE: 9.5826e-06
- Gain:               19.6%
- p-value:            5.1160e-06
- Decision:           **GO**

## Method Coverage
- mean: n=36 rows
- nearest: n=36 rows
- tikhonov: n=36 rows
- temporal_laplacian: n=36 rows
- graph_time_tikhonov: n=36 rows
- tv: n=36 rows
- trss: n=36 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:04:44.941981