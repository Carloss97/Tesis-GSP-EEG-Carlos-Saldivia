# Stats QA Report — it04_physionet

**Overall: FAIL**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths positive/finite | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 5 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < best instant MAE | FAIL |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | directed_tv | 0.0000 | TV/Time |
| 2 | gsmooth | 0.0000 | Instant |
| 3 | heat_diffusion_temporal | 0.0000 | TV/Time |
| 4 | gsp | 0.0000 | Instant |
| 5 | idw | 0.0000 | Instant |
| 6 | linear | 0.0000 | Instant |
| 7 | rbfi_mq | 0.0000 | Instant |
| 8 | mean | 0.0000 | Instant |
| 9 | rbfi_tps | 0.0000 | Instant |
| 10 | tv | 0.0000 | TV/Time |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.0006022 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.1275    | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.9783    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.4307    | fail_to_reject_H0 |

## Iteration Note

Real EEG dataset. Tiny absolute values (MAE ~1e-5). Performance closely matched.