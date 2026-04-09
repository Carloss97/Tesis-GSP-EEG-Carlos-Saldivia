# Stats QA Report — it51_all_datasets_strong_tv

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
| 2 | gsmooth | instant | 0.161092 |
| 3 | tv | tv_time | 0.161320 |
| 4 | idw | instant | 0.164522 |
| 5 | trss | tv_time | 0.165710 |
| 6 | heat_diffusion_temporal | tv_time | 0.166028 |
| 7 | directed_tv | tv_time | 0.167123 |
| 8 | wavelet_temporal | tv_time | 0.177728 |
| 9 | linear | instant | 0.186874 |
| 10 | nearest | instant | 0.203631 |
