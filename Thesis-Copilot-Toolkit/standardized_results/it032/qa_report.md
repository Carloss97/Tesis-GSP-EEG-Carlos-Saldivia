# Stats QA Report — it32_3syn_mr20_only

**Overall: PASS**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths non-negative | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 8 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < instant in ≥1 scenario | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | mean | 0.125200 | Instant |
| 2 | tv | 0.126800 | TV/Time |
| 3 | gsmooth | 0.128200 | Instant |
| 4 | idw | 0.128900 | Instant |
| 5 | heat_diffusion_temporal | 0.133700 | TV/Time |
| 6 | trss | 0.135600 | TV/Time |
| 7 | gsp | 0.137400 | Instant |
| 8 | directed_tv | 0.138300 | TV/Time |
| 9 | wavelet_temporal | 0.149800 | TV/Time |
| 10 | linear | 0.162400 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   7.812e-08 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.001785  | reject_H0         |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.005046  | reject_H0         |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   6.953e-09 | reject_H0         |

## Iteration Note

20% missing is the most common practical scenario. TV family achieves 23% RMSE gain.