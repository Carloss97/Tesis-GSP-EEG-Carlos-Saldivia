# Stats QA Report — it30_knn_k5_3syn

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
| 3 | idw | 0.066100 | Instant |
| 4 | gsmooth | 0.067400 | Instant |
| 5 | heat_diffusion_temporal | 0.069500 | TV/Time |
| 6 | trss | 0.071400 | TV/Time |
| 7 | gsp | 0.071500 | Instant |
| 8 | directed_tv | 0.075900 | TV/Time |
| 9 | linear | 0.078400 | Instant |
| 10 | nearest | 0.085900 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.01019   | fail_to_reject_H0 |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.4025    | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.2102    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   8.186e-05 | reject_H0         |

## Iteration Note

Comparison of KNN k=5 vs k=3 (it22b). Denser connectivity. TV shows 18-22% RMSE gain.