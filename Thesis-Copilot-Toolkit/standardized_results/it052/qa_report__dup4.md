# Stats QA Report — it52_all_datasets_gaussian_graph

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
| 2 | tv | tv_time | 0.159735 |
| 3 | gsmooth | instant | 0.160077 |
| 4 | heat_diffusion_temporal | tv_time | 0.160373 |
| 5 | trss | tv_time | 0.161320 |
| 6 | gsp | instant | 0.161346 |
| 7 | directed_tv | tv_time | 0.162407 |
| 8 | idw | instant | 0.164522 |
| 9 | wavelet_temporal | tv_time | 0.183763 |
| 10 | linear | instant | 0.186874 |
