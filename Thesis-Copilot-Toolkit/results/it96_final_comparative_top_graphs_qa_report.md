# QA Report: it96_final_comparative_top_graphs

## Status: GO

## Datasets
synthetic_16ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 504
- Methods tested: 7
- Graphs: 3
- Missing scenarios: 2
- Best method: trss (MAE=1.6350e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.5408e-06
- Instant median MAE: 9.3984e-06
- Gain:               19.8%
- p-value:            3.6142e-10
- Decision:           **GO**

## Method Coverage
- mean: n=72 rows
- nearest: n=72 rows
- tikhonov: n=72 rows
- temporal_laplacian: n=72 rows
- graph_time_tikhonov: n=72 rows
- tv: n=72 rows
- trss: n=72 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:05:01.876773