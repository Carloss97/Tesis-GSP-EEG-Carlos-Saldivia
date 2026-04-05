# Stats QA Report — it20_synthetic_alpha_high_missing

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
| 1 | directed_tv | 0.201900 | TV/Time |
| 2 | heat_diffusion_temporal | 0.207400 | TV/Time |
| 3 | wavelet_temporal | 0.208200 | TV/Time |
| 4 | mean | 0.212500 | Instant |
| 5 | tv | 0.214600 | TV/Time |
| 6 | gsmooth | 0.216900 | Instant |
| 7 | idw | 0.219300 | Instant |
| 8 | trss | 0.224900 | TV/Time |
| 9 | gsp | 0.230500 | Instant |
| 10 | linear | 0.257200 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.0003686 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.05226   | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   9.988e-06 | reject_H0         |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   8.147e-17 | reject_H0         |

## Iteration Note

Alpha band TV family achieves 22-25% RMSE gain at high missing rates. directed_tv is best at mr=0.3.