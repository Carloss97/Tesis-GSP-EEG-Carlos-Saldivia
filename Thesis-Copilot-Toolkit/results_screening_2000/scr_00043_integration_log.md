# Integration Log: scr_00043
Started: 2026-04-16T15:38:12.819152+00:00
Description: Screening scr_00043 ds=iris_graph_signal graph=gaussian miss=1ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0017s
    nearest | MR=1ch | seed=0 | MAE=1.6484e-01 | t=0.0022s
    tikhonov | MR=1ch | seed=0 | MAE=1.8399e-01 | t=0.0042s
    tv | MR=1ch | seed=0 | MAE=1.1848e-01 | t=0.1504s
    trss | MR=1ch | seed=0 | MAE=9.8642e-02 | t=0.0041s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=3.1750e-01 | t=0.0046s
    temporal_laplacian | MR=1ch | seed=0 | MAE=5.1507e-01 | t=1.5703s
    mean | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0018s
    nearest | MR=1ch | seed=1 | MAE=1.5346e-01 | t=0.0016s
    tikhonov | MR=1ch | seed=1 | MAE=1.9192e-01 | t=0.0037s
    tv | MR=1ch | seed=1 | MAE=1.3280e-01 | t=0.2792s
    trss | MR=1ch | seed=1 | MAE=1.0806e-01 | t=0.0041s

Completed: 2026-04-16T15:38:12.820303+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.