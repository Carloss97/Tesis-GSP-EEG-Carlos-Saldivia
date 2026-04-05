# Stats QA Report — it59_broad_high_missing

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
| 1 | heat_diffusion_temporal | tv_time | 0.217511 |
| 2 | directed_tv | tv_time | 0.219687 |
| 3 | spherical_spline | instant | 0.220209 |
| 4 | mean | instant | 0.220209 |
| 5 | tv | tv_time | 0.220532 |
| 6 | gsmooth | instant | 0.220546 |
| 7 | idw | instant | 0.226420 |
| 8 | trss | tv_time | 0.227483 |
| 9 | gsp | instant | 0.231558 |
| 10 | wavelet_temporal | tv_time | 0.237858 |
