# Stats QA Report — it34_physionet_kalofolias_gaussian

**Overall: FAIL**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths non-negative | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 3 per (method, scenario) | FAIL |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | FAIL |
| QA-06 | TV/Time MAE < instant in ≥1 scenario | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | gsmooth | 0.000009 | Instant |
| 2 | linear | 0.000009 | Instant |
| 3 | idw | 0.000009 | Instant |
| 4 | gsp | 0.000009 | Instant |
| 5 | nearest | 0.000009 | Instant |
| 6 | rbfi_tps | 0.000009 | Instant |
| 7 | mean | 0.000009 | Instant |
| 8 | tv | 0.000009 | TV/Time |
| 9 | trss | 0.000009 | TV/Time |
| 10 | heat_diffusion_temporal | 0.000010 | TV/Time |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |   p_value | decision          |
|:--------------------------|:---------|:----------|:----------|----------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.02857 | fail_to_reject_H0 |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.1143  | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   1       | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan       | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.9433  | fail_to_reject_H0 |

## Iteration Note

Best graphs for physionet at 40% missing: gaussian shows 16.7% RMSE gain. kalofolias: 5.2%.