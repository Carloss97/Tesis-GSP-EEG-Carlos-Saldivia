# Stats QA Report — it01

**Overall: FAIL**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths positive/finite | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 5 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < best instant MAE | FAIL |
| QA-07 | No duplicate stats rows | PASS |

## Top Methods by MAE (median across scenarios)

| Rank | Method | MAE median | MAE mean | MAE std |
|------|--------|-----------|----------|---------|
| 1 | mean | 0.0589 | 0.1307 | 0.0000 |
| 2 | idw | 0.0626 | 0.1369 | 0.0000 |
| 3 | tv | 0.0633 | 0.1359 | 0.0052 |
| 4 | linear | 0.0634 | 0.1659 | 0.0000 |
| 5 | nearest | 0.0643 | 0.1777 | 0.0000 |
| 6 | gsmooth | 0.0652 | 0.1373 | 0.0034 |
| 7 | heat_diffusion_temporal | 0.0708 | 0.2739 | 0.3871 |
| 8 | trss | 0.0795 | 0.1510 | 0.0135 |
| 9 | gsp | 0.0808 | 0.1594 | 0.0208 |
| 10 | wavelet_temporal | 0.0827 | 0.1459 | 0.0048 |
| 11 | rbfi_tps | 0.0884 | 0.1835 | 0.0000 |
| 12 | rbfi_mq | 0.0895 | 0.1893 | 0.0000 |
| 13 | directed_tv | 0.0958 | 0.1568 | 0.0183 |
| 14 | spherical_spline | 0.1110 | 0.2287 | 0.0000 |
| 15 | tikhonov | 0.1695 | 0.2653 | 0.1264 |
| 16 | spline_surface | 0.2117 | 0.3014 | 0.0000 |
| 17 | graph_time_tikhonov | 0.3562 | 0.3944 | 0.1090 |
| 18 | puy | 0.3909 | 0.4137 | 0.1324 |
| 19 | temporal_laplacian | 0.4036 | 0.4465 | 0.0867 |
| 20 | bgsrp | 0.5112 | 0.5326 | 0.0262 |
| 21 | sobolev | 0.5529 | 0.5430 | 0.0682 |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.0001822 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.08512   | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.3997    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.001331  | reject_H0         |

## Interpretation Note

- TV/Time family: `graph_time_tikhonov`, `trss`, `tv`.
- Bonferroni-adjusted alpha: 0.0100.
- Pseudo-seeds = 8 graph construction methods (knn_k3, knn_k5, nnk_k4, etc.).
- DTW not available in canonical run → DTW stats are NaN.
- INS-13 status: proxy Python-only — do not claim 1:1 MATLAB/GSPBox equivalence.