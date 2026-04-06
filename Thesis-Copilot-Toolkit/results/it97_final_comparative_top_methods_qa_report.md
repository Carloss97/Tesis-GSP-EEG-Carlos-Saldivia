# QA Report: it97_final_comparative_top_methods

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 432
- Methods tested: 6
- Graphs: 2
- Missing scenarios: 3
- Best method: trss (MAE=1.6329e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.5880e-06
- Instant median MAE: 8.5373e-06
- Gain:               11.1%
- p-value:            1.4259e-06
- Decision:           **GO**

## Method Coverage
- mean: n=72 rows
- tikhonov: n=72 rows
- temporal_laplacian: n=72 rows
- graph_time_tikhonov: n=72 rows
- tv: n=72 rows
- trss: n=72 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:05:03.604860