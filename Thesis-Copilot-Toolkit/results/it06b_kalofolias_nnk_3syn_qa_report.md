# Stats QA Report — it06b_kalofolias_nnk_3syn

**Overall: PASS**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths positive/finite | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 5 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < best instant MAE | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | mean | 0.0659 | Instant |
| 2 | idw | 0.0661 | Instant |
| 3 | tv | 0.0662 | TV/Time |
| 4 | gsmooth | 0.0687 | Instant |
| 5 | directed_tv | 0.0777 | TV/Time |
| 6 | linear | 0.0784 | Instant |
| 7 | trss | 0.0785 | TV/Time |
| 8 | gsp | 0.0845 | Instant |
| 9 | nearest | 0.0859 | Instant |
| 10 | rbfi_tps | 0.0884 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.0003205 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.001251  | reject_H0         |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.7701    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.002454  | reject_H0         |

## Iteration Note

Kalofolias (learnable graph by Kalofolias et al.) and NNK (non-negative kernel) graph construction methods. n=2 graphs × 3 datasets = 6 per group.