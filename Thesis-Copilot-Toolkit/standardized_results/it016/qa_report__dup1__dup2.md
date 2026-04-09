# Stats QA Report — it16_synthetic_broad_vknng

**Overall: FAIL**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths non-negative | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 5 per (method, scenario) | FAIL |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | FAIL |
| QA-06 | TV/Time MAE < best instant in ≥1 scenario | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | directed_tv | 0.076000 | TV/Time |
| 2 | heat_diffusion_temporal | 0.080200 | TV/Time |
| 3 | idw | 0.083100 | Instant |
| 4 | tv | 0.084000 | TV/Time |
| 5 | gsmooth | 0.084200 | Instant |
| 6 | trss | 0.084400 | TV/Time |
| 7 | gsp | 0.085300 | Instant |
| 8 | mean | 0.085300 | Instant |
| 9 | spherical_spline | 0.085300 | Instant |
| 10 | linear | 0.094300 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |   p_value | decision          |
|:--------------------------|:---------|:----------|:----------|----------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.3429  | fail_to_reject_H0 |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.6857  | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.5096  | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan       | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.04895 | fail_to_reject_H0 |

## Iteration Note

VKNNG adapts k per node (kmin=2, kmax=8). TV family shows 15-21% gain. Best for non-uniform EEG sensor layouts.