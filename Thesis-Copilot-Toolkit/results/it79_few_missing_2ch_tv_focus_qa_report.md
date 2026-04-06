# QA Report: it79_few_missing_2ch_tv_focus

## Status: NO-GO

## Datasets
synthetic_16ch, synthetic_32ch, mne_sample_proxy, bci_competition_proxy, bci_competition_proxy_s2

## Summary
- Total rows: 35
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: tv (MAE=1.7789e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      6.9761e-06
- Instant median MAE: 6.7749e-06
- Gain:               -3.0%
- p-value:            4.2727e-01
- Decision:           **NO-GO**

## Method Coverage
- mean: n=5 rows
- nearest: n=5 rows
- tikhonov: n=5 rows
- temporal_laplacian: n=5 rows
- graph_time_tikhonov: n=5 rows
- tv: n=5 rows
- directed_tv: n=5 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T06:29:34.143587
