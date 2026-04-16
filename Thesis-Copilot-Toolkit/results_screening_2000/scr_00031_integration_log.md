# Integration Log: scr_00031
Started: 2026-04-16T15:32:31.045247+00:00
Description: Screening scr_00031 ds=iris_graph_signal graph=knn miss=1ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0018s
    nearest | MR=1ch | seed=0 | MAE=1.6484e-01 | t=0.0016s
    tikhonov | MR=1ch | seed=0 | MAE=2.6554e-01 | t=0.0517s
    tv | MR=1ch | seed=0 | MAE=1.2451e-01 | t=0.1741s
    trss | MR=1ch | seed=0 | MAE=1.0078e-01 | t=0.0037s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.2277e-01 | t=0.0053s
    temporal_laplacian | MR=1ch | seed=0 | MAE=6.6155e-01 | t=26.7504s
    mean | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0020s
    nearest | MR=1ch | seed=1 | MAE=1.5346e-01 | t=0.0015s
    tikhonov | MR=1ch | seed=1 | MAE=2.7035e-01 | t=0.0037s
    tv | MR=1ch | seed=1 | MAE=1.3724e-01 | t=0.2328s
    trss | MR=1ch | seed=1 | MAE=1.1048e-01 | t=0.1124s

Completed: 2026-04-16T15:32:31.046245+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.