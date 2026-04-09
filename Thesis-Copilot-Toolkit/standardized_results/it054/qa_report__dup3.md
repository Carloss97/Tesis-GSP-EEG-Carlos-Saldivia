# Stats QA Report — it54_all_datasets_high_mr

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
| 1 | mean | instant | 0.226332 |
| 2 | gsmooth | instant | 0.227245 |
| 3 | tv | tv_time | 0.227538 |
| 4 | directed_tv | tv_time | 0.230631 |
| 5 | trss | tv_time | 0.233149 |
| 6 | idw | instant | 0.233315 |
| 7 | heat_diffusion_temporal | tv_time | 0.233548 |
| 8 | wavelet_temporal | tv_time | 0.239092 |
| 9 | gsp | instant | 0.241150 |
| 10 | linear | instant | 0.264213 |
