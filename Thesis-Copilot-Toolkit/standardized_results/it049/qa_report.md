# Stats QA Report — it49_physionet_multisubj_low_mr

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
| 1 | linear | instant | 0.000003 |
| 2 | mean | instant | 0.000003 |
| 3 | tv | tv_time | 0.000003 |
| 4 | trss | tv_time | 0.000003 |
| 5 | idw | instant | 0.000003 |
| 6 | gsmooth | instant | 0.000004 |
| 7 | gsp | instant | 0.000004 |
| 8 | heat_diffusion_temporal | tv_time | 0.000004 |
| 9 | rbfi_tps | instant | 0.000004 |
| 10 | directed_tv | tv_time | 0.000004 |
