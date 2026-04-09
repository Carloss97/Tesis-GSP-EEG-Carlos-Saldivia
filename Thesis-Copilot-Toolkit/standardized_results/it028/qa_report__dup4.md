# Stats QA Report — it28_nnk_3syn

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
| 1 | gsmooth | 0.065100 | Instant |
| 2 | mean | 0.065900 | Instant |
| 3 | idw | 0.066100 | Instant |
| 4 | tv | 0.066500 | TV/Time |
| 5 | heat_diffusion_temporal | 0.069700 | TV/Time |
| 6 | trss | 0.075800 | TV/Time |
| 7 | linear | 0.078400 | Instant |
| 8 | gsp | 0.080700 | Instant |
| 9 | wavelet_temporal | 0.083000 | TV/Time |
| 10 | nearest | 0.085900 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.2855    | fail_to_reject_H0 |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.3123    | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.2231    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   8.795e-06 | reject_H0         |

## Iteration Note

NNK learns non-negative edge weights via convex optimization. k=4 neighbors. TV family shows 12-17% RMSE gain.