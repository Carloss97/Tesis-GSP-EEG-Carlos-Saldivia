# Stats QA Report — it05_all_datasets

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
| 1 | mean | 0.0624 | Instant |
| 2 | idw | 0.0643 | Instant |
| 3 | gsmooth | 0.0655 | Instant |
| 4 | tv | 0.0657 | TV/Time |
| 5 | heat_diffusion_temporal | 0.0672 | TV/Time |
| 6 | trss | 0.0704 | TV/Time |
| 7 | gsp | 0.0707 | Instant |
| 8 | linear | 0.0709 | Instant |
| 9 | directed_tv | 0.0741 | TV/Time |
| 10 | nearest | 0.0751 | Instant |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   9.037e-06 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.04034   | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.1102    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   4.913e-11 | reject_H0         |

## Iteration Note

Combined benchmark. TV family shows 8-13% MAE gain in pooled analysis.