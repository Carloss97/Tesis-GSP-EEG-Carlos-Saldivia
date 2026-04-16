# Integration Log: it150_043
Started: 2026-04-15T00:29:57.172325+00:00
Description: Bulk normalized run it150_043 dataset=iris_graph_signal graph=gaussian miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0010s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0010s
    tikhonov | MR=0.1 | seed=0 | MAE=1.4209e-01 | t=0.0029s
    tv | MR=0.1 | seed=0 | MAE=1.0936e-01 | t=0.0608s
    trss | MR=0.1 | seed=0 | MAE=1.0897e-01 | t=0.0027s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.1049e-01 | t=0.0025s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=3.8607e-01 | t=0.0535s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0009s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0011s
    tikhonov | MR=0.1 | seed=1 | MAE=1.5325e-01 | t=0.0034s
    tv | MR=0.1 | seed=1 | MAE=1.2181e-01 | t=0.0595s
    trss | MR=0.1 | seed=1 | MAE=1.1909e-01 | t=0.0028s

Completed: 2026-04-15T00:29:57.173222+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.