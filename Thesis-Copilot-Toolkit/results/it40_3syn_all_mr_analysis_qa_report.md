# Stats QA Report — it40_3syn_all_mr_analysis

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
| 1 | mean | 0.065900 | Instant |
| 2 | idw | 0.066100 | Instant |
| 3 | tv | 0.066100 | TV/Time |
| 4 | gsmooth | 0.066700 | Instant |
| 5 | heat_diffusion_temporal | 0.071600 | TV/Time |
| 6 | directed_tv | 0.075800 | TV/Time |
| 7 | trss | 0.076400 | TV/Time |
| 8 | gsp | 0.076900 | Instant |
| 9 | linear | 0.078400 | Instant |
| 10 | nearest | 0.085900 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.001785  | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.4273    | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.0937    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   1.229e-08 | reject_H0         |

## Iteration Note

Comprehensive analysis of symmetric KNN topologies across all missing rates and bands.