# Integration Log: scr_00714
Started: 2026-04-16T15:37:28.434473+00:00
Description: Screening scr_00714 ds=iv100hz_mat graph=kalofolias miss=[0.4] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: kalofolias built OK
    mean | MR=0.4 | seed=0 | MAE=1.0557e+02 | t=0.0034s
    nearest | MR=0.4 | seed=0 | MAE=1.5725e+02 | t=0.0193s
    tikhonov | MR=0.4 | seed=0 | MAE=1.3254e+02 | t=0.0188s
    tv | MR=0.4 | seed=0 | MAE=1.0405e+02 | t=0.8967s
    trss | MR=0.4 | seed=0 | MAE=4.6062e+01 | t=0.0302s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.3464e+02 | t=0.0172s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=2.9562e+02 | t=34.8181s
    mean | MR=0.4 | seed=1 | MAE=1.0515e+02 | t=0.0054s
    nearest | MR=0.4 | seed=1 | MAE=1.5788e+02 | t=0.0506s
    tikhonov | MR=0.4 | seed=1 | MAE=1.3458e+02 | t=0.0304s
    tv | MR=0.4 | seed=1 | MAE=1.0478e+02 | t=1.4581s
    trss | MR=0.4 | seed=1 | MAE=4.5795e+01 | t=0.0310s

Completed: 2026-04-16T15:37:28.475911+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.