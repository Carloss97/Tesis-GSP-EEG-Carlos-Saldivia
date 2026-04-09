# QA Report: it82_full_signal_recon_synthetic

## Status: NO-GO

## Datasets
synthetic_16ch

## Summary
- Total rows: 84
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 3
- Best method: mean (MAE=4.8466e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      5.3319e-01
- Instant median MAE: 5.6046e-01
- Gain:               4.9%
- p-value:            2.7088e-01
- Decision:           **NO-GO**

## Method Coverage
- mean: n=12 rows
- nearest: n=12 rows
- tikhonov: n=12 rows
- temporal_laplacian: n=12 rows
- graph_time_tikhonov: n=12 rows
- tv: n=12 rows
- trss: n=12 rows

## Proxy Note
Datasets reales o sintéticos estándar.

Generated: 2026-04-06T06:35:20.083968
