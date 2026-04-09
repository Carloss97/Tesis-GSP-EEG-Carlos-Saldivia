# Stats QA Report — it08_high_missing_synthetic

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
| 1 | directed_tv | 0.2026 | TV/Time |
| 2 | heat_diffusion_temporal | 0.2030 | TV/Time |
| 3 | mean | 0.2039 | Instant |
| 4 | tv | 0.2044 | TV/Time |
| 5 | gsmooth | 0.2048 | Instant |
| 6 | idw | 0.2090 | Instant |
| 7 | trss | 0.2128 | TV/Time |
| 8 | wavelet_temporal | 0.2160 | TV/Time |
| 9 | gsp | 0.2165 | Instant |
| 10 | linear | 0.2364 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   9.227e-10 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.00233   | reject_H0         |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   1.433e-07 | reject_H0         |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   5.264e-35 | reject_H0         |

## Iteration Note

TV methods show greatest advantage under high missing-channel rates. Family RMSE gain exceeds 20% at these scenarios.