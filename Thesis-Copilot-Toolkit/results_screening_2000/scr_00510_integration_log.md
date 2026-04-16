# Integration Log: scr_00510
Started: 2026-04-16T13:56:07.071282+00:00
Description: Screening scr_00510 ds=iv100hz_mat graph=knng miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=5.2754e+01 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=8.0647e+01 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0748e+02 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=4.2149e+01 | t=0.1449s
    trss | MR=0.2 | seed=0 | MAE=3.9561e+01 | t=0.0184s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7331e+02 | t=0.0078s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0883e+02 | t=25.3395s
    mean | MR=0.2 | seed=1 | MAE=5.2652e+01 | t=0.0023s
    nearest | MR=0.2 | seed=1 | MAE=8.0770e+01 | t=0.0056s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0843e+02 | t=0.0056s
    tv | MR=0.2 | seed=1 | MAE=4.6932e+01 | t=0.1487s
    trss | MR=0.2 | seed=1 | MAE=4.1004e+01 | t=0.0182s

Completed: 2026-04-16T13:56:07.072477+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.