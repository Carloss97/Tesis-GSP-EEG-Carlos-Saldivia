# QA Report: it95_final_comparative_all_datasets

## Status: GO

## Datasets
synthetic_16ch, synthetic_32ch, mne_sample_proxy, bci_competition_proxy, physionet_eegmmidb

## Summary
- Total rows: 420
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 4
- Best method: trss (MAE=1.7991e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.4634e-05
- Instant median MAE: 3.0851e-05
- Gain:               20.2%
- p-value:            2.2390e-05
- Decision:           **GO**

## Method Coverage
- mean: n=60 rows
- nearest: n=60 rows
- tikhonov: n=60 rows
- temporal_laplacian: n=60 rows
- graph_time_tikhonov: n=60 rows
- tv: n=60 rows
- trss: n=60 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T17:05:00.233209