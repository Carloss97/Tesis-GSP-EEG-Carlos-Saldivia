# Stats QA Report — it53_all_datasets_nnk

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
| 1 | mean | instant | 0.159522 |
| 2 | heat_diffusion_temporal | tv_time | 0.162435 |
| 3 | gsmooth | instant | 0.162702 |
| 4 | tv | tv_time | 0.163996 |
| 5 | idw | instant | 0.164522 |
| 6 | trss | tv_time | 0.168169 |
| 7 | wavelet_temporal | tv_time | 0.170747 |
| 8 | directed_tv | tv_time | 0.175865 |
| 9 | gsp | instant | 0.179537 |
| 10 | linear | instant | 0.186874 |
