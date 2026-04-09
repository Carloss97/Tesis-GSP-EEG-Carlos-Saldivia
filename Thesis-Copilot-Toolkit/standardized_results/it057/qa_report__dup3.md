# Stats QA Report — it57_3syn_mr40_only

**Overall: PASS**

## QA Gates

| Gate | Description | Status |
|------|-------------|--------|
| QA-01 | No missing values in stats | PASS |
| QA-02 | CI widths ≥ 0 | PASS |
| QA-03 | ≥5 unique methods | PASS |
| QA-04 | n ≥ 3 per scenario | PASS |
| QA-05 | ≥1 significant contrast | PASS |
| QA-06 | TV family MAE < instant | PASS |
| QA-07 | No duplicate rows | PASS |

## Top-10 Methods by MAE (median)

| Rank | Method | Family | Median MAE |
|------|--------|--------|------------|
| 1 | mean | instant | 0.261051 |
| 2 | tv | tv_time | 0.261373 |
| 3 | directed_tv | tv_time | 0.270135 |
| 4 | gsmooth | instant | 0.270702 |
| 5 | heat_diffusion_temporal | tv_time | 0.272857 |
| 6 | idw | instant | 0.275267 |
| 7 | wavelet_temporal | tv_time | 0.276645 |
| 8 | trss | tv_time | 0.281334 |
| 9 | gsp | instant | 0.286079 |
| 10 | linear | instant | 0.307510 |
