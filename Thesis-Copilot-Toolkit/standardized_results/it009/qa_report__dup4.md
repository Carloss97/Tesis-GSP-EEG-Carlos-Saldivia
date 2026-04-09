# Stats QA Report — it09_tikhonov_rbfi_focus

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
| 1 | gsmooth | 0.0658 | Instant |
| 2 | mean | 0.0659 | Instant |
| 3 | tv | 0.0659 | TV/Time |
| 4 | idw | 0.0661 | Instant |
| 5 | heat_diffusion_temporal | 0.0728 | TV/Time |
| 6 | directed_tv | 0.0760 | TV/Time |
| 7 | linear | 0.0784 | Instant |
| 8 | trss | 0.0793 | TV/Time |
| 9 | gsp | 0.0808 | Instant |
| 10 | nearest | 0.0859 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   7.05e-10  | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.004257  | reject_H0         |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.01414   | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   2.099e-23 | reject_H0         |

## Iteration Note

Classic spatial interpolation methods (Tikhonov, RBF, spherical spline) are strong baselines. This iteration quantifies their gap with temporal-graph methods.