# Stats QA Report — it17_synthetic_broad_all_graphs

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
| 1 | directed_tv | 0.077200 | TV/Time |
| 2 | heat_diffusion_temporal | 0.080400 | TV/Time |
| 3 | idw | 0.083100 | Instant |
| 4 | trss | 0.083300 | TV/Time |
| 5 | tv | 0.084200 | TV/Time |
| 6 | gsmooth | 0.084200 | Instant |
| 7 | gsp | 0.085300 | Instant |
| 8 | mean | 0.085300 | Instant |
| 9 | spherical_spline | 0.085300 | Instant |
| 10 | linear | 0.094300 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   8.585e-05 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.02285   | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.3181    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   4.387e-06 | reject_H0         |

## Iteration Note

Compares aew, gaussian, kalofolias, knn_k3, knn_k5, knng, nnk, vknng on broadband EEG.