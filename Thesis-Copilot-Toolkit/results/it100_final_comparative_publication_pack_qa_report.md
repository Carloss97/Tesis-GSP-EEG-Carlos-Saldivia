# QA Report: it100_final_comparative_publication_pack

## Status: GO

## Datasets
synthetic_16ch, synthetic_32ch, mne_sample_proxy, bci_competition_proxy, physionet_eegmmidb

## Summary
- Total rows: 1260
- Methods tested: 7
- Graphs: 3
- Missing scenarios: 4
- Best method: trss (MAE=1.7959e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.4588e-05
- Instant median MAE: 3.1447e-05
- Gain:               21.8%
- p-value:            8.4788e-15
- Decision:           **GO**

## Method Coverage
- mean: n=180 rows
- nearest: n=180 rows
- tikhonov: n=180 rows
- temporal_laplacian: n=180 rows
- graph_time_tikhonov: n=180 rows
- tv: n=180 rows
- trss: n=180 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:05:08.792830