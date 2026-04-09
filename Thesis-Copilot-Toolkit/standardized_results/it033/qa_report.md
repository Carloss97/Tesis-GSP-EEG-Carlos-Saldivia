# Stats QA Report — it33_3syn_mr30_only

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
| 1 | directed_tv | 0.202600 | TV/Time |
| 2 | heat_diffusion_temporal | 0.203000 | TV/Time |
| 3 | mean | 0.203900 | Instant |
| 4 | tv | 0.204400 | TV/Time |
| 5 | gsmooth | 0.204800 | Instant |
| 6 | idw | 0.209000 | Instant |
| 7 | trss | 0.212800 | TV/Time |
| 8 | wavelet_temporal | 0.216000 | TV/Time |
| 9 | gsp | 0.216500 | Instant |
| 10 | linear | 0.236400 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   1.23e-07  | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.00758   | reject_H0         |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   2.068e-07 | reject_H0         |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   3.823e-21 | reject_H0         |

## Iteration Note

30% missing is the boundary between moderate and high degradation. TV family achieves 21% RMSE gain.