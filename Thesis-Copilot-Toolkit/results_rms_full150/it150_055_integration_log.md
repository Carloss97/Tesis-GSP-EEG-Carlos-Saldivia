# Integration Log: it150_055
Started: 2026-04-15T00:32:10.169250+00:00
Description: Bulk normalized run it150_055 dataset=iris_graph_signal graph=kalofolias miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=42
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0010s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0010s
    tikhonov | MR=0.1 | seed=0 | MAE=5.3900e-01 | t=0.0025s
    tv | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0753s
    trss | MR=0.1 | seed=0 | MAE=9.3339e-02 | t=0.0033s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=5.3343e-01 | t=0.0033s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.2372e-01 | t=0.1155s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0013s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0014s
    tikhonov | MR=0.1 | seed=1 | MAE=5.3246e-01 | t=0.0030s
    tv | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0645s
    trss | MR=0.1 | seed=1 | MAE=1.0295e-01 | t=0.0033s

Completed: 2026-04-15T00:32:10.170150+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.