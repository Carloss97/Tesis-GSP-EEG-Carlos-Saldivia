# Integration Log: scr_00703
Started: 2026-04-16T15:31:34.893459+00:00
Description: Screening scr_00703 ds=iris_graph_signal graph=gaussian miss=[0.4] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.4 | seed=0 | MAE=2.7644e-01 | t=0.0039s
    nearest | MR=0.4 | seed=0 | MAE=3.5475e-01 | t=0.0024s
    tikhonov | MR=0.4 | seed=0 | MAE=2.8845e-01 | t=0.0041s
    tv | MR=0.4 | seed=0 | MAE=2.7070e-01 | t=0.7044s
    trss | MR=0.4 | seed=0 | MAE=2.5538e-01 | t=0.0055s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=3.2490e-01 | t=0.0127s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=4.5295e-01 | t=11.5417s
    mean | MR=0.4 | seed=1 | MAE=2.5974e-01 | t=0.0080s
    nearest | MR=0.4 | seed=1 | MAE=3.7471e-01 | t=0.0025s
    tikhonov | MR=0.4 | seed=1 | MAE=2.8703e-01 | t=0.0042s
    tv | MR=0.4 | seed=1 | MAE=2.5923e-01 | t=0.6485s
    trss | MR=0.4 | seed=1 | MAE=2.4612e-01 | t=0.0044s

Completed: 2026-04-16T15:31:34.894470+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.