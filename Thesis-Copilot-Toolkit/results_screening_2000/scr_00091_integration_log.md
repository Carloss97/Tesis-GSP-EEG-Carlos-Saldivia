# Integration Log: scr_00091
Started: 2026-04-16T14:58:33.320901+00:00
Description: Screening scr_00091 ds=iris_graph_signal graph=vknng miss=1ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0018s
    nearest | MR=1ch | seed=0 | MAE=1.6484e-01 | t=0.0015s
    tikhonov | MR=1ch | seed=0 | MAE=2.6554e-01 | t=0.0038s
    tv | MR=1ch | seed=0 | MAE=1.2451e-01 | t=0.1768s
    trss | MR=1ch | seed=0 | MAE=1.0078e-01 | t=0.0072s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.2277e-01 | t=0.0054s
    temporal_laplacian | MR=1ch | seed=0 | MAE=6.6155e-01 | t=15.1973s
    mean | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0016s
    nearest | MR=1ch | seed=1 | MAE=1.5346e-01 | t=0.0019s
    tikhonov | MR=1ch | seed=1 | MAE=2.7035e-01 | t=0.0035s
    tv | MR=1ch | seed=1 | MAE=1.3724e-01 | t=0.2477s
    trss | MR=1ch | seed=1 | MAE=1.1048e-01 | t=0.0036s

Completed: 2026-04-16T14:58:33.321781+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.