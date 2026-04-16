# Integration Log: scr_01086
Started: 2026-04-16T13:34:10.677009+00:00
Description: Screening scr_01086 ds=iv100hz_mat graph=knn miss=[0.1] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1206e+01 | t=0.1507s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.9974e+01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=1.2847e+01 | t=0.1960s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5872e+02 | t=15.8291s
    tv | MR=0.2 | seed=1 | MAE=5.1152e+01 | t=0.1544s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.1246e+01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.2922e+01 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5936e+02 | t=7.8189s
    tv | MR=0.2 | seed=0 | MAE=4.9607e+01 | t=0.5187s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0930e+02 | t=0.0135s
    trss | MR=0.2 | seed=0 | MAE=1.8138e+01 | t=0.2111s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6636e+02 | t=19.1321s

Completed: 2026-04-16T13:34:10.677889+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.