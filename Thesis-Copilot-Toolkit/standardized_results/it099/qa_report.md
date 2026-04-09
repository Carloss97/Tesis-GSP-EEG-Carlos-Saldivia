# QA Report: it99_final_comparative_consensus

## Status: GO

## Datasets
synthetic_16ch, synthetic_32ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 672
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 4
- Best method: trss (MAE=2.2332e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.8216e-01
- Instant median MAE: 2.2082e-01
- Gain:               17.5%
- p-value:            9.1198e-14
- Decision:           **GO**

## Method Coverage
- mean: n=96 rows
- nearest: n=96 rows
- tikhonov: n=96 rows
- temporal_laplacian: n=96 rows
- graph_time_tikhonov: n=96 rows
- tv: n=96 rows
- trss: n=96 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:05:07.014550