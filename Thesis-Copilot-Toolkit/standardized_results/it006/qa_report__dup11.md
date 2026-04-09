# Stats QA Report — it06_tv_focus_kalofolias_nnk

**Overall: FAIL**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths positive/finite | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 5 per (method, scenario) | FAIL |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < best instant MAE | FAIL |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | idw | 0.0746 | Instant |
| 2 | gsmooth | 0.0753 | Instant |
| 3 | tv | 0.0754 | TV/Time |
| 4 | mean | 0.0756 | Instant |
| 5 | trss | 0.0768 | TV/Time |
| 6 | directed_tv | 0.0777 | TV/Time |
| 7 | gsp | 0.0805 | Instant |
| 8 | rbfi_tps | 0.0858 | Instant |
| 9 | linear | 0.0863 | Instant |
| 10 | spherical_spline | 0.0877 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |    p_value | decision          |
|:--------------------------|:---------|:----------|:----------|-----------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.002414 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.005603 | reject_H0         |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.6641   | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan        | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.03331  | fail_to_reject_H0 |

## Iteration Note

Graph focus: kalofolias (learnable graph) and NNK (non-negative kernel). Highlights graph construction effect.