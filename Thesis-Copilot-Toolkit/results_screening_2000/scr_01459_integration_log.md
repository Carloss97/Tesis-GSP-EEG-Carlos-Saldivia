# Integration Log: scr_01459
Started: 2026-04-16T08:51:38.956095+00:00
Description: Screening scr_01459 ds=iris_graph_signal graph=gaussian miss=[0.4] mode=lambda

## Dataset: iris_graph_signal | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=1.0884e-01 | t=0.0523s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7061e-01 | t=0.0025s
    trss | MR=0.2 | seed=0 | MAE=1.1925e-01 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4333e-01 | t=0.7090s
    tv | MR=0.2 | seed=1 | MAE=1.2384e-01 | t=0.0519s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.8119e-01 | t=0.0028s
    trss | MR=0.2 | seed=1 | MAE=1.2643e-01 | t=0.0028s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.4371e-01 | t=0.5867s
    tv | MR=0.2 | seed=0 | MAE=1.0993e-01 | t=0.0528s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7459e-01 | t=0.0025s
    trss | MR=0.2 | seed=0 | MAE=1.1755e-01 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4772e-01 | t=0.7856s

Completed: 2026-04-16T08:51:38.956816+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.