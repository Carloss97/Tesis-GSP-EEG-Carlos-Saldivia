# Stats QA Report — it38_broad_gaussian_kalofolias_nnk

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
| 1 | heat_diffusion_temporal | 0.081300 | TV/Time |
| 2 | directed_tv | 0.081500 | TV/Time |
| 3 | idw | 0.083100 | Instant |
| 4 | trss | 0.083200 | TV/Time |
| 5 | gsmooth | 0.084700 | Instant |
| 6 | tv | 0.085100 | TV/Time |
| 7 | spherical_spline | 0.085300 | Instant |
| 8 | mean | 0.085300 | Instant |
| 9 | gsp | 0.088300 | Instant |
| 10 | linear | 0.094300 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |   p_value | decision          |
|:--------------------------|:---------|:----------|:----------|----------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.00355 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.0404  | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.9656  | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan       | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.05643 | fail_to_reject_H0 |

## Iteration Note

Compares RBF-kernel (Gaussian), learned-smooth (Kalofolias), and non-negative-kernel (NNK) graph constructions.