# Batch Analysis Summary

- Files processed (approx): 141
- Rows consolidated: 93277

## Global method MAE (lower better)
method | count | mean | std
---|---|---|---
spline_temporal | 32 | 1.16548e-05 | 2.72095e-06
gsmooth | 5274 | 0.0925906 | 0.0964884
idw | 5406 | 0.095452 | 0.0991223
gsp | 3173 | 0.115833 | 0.108173
directed_tv | 2560 | 0.12061 | 0.170436
linear | 3512 | 0.120846 | 0.118006
wavelet_temporal | 2550 | 0.122317 | 0.103314
spherical_spline | 3306 | 0.134658 | 0.142029
rbfi_tps | 3306 | 0.144015 | 0.149192
rbfi_mq | 3306 | 0.160766 | 0.170595

## Scenarios with significant Friedman test (p<0.05)
- Scenario: **frontal_band** — p=3.319e-10, blocks=8. Top methods: spherical_spline, tv, gsmooth, idw, trss
- Scenario: **left_lateral_temporal** — p=2.199e-11, blocks=8. Top methods: spherical_spline, tv, gsmooth, idw, trss
- Scenario: **midline_central** — p=2.225e-12, blocks=8. Top methods: spherical_spline, tv, gsmooth, trss, gsp
- Scenario: **occipital_band** — p=8.649e-11, blocks=8. Top methods: spherical_spline, tv, gsmooth, trss, idw
- Scenario: **right_lateral_temporal** — p=2.787e-11, blocks=8. Top methods: spherical_spline, tv, gsmooth, idw, trss
