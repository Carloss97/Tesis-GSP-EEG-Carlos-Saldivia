# Stats QA Report — it58_broad_low_missing

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
| 1 | directed_tv | tv_time | 0.099140 |
| 2 | heat_diffusion_temporal | tv_time | 0.100185 |
| 3 | gsmooth | instant | 0.104108 |
| 4 | trss | tv_time | 0.104207 |
| 5 | idw | instant | 0.104209 |
| 6 | tv | tv_time | 0.104393 |
| 7 | spherical_spline | instant | 0.105267 |
| 8 | mean | instant | 0.105267 |
| 9 | gsp | instant | 0.105804 |
| 10 | linear | instant | 0.114079 |
