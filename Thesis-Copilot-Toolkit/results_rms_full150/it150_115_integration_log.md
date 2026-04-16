# Integration Log: it150_115
Started: 2026-04-15T00:43:21.594827+00:00
Description: Bulk normalized run it150_115 dataset=iris_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0010s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0012s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6554e-01 | t=0.0036s
    tv | MR=0.2 | seed=0 | MAE=1.2451e-01 | t=0.0761s
    trss | MR=0.2 | seed=0 | MAE=1.0078e-01 | t=0.0042s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2277e-01 | t=0.0041s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6155e-01 | t=0.1275s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0010s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0010s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7035e-01 | t=0.0042s
    tv | MR=0.2 | seed=1 | MAE=1.3724e-01 | t=0.0762s
    trss | MR=0.2 | seed=1 | MAE=1.1048e-01 | t=0.0028s

Completed: 2026-04-15T00:43:21.596075+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.