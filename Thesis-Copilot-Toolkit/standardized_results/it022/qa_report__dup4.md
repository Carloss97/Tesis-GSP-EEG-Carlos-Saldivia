# Stats QA Report — it22b_knn_k3_3syn

**Overall: PASS**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths non-negative | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 3 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < best instant in ≥1 scenario | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | gsmooth | 0.065300 | Instant |
| 2 | mean | 0.065900 | Instant |
| 3 | idw | 0.066100 | Instant |
| 4 | tv | 0.066300 | TV/Time |
| 5 | heat_diffusion_temporal | 0.073800 | TV/Time |
| 6 | directed_tv | 0.075700 | TV/Time |
| 7 | linear | 0.078400 | Instant |
| 8 | trss | 0.081400 | TV/Time |
| 9 | gsp | 0.082200 | Instant |
| 10 | nearest | 0.085900 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.06896   | fail_to_reject_H0 |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.6236    | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.2545    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   3.783e-05 | reject_H0         |

## Iteration Note

KNN k=3 is the most conservative nearest-neighbor graph. Retry of it22 with 3 datasets for statistical power.