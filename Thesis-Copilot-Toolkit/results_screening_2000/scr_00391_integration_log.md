# Integration Log: scr_00391
Started: 2026-04-16T13:15:25.768331+00:00
Description: Screening scr_00391 ds=iris_graph_signal graph=kalofolias miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0017s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0020s
    tikhonov | MR=0.1 | seed=0 | MAE=5.3900e-01 | t=0.0037s
    tv | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.1311s
    trss | MR=0.1 | seed=0 | MAE=9.3339e-02 | t=0.0050s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=5.3343e-01 | t=0.0213s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.2372e-01 | t=13.0241s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0010s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0019s
    tikhonov | MR=0.1 | seed=1 | MAE=5.3246e-01 | t=0.0026s
    tv | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0703s
    trss | MR=0.1 | seed=1 | MAE=1.0295e-01 | t=0.0030s

Completed: 2026-04-16T13:15:25.769212+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.