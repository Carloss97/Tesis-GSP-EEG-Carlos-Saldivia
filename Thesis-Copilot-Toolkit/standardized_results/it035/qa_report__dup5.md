# Stats QA Report — it35_all4_kalofolias

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
| 1 | mean | 0.062400 | Instant |
| 2 | tv | 0.062400 | TV/Time |
| 3 | idw | 0.064300 | Instant |
| 4 | directed_tv | 0.066000 | TV/Time |
| 5 | gsmooth | 0.068700 | Instant |
| 6 | linear | 0.070900 | Instant |
| 7 | nearest | 0.075100 | Instant |
| 8 | rbfi_tps | 0.082500 | Instant |
| 9 | trss | 0.082800 | TV/Time |
| 10 | rbfi_mq | 0.083800 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |    p_value | decision          |
|:--------------------------|:---------|:----------|:----------|-----------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.003937 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.006287 | reject_H0         |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.2471   | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan        | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.8774   | fail_to_reject_H0 |

## Iteration Note

Kalofolias on all datasets: synthetic 8-25% gain, physionet ~5% (marginal). Family-level pooling stabilizes.