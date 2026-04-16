# Integration Log: scr_00007
Started: 2026-04-16T15:19:44.691996+00:00
Description: Screening scr_00007 ds=iris_graph_signal graph=knn miss=1ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0016s
    nearest | MR=1ch | seed=0 | MAE=1.6484e-01 | t=0.0015s
    tikhonov | MR=1ch | seed=0 | MAE=2.6763e-01 | t=0.0036s
    tv | MR=1ch | seed=0 | MAE=1.2623e-01 | t=0.1792s
    trss | MR=1ch | seed=0 | MAE=1.1223e-01 | t=0.0039s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.1809e-01 | t=0.0039s
    temporal_laplacian | MR=1ch | seed=0 | MAE=6.1214e-01 | t=10.3926s
    mean | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0203s
    nearest | MR=1ch | seed=1 | MAE=1.5346e-01 | t=0.0210s
    tikhonov | MR=1ch | seed=1 | MAE=2.7086e-01 | t=0.0302s
    tv | MR=1ch | seed=1 | MAE=1.3868e-01 | t=0.1906s
    trss | MR=1ch | seed=1 | MAE=1.2000e-01 | t=0.0040s

Completed: 2026-04-16T15:19:44.693571+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.