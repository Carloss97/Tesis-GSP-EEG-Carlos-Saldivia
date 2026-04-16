# Integration Log: scr_00618
Started: 2026-04-16T14:45:20.054568+00:00
Description: Screening scr_00618 ds=iv100hz_mat graph=knng miss=[0.3] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knng built OK
    mean | MR=0.3 | seed=0 | MAE=7.3919e+01 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=1.1253e+02 | t=0.0101s
    tikhonov | MR=0.3 | seed=0 | MAE=1.2585e+02 | t=0.1636s
    tv | MR=0.3 | seed=0 | MAE=6.0806e+01 | t=0.5130s
    trss | MR=0.3 | seed=0 | MAE=6.1727e+01 | t=0.3764s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.8178e+02 | t=0.0513s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.1674e+02 | t=25.0334s
    mean | MR=0.3 | seed=1 | MAE=7.2756e+01 | t=0.0036s
    nearest | MR=0.3 | seed=1 | MAE=1.1224e+02 | t=0.0101s
    tikhonov | MR=0.3 | seed=1 | MAE=1.2595e+02 | t=0.0170s
    tv | MR=0.3 | seed=1 | MAE=6.6474e+01 | t=0.4969s
    trss | MR=0.3 | seed=1 | MAE=6.0712e+01 | t=0.3236s

Completed: 2026-04-16T14:45:20.055843+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.