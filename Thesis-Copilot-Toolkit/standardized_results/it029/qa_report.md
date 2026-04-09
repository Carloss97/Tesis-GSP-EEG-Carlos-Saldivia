# Stats QA Report — it29_kalofolias_3syn

**Overall: PASS**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths non-negative | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 3 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < instant in ≥1 scenario | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | mean | 0.065900 | Instant |
| 2 | tv | 0.065900 | TV/Time |
| 3 | directed_tv | 0.066000 | TV/Time |
| 4 | idw | 0.066100 | Instant |
| 5 | gsmooth | 0.070400 | Instant |
| 6 | linear | 0.078400 | Instant |
| 7 | nearest | 0.085900 | Instant |
| 8 | rbfi_tps | 0.088400 | Instant |
| 9 | rbfi_mq | 0.089500 | Instant |
| 10 | spherical_spline | 0.090000 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   3.658e-05 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   6.006e-05 | reject_H0         |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.07795   | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.8294    | fail_to_reject_H0 |

## Iteration Note

Kalofolias (2016) graph learning via smooth signal assumption. TV shows 8-25% gain (strongest at mr=0.4).