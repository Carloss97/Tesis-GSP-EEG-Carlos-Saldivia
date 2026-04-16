# Integration Log: scr_00019
Started: 2026-04-16T15:26:08.106127+00:00
Description: Screening scr_00019 ds=iris_graph_signal graph=knn miss=1ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0015s
    nearest | MR=1ch | seed=0 | MAE=1.6484e-01 | t=0.0028s
    tikhonov | MR=1ch | seed=0 | MAE=2.6554e-01 | t=0.0102s
    tv | MR=1ch | seed=0 | MAE=1.2451e-01 | t=0.2795s
    trss | MR=1ch | seed=0 | MAE=1.0078e-01 | t=0.0038s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.2277e-01 | t=0.0045s
    temporal_laplacian | MR=1ch | seed=0 | MAE=6.6155e-01 | t=5.4311s
    mean | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0185s
    nearest | MR=1ch | seed=1 | MAE=1.5346e-01 | t=0.0014s
    tikhonov | MR=1ch | seed=1 | MAE=2.7035e-01 | t=0.0338s
    tv | MR=1ch | seed=1 | MAE=1.3724e-01 | t=0.1118s
    trss | MR=1ch | seed=1 | MAE=1.1048e-01 | t=0.0037s

Completed: 2026-04-16T15:26:08.107055+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.