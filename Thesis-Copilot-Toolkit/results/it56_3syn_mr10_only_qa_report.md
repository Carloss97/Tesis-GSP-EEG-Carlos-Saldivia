# Stats QA Report — it56_3syn_mr10_only

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
| 1 | gsmooth | instant | 0.065842 |
| 2 | mean | instant | 0.065862 |
| 3 | tv | tv_time | 0.065912 |
| 4 | idw | instant | 0.066099 |
| 5 | heat_diffusion_temporal | tv_time | 0.072771 |
| 6 | directed_tv | tv_time | 0.076043 |
| 7 | linear | instant | 0.078442 |
| 8 | trss | tv_time | 0.079331 |
| 9 | gsp | instant | 0.080761 |
| 10 | nearest | instant | 0.085912 |
