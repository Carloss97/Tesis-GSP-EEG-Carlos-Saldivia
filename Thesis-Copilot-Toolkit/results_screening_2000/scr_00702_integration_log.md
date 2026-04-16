# Integration Log: scr_00702
Started: 2026-04-16T15:31:04.323442+00:00
Description: Screening scr_00702 ds=iv100hz_mat graph=gaussian miss=[0.4] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0557e+02 | t=0.0227s
    nearest | MR=0.4 | seed=0 | MAE=1.5725e+02 | t=0.0692s
    tikhonov | MR=0.4 | seed=0 | MAE=1.5975e+02 | t=0.0264s
    tv | MR=0.4 | seed=0 | MAE=8.8432e+01 | t=0.9075s
    trss | MR=0.4 | seed=0 | MAE=9.0889e+01 | t=0.3899s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.0575e+02 | t=0.0697s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=2.5451e+02 | t=11.9980s
    mean | MR=0.4 | seed=1 | MAE=1.0515e+02 | t=0.0039s
    nearest | MR=0.4 | seed=1 | MAE=1.5788e+02 | t=0.0538s
    tikhonov | MR=0.4 | seed=1 | MAE=1.6007e+02 | t=0.0164s
    tv | MR=0.4 | seed=1 | MAE=9.9293e+01 | t=0.8590s
    trss | MR=0.4 | seed=1 | MAE=9.1275e+01 | t=0.2721s

Completed: 2026-04-16T15:31:04.324436+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.