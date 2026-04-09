# Stats QA Report — it25_alpha_beta_two_bands

**Overall: PASS**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths non-negative | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 5 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < instant in ≥1 scenario | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | mean | 0.062400 | Instant |
| 2 | idw | 0.064300 | Instant |
| 3 | gsmooth | 0.065500 | Instant |
| 4 | tv | 0.065700 | TV/Time |
| 5 | heat_diffusion_temporal | 0.067200 | TV/Time |
| 6 | trss | 0.070400 | TV/Time |
| 7 | gsp | 0.070700 | Instant |
| 8 | linear | 0.070900 | Instant |
| 9 | directed_tv | 0.074100 | TV/Time |
| 10 | nearest | 0.075100 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   1.399e-06 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.02924   | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.01027   | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   4.502e-20 | reject_H0         |

## Iteration Note

Tests TV family on narrow frequency bands only. Gains 14-21% family RMSE.