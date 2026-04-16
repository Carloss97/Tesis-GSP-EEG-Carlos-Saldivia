# Integration Log: scr_00522
Started: 2026-04-16T14:01:00.401937+00:00
Description: Screening scr_00522 ds=iv100hz_mat graph=vknng miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=5.2754e+01 | t=0.0037s
    nearest | MR=0.2 | seed=0 | MAE=8.0647e+01 | t=0.0092s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0939e+02 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=4.1318e+01 | t=0.3699s
    trss | MR=0.2 | seed=0 | MAE=3.9009e+01 | t=0.0176s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7562e+02 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.1109e+02 | t=22.4727s
    mean | MR=0.2 | seed=1 | MAE=5.2652e+01 | t=0.0095s
    nearest | MR=0.2 | seed=1 | MAE=8.0770e+01 | t=0.0079s
    tikhonov | MR=0.2 | seed=1 | MAE=1.1030e+02 | t=0.0059s
    tv | MR=0.2 | seed=1 | MAE=4.2813e+01 | t=0.1493s
    trss | MR=0.2 | seed=1 | MAE=4.0454e+01 | t=0.0182s

Completed: 2026-04-16T14:01:00.403473+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.