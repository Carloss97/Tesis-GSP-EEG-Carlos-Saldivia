# Stats QA Report — it19_synthetic_beta_high_missing

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
| 1 | heat_diffusion_temporal | 0.203000 | TV/Time |
| 2 | tv | 0.203800 | TV/Time |
| 3 | mean | 0.203900 | Instant |
| 4 | gsmooth | 0.204100 | Instant |
| 5 | directed_tv | 0.204900 | TV/Time |
| 6 | idw | 0.205200 | Instant |
| 7 | trss | 0.207400 | TV/Time |
| 8 | gsp | 0.210400 | Instant |
| 9 | wavelet_temporal | 0.224800 | TV/Time |
| 10 | linear | 0.236400 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.002733  | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.07342   | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.01731   | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   7.068e-13 | reject_H0         |

## Iteration Note

Beta band shows directed_tv best at 40% missing (MAE=0.2555). High missing is most impactful regime.