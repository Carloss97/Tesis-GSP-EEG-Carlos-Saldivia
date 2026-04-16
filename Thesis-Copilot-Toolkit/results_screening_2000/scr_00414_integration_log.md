# Integration Log: scr_00414
Started: 2026-04-16T13:22:58.749853+00:00
Description: Screening scr_00414 ds=iv100hz_mat graph=vknng miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=8.5494e+01 | t=0.0061s
    tv | MR=0.1 | seed=0 | MAE=1.4026e+01 | t=0.1493s
    trss | MR=0.1 | seed=0 | MAE=1.4107e+01 | t=0.0176s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.6418e+02 | t=0.0080s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.0089e+02 | t=2.7976s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0114s
    tikhonov | MR=0.1 | seed=1 | MAE=8.6007e+01 | t=0.0085s
    tv | MR=0.1 | seed=1 | MAE=1.5710e+01 | t=0.3283s
    trss | MR=0.1 | seed=1 | MAE=1.4780e+01 | t=0.6741s

Completed: 2026-04-16T13:22:58.750728+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.