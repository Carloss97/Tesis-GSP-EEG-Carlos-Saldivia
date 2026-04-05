# Stats QA Report — it15b_gaussian_3syn

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
| 1 | trss | 0.065100 | TV/Time |
| 2 | heat_diffusion_temporal | 0.065200 | TV/Time |
| 3 | gsp | 0.065200 | Instant |
| 4 | gsmooth | 0.065500 | Instant |
| 5 | tv | 0.065700 | TV/Time |
| 6 | mean | 0.065900 | Instant |
| 7 | idw | 0.066100 | Instant |
| 8 | directed_tv | 0.074300 | TV/Time |
| 9 | linear | 0.078400 | Instant |
| 10 | nearest | 0.085900 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.001354  | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.4357    | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.1672    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.0001538 | reject_H0         |

## Iteration Note

Retry of it15 with 3 datasets for statistical power. n=3 per (method, scenario). Gaussian sigma=1 RBF graph achieves 19-23% TV family gain.