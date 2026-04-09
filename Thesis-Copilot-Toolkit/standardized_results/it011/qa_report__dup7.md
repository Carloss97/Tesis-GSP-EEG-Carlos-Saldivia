# Stats QA Report — it11_physionet_high_missing

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
| 1 | gsmooth | 0.000013 | Instant |
| 2 | mean | 0.000013 | Instant |
| 3 | tv | 0.000013 | TV/Time |
| 4 | heat_diffusion_temporal | 0.000014 | TV/Time |
| 5 | gsp | 0.000014 | Instant |
| 6 | idw | 0.000014 | Instant |
| 7 | trss | 0.000014 | TV/Time |
| 8 | directed_tv | 0.000015 | TV/Time |
| 9 | nearest | 0.000015 | Instant |
| 10 | linear | 0.000015 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.001088  | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.2345    | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.01587   | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.0004972 | reject_H0         |

## Iteration Note

At 40% missing channels, TV/Time median MAE beats instant median on physionet. Limited to single scenario.