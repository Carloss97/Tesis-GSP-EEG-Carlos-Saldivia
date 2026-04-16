# Integration Log: scr_00534
Started: 2026-04-16T14:05:15.379824+00:00
Description: Screening scr_00534 ds=iv100hz_mat graph=aew miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=5.2754e+01 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=8.0647e+01 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0028e+02 | t=0.0111s
    tv | MR=0.2 | seed=0 | MAE=4.1205e+01 | t=1.0336s
    trss | MR=0.2 | seed=0 | MAE=3.9148e+01 | t=0.4349s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6397e+02 | t=0.0461s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.9751e+02 | t=18.0843s
    mean | MR=0.2 | seed=1 | MAE=5.2652e+01 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.0770e+01 | t=0.0065s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0120e+02 | t=0.0060s
    tv | MR=0.2 | seed=1 | MAE=4.0377e+01 | t=0.1536s
    trss | MR=0.2 | seed=1 | MAE=4.0426e+01 | t=0.0189s

Completed: 2026-04-16T14:05:15.381490+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.