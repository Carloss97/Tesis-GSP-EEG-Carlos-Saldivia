# Stats QA Report — it13_gaussian_aew_3syn

**Overall: PASS**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths non-negative | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 5 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < best instant in ≥1 scenario | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | gsmooth | 0.065600 | Instant |
| 2 | mean | 0.065900 | Instant |
| 3 | idw | 0.066100 | Instant |
| 4 | heat_diffusion_temporal | 0.067200 | TV/Time |
| 5 | tv | 0.069900 | TV/Time |
| 6 | trss | 0.072900 | TV/Time |
| 7 | gsp | 0.076100 | Instant |
| 8 | linear | 0.078400 | Instant |
| 9 | nearest | 0.085900 | Instant |
| 10 | directed_tv | 0.086300 | TV/Time |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.004022  | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.1768    | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.06706   | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   4.971e-08 | reject_H0         |

## Iteration Note

Gaussian graph: sigma=1 RBF kernel. AEW: adaptive edge weights combining correlation and distance. 13-22% TV family gain.