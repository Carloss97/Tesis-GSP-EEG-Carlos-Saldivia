# QA Report: it80_few_missing_comprehensive

## Status: NO-GO

## Datasets
synthetic_16ch, mne_sample_proxy, bci_competition_proxy

## Summary
- Total rows: 36
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 3
- Best method: mean (MAE=1.3511e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.4892e-06
- Instant median MAE: 6.6744e-06
- Gain:               -12.2%
- p-value:            6.7680e-01
- Decision:           **NO-GO**

## Method Coverage
- mean: n=9 rows
- tikhonov: n=9 rows
- temporal_laplacian: n=9 rows
- tv: n=9 rows

## Proxy Note
MNE Sample y BCI Competition datasets son proxies sintéticos cuando los reales no están disponibles.

Generated: 2026-04-06T06:34:25.428865
