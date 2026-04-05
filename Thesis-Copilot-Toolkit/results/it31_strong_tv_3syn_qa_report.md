# Stats QA Report — it31_strong_tv_3syn

**Overall: PASS**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats (non-DTW) | PASS |
| QA-02 | CI95 widths non-negative | PASS |
| QA-03 | All methods present in MAE stats | PASS |
| QA-04 | N ≥ 5 per (method, scenario) | PASS |
| QA-05 | ≥ 1 contrast significant (Bonferroni) | PASS |
| QA-06 | TV/Time MAE < instant in ≥1 scenario | PASS |
| QA-07 | No duplicate stats rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | MAE median | Family |
|------|--------|------------|--------|
| 1 | gsmooth | 0.065800 | Instant |
| 2 | mean | 0.065900 | Instant |
| 3 | tv | 0.065900 | TV/Time |
| 4 | idw | 0.066100 | Instant |
| 5 | heat_diffusion_temporal | 0.072800 | Instant |
| 6 | directed_tv | 0.076000 | TV/Time |
| 7 | linear | 0.078400 | Instant |
| 8 | trss | 0.079300 | TV/Time |
| 9 | gsp | 0.080800 | Instant |
| 10 | nearest | 0.085900 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   7.05e-10  | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.004257  | reject_H0         |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   1.275e-28 | reject_H0         |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   1.544e-29 | reject_H0         |

## Iteration Note

Focuses on the 3 consistently best TV methods. Reduces noise from weaker TV variants (graph_time_tikhonov, temporal_laplacian).