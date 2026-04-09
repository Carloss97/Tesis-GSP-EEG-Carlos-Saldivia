# Stats QA Report — it41_physionet_multisubject_run4

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
| 1 | tv | tv_time | 0.000007 |
| 2 | idw | instant | 0.000007 |
| 3 | linear | instant | 0.000007 |
| 4 | mean | instant | 0.000008 |
| 5 | gsmooth | instant | 0.000008 |
| 6 | heat_diffusion_temporal | tv_time | 0.000008 |
| 7 | nearest | instant | 0.000008 |
| 8 | trss | tv_time | 0.000008 |
| 9 | directed_tv | tv_time | 0.000008 |
| 10 | gsp | instant | 0.000009 |
