# QA Report: it90_robustness_graph_sensitivity

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 378
- Methods tested: 7
- Graphs: 3
- Missing scenarios: 2
- Best method: trss (MAE=1.6770e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.6787e-06
- Instant median MAE: 9.4884e-06
- Gain:               19.1%
- p-value:            1.4019e-07
- Decision:           **GO**

## Method Coverage
- mean: n=54 rows
- nearest: n=54 rows
- tikhonov: n=54 rows
- temporal_laplacian: n=54 rows
- graph_time_tikhonov: n=54 rows
- tv: n=54 rows
- trss: n=54 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:04:51.760720