# Integration Log: scr_00367
Started: 2026-04-16T13:09:45.126991+00:00
Description: Screening scr_00367 ds=iris_graph_signal graph=gaussian miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0009s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0009s
    tikhonov | MR=0.1 | seed=0 | MAE=1.8399e-01 | t=0.0029s
    tv | MR=0.1 | seed=0 | MAE=1.1848e-01 | t=0.0554s
    trss | MR=0.1 | seed=0 | MAE=9.8642e-02 | t=0.0026s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.1750e-01 | t=0.0025s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.1507e-01 | t=1.0219s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0009s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0009s
    tikhonov | MR=0.1 | seed=1 | MAE=1.9192e-01 | t=0.0023s
    tv | MR=0.1 | seed=1 | MAE=1.3280e-01 | t=0.0521s
    trss | MR=0.1 | seed=1 | MAE=1.0806e-01 | t=0.0026s

Completed: 2026-04-16T13:09:45.128189+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.