# Stats QA Report — it01_retry

**Overall: PASS**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths positive/finite | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 5 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < best instant MAE | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top Methods by MAE (median across scenarios)

| Rank | Method | MAE median | MAE mean | MAE std |
|------|--------|-----------|----------|---------|
| 1 | directed_tv | 0.0772 | 0.1648 | 0.0114 |
| 2 | heat_diffusion_temporal | 0.0804 | 0.3185 | 0.4518 |
| 3 | idw | 0.0831 | 0.1653 | 0.0000 |
| 4 | trss | 0.0833 | 0.1657 | 0.0048 |
| 5 | tv | 0.0842 | 0.1630 | 0.0019 |
| 6 | gsmooth | 0.0842 | 0.1628 | 0.0012 |
| 7 | gsp | 0.0853 | 0.1697 | 0.0060 |
| 8 | mean | 0.0853 | 0.1627 | 0.0000 |
| 9 | spherical_spline | 0.0853 | 0.1627 | 0.0000 |
| 10 | linear | 0.0943 | 0.1853 | 0.0000 |
| 11 | rbfi_tps | 0.0951 | 0.2023 | 0.0000 |
| 12 | spline_surface | 0.0951 | 0.2023 | 0.0000 |
| 13 | nearest | 0.1023 | 0.2023 | 0.0000 |
| 14 | rbfi_mq | 0.1077 | 0.2293 | 0.0000 |
| 15 | wavelet_temporal | 0.1108 | 0.1819 | 0.0098 |
| 16 | tikhonov | 0.1700 | 0.2778 | 0.1344 |
| 17 | graph_time_tikhonov | 0.3686 | 0.4080 | 0.1079 |
| 18 | puy | 0.3850 | 0.4090 | 0.1358 |
| 19 | temporal_laplacian | 0.4135 | 0.4503 | 0.0838 |
| 20 | bgsrp | 0.4409 | 0.4827 | 0.0510 |
| 21 | sobolev | 0.5498 | 0.5394 | 0.0735 |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   8.585e-05 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.02285   | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.3181    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   4.387e-06 | reject_H0         |

## Interpretation Note

- TV/Time family: `graph_time_tikhonov`, `trss`, `tv`.
- Bonferroni-adjusted alpha: 0.0100.
- Pseudo-seeds = 8 graph construction methods (knn_k3, knn_k5, nnk_k4, etc.).
- DTW not available in canonical run → DTW stats are NaN.
- INS-13 status: proxy Python-only — do not claim 1:1 MATLAB/GSPBox equivalence.