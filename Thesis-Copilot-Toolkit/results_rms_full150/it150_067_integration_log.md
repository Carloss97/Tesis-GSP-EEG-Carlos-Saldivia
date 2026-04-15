# Integration Log: it150_067
Started: 2026-04-15T00:34:37.936819+00:00
Description: Bulk normalized run it150_067 dataset=iris_graph_signal graph=knng miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=42
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0011s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0012s
    tikhonov | MR=0.1 | seed=0 | MAE=1.8399e-01 | t=0.0041s
    tv | MR=0.1 | seed=0 | MAE=1.1848e-01 | t=0.0740s
    trss | MR=0.1 | seed=0 | MAE=9.8642e-02 | t=0.0030s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.1750e-01 | t=0.0044s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.1507e-01 | t=0.0851s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0014s
    tikhonov | MR=0.1 | seed=1 | MAE=1.9192e-01 | t=0.0026s
    tv | MR=0.1 | seed=1 | MAE=1.3280e-01 | t=0.0749s
    trss | MR=0.1 | seed=1 | MAE=1.0806e-01 | t=0.0028s

Completed: 2026-04-15T00:34:37.937855+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.