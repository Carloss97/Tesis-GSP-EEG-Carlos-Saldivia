# Integration Log: scr_00331
Started: 2026-04-16T15:38:20.555109+00:00
Description: Screening scr_00331 ds=iris_graph_signal graph=knn miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0014s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0015s
    tikhonov | MR=0.1 | seed=0 | MAE=2.6763e-01 | t=0.0035s
    tv | MR=0.1 | seed=0 | MAE=1.2623e-01 | t=0.3310s
    trss | MR=0.1 | seed=0 | MAE=1.1223e-01 | t=0.0054s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1809e-01 | t=0.0097s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.1214e-01 | t=9.3469s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0016s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0017s
    tikhonov | MR=0.1 | seed=1 | MAE=2.7086e-01 | t=0.0042s
    tv | MR=0.1 | seed=1 | MAE=1.3868e-01 | t=0.4725s
    trss | MR=0.1 | seed=1 | MAE=1.2000e-01 | t=0.0037s

Completed: 2026-04-16T15:38:20.556556+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.