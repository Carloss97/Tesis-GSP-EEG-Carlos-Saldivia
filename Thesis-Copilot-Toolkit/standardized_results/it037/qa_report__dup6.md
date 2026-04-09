# Stats QA Report — it37_3syn_alpha_low_missing

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
| 1 | mean | 0.058900 | Instant |
| 2 | idw | 0.062600 | Instant |
| 3 | tv | 0.063300 | TV/Time |
| 4 | linear | 0.063400 | Instant |
| 5 | nearest | 0.064300 | Instant |
| 6 | gsmooth | 0.065200 | Instant |
| 7 | heat_diffusion_temporal | 0.070800 | TV/Time |
| 8 | trss | 0.079500 | TV/Time |
| 9 | gsp | 0.080800 | Instant |
| 10 | wavelet_temporal | 0.082700 | TV/Time |

## Significance Summary

| test_id                   | metric   | group_a   | group_b   |     p_value | decision          |
|:--------------------------|:---------|:----------|:----------|------------:|:------------------|
| mae_trss_vs_tikhonov      | mae      | trss      | tikhonov  |   5.088e-05 | reject_H0         |
| rmse_trss_vs_tikhonov     | rmse     | trss      | tikhonov  |   0.06756   | fail_to_reject_H0 |
| mae_tv_family_vs_instant  | mae      | tv_time   | instant   |   0.4728    | fail_to_reject_H0 |
| dtw_tv_family_vs_instant  | dtw      | tv_time   | instant   | nan         | insufficient_data |
| rmse_tv_family_vs_instant | rmse     | tv_time   | instant   |   0.003015  | reject_H0         |

## Iteration Note

Alpha band TV family advantage at mild degradation. Complements it20 (high missing on alpha).