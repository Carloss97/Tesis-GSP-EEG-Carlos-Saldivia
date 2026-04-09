# Stats QA Report — it03_synthetic_beta

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
| 1 | gsmooth | 0.0657 | Instant |
| 2 | heat_diffusion_temporal | 0.0657 | TV/Time |
| 3 | tv | 0.0658 | TV/Time |
| 4 | mean | 0.0659 | Instant |
| 5 | idw | 0.0661 | Instant |
| 6 | trss | 0.0676 | TV/Time |
| 7 | directed_tv | 0.0685 | TV/Time |
| 8 | gsp | 0.0695 | Instant |
| 9 | rbfi_tps | 0.0766 | Instant |
| 10 | rbfi_mq | 0.0781 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.0008898 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.07522   | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.1158    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   9.43e-10  | reject_H0         |

## Iteration Note

Beta band EEG synthetic dataset. TV family expected to win at high missing rates.