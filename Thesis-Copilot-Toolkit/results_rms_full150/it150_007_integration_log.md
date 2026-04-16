# Integration Log: it150_007
Started: 2026-04-15T00:23:17.686136+00:00
Description: Bulk normalized run it150_007 dataset=iris_graph_signal graph=knn miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0015s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0012s
    tikhonov | MR=0.1 | seed=0 | MAE=2.6763e-01 | t=0.0039s
    tv | MR=0.1 | seed=0 | MAE=1.2623e-01 | t=0.0702s
    trss | MR=0.1 | seed=0 | MAE=1.1223e-01 | t=0.0028s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1809e-01 | t=0.0039s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.1214e-01 | t=0.3883s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0013s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0011s
    tikhonov | MR=0.1 | seed=1 | MAE=2.7086e-01 | t=0.0031s
    tv | MR=0.1 | seed=1 | MAE=1.3868e-01 | t=0.0701s
    trss | MR=0.1 | seed=1 | MAE=1.2000e-01 | t=0.0030s

Completed: 2026-04-15T00:23:17.687098+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.