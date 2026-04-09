# Stats QA Report — it55_all_datasets_low_mr

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
| 1 | mean | instant | 0.092713 |
| 2 | gsmooth | instant | 0.094939 |
| 3 | tv | tv_time | 0.095102 |
| 4 | idw | instant | 0.095729 |
| 5 | trss | tv_time | 0.098272 |
| 6 | heat_diffusion_temporal | tv_time | 0.098508 |
| 7 | gsp | instant | 0.098723 |
| 8 | directed_tv | tv_time | 0.103614 |
| 9 | linear | instant | 0.109536 |
| 10 | wavelet_temporal | tv_time | 0.116364 |
