# Integration Log: scr_00511
Started: 2026-04-16T13:56:27.767353+00:00
Description: Screening scr_00511 ds=iris_graph_signal graph=knng miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0014s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0014s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8399e-01 | t=0.0037s
    tv | MR=0.2 | seed=0 | MAE=1.1848e-01 | t=0.1219s
    trss | MR=0.2 | seed=0 | MAE=9.8642e-02 | t=0.0035s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1750e-01 | t=0.0038s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.1507e-01 | t=9.6943s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0201s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0236s
    tikhonov | MR=0.2 | seed=1 | MAE=1.9192e-01 | t=0.0036s
    tv | MR=0.2 | seed=1 | MAE=1.3280e-01 | t=0.0838s
    trss | MR=0.2 | seed=1 | MAE=1.0806e-01 | t=0.0037s

Completed: 2026-04-16T13:56:27.768075+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.