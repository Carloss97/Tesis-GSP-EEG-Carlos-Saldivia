# Integration Log: it150_091
Started: 2026-04-15T00:38:42.313889+00:00
Description: Bulk normalized run it150_091 dataset=iris_graph_signal graph=aew miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=42
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0009s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0010s
    tikhonov | MR=0.1 | seed=0 | MAE=1.3169e-01 | t=0.0034s
    tv | MR=0.1 | seed=0 | MAE=1.0497e-01 | t=0.0679s
    trss | MR=0.1 | seed=0 | MAE=8.0596e-02 | t=0.0038s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.2150e-01 | t=0.0033s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.6663e-01 | t=0.0627s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0013s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0013s
    tikhonov | MR=0.1 | seed=1 | MAE=1.4471e-01 | t=0.0028s
    tv | MR=0.1 | seed=1 | MAE=1.2292e-01 | t=0.0713s
    trss | MR=0.1 | seed=1 | MAE=9.4878e-02 | t=0.0027s

Completed: 2026-04-15T00:38:42.315212+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.