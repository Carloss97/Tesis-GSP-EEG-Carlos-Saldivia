# Integration Log: it150_103
Started: 2026-04-15T00:40:43.480416+00:00
Description: Bulk normalized run it150_103 dataset=iris_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0015s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0021s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6763e-01 | t=0.0036s
    tv | MR=0.2 | seed=0 | MAE=1.2623e-01 | t=0.0703s
    trss | MR=0.2 | seed=0 | MAE=1.1223e-01 | t=0.0037s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1809e-01 | t=0.0041s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1214e-01 | t=0.0663s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0013s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7086e-01 | t=0.0027s
    tv | MR=0.2 | seed=1 | MAE=1.3868e-01 | t=0.0646s
    trss | MR=0.2 | seed=1 | MAE=1.2000e-01 | t=0.0037s

Completed: 2026-04-15T00:40:43.481539+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.