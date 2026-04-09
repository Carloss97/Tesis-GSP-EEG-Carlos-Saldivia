# Stats QA Report — it39_physionet_gaussian_nnk_knn

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
| 1 | mean | 0.000013 | Instant |
| 2 | tv | 0.000013 | TV/Time |
| 3 | heat_diffusion_temporal | 0.000014 | TV/Time |
| 4 | idw | 0.000014 | Instant |
| 5 | linear | 0.000015 | Instant |
| 6 | gsmooth | 0.000015 | Instant |
| 7 | nearest | 0.000015 | Instant |
| 8 | directed_tv | 0.000015 | TV/Time |
| 9 | trss | 0.000016 | TV/Time |
| 10 | wavelet_temporal | 0.000016 | TV/Time |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |   p_value | decision          |
|:--------------------------|:---------|:----------|:----------|----------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   0.1     | fail_to_reject_H0 |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.2     | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.1239  | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan       | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.00597 | reject_H0         |

## Iteration Note

Best physionet graphs at mr=40%: gaussian 16.7%, nnk 15.8%, knn_k3 16.0%. All three pooled.