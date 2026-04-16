# Integration Log: it150_139
Started: 2026-04-15T00:57:15.024706+00:00
Description: Bulk normalized run it150_139 dataset=iris_graph_signal graph=gaussian miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0013s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0010s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4209e-01 | t=0.0024s
    tv | MR=0.2 | seed=0 | MAE=1.0936e-01 | t=0.0710s
    trss | MR=0.2 | seed=0 | MAE=1.0897e-01 | t=0.0031s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.1049e-01 | t=0.0028s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8607e-01 | t=0.0912s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0010s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0013s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5325e-01 | t=0.0027s
    tv | MR=0.2 | seed=1 | MAE=1.2181e-01 | t=0.0650s
    trss | MR=0.2 | seed=1 | MAE=1.1909e-01 | t=0.0027s

Completed: 2026-04-15T00:57:15.025555+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.