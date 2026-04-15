# Integration Log: it150_079
Started: 2026-04-15T00:36:40.637172+00:00
Description: Bulk normalized run it150_079 dataset=iris_graph_signal graph=vknng miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=42
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0013s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0016s
    tikhonov | MR=0.1 | seed=0 | MAE=2.6554e-01 | t=0.0032s
    tv | MR=0.1 | seed=0 | MAE=1.2451e-01 | t=0.0687s
    trss | MR=0.1 | seed=0 | MAE=1.0078e-01 | t=0.0033s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.2277e-01 | t=0.0027s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.6155e-01 | t=0.0796s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0010s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0017s
    tikhonov | MR=0.1 | seed=1 | MAE=2.7035e-01 | t=0.0030s
    tv | MR=0.1 | seed=1 | MAE=1.3724e-01 | t=0.0655s
    trss | MR=0.1 | seed=1 | MAE=1.1048e-01 | t=0.0031s

Completed: 2026-04-15T00:36:40.638335+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.