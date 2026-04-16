# Integration Log: scr_00474
Started: 2026-04-16T13:43:30.852015+00:00
Description: Screening scr_00474 ds=iv100hz_mat graph=gaussian miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2754e+01 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=8.0647e+01 | t=0.0081s
    tikhonov | MR=0.2 | seed=0 | MAE=1.5029e+02 | t=0.0093s
    tv | MR=0.2 | seed=0 | MAE=3.5430e+01 | t=0.7712s
    trss | MR=0.2 | seed=0 | MAE=3.8317e+01 | t=0.5629s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.1000e+02 | t=0.0124s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7337e+02 | t=11.8272s
    mean | MR=0.2 | seed=1 | MAE=5.2652e+01 | t=0.0032s
    nearest | MR=0.2 | seed=1 | MAE=8.0770e+01 | t=0.0077s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5028e+02 | t=0.0087s
    tv | MR=0.2 | seed=1 | MAE=3.4019e+01 | t=0.6642s
    trss | MR=0.2 | seed=1 | MAE=3.8471e+01 | t=0.1733s

Completed: 2026-04-16T13:43:30.852962+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.