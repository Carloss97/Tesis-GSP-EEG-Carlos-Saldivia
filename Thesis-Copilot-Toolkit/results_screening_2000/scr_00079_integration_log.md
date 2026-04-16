# Integration Log: scr_00079
Started: 2026-04-16T14:52:51.207912+00:00
Description: Screening scr_00079 ds=iris_graph_signal graph=knng miss=1ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0019s
    nearest | MR=1ch | seed=0 | MAE=1.6484e-01 | t=0.0016s
    tikhonov | MR=1ch | seed=0 | MAE=1.8399e-01 | t=0.0039s
    tv | MR=1ch | seed=0 | MAE=1.1848e-01 | t=0.2338s
    trss | MR=1ch | seed=0 | MAE=9.8642e-02 | t=0.0036s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=3.1750e-01 | t=0.0038s
    temporal_laplacian | MR=1ch | seed=0 | MAE=5.1507e-01 | t=10.7538s
    mean | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0016s
    nearest | MR=1ch | seed=1 | MAE=1.5346e-01 | t=0.0015s
    tikhonov | MR=1ch | seed=1 | MAE=1.9192e-01 | t=0.0035s
    tv | MR=1ch | seed=1 | MAE=1.3280e-01 | t=0.1738s
    trss | MR=1ch | seed=1 | MAE=1.0806e-01 | t=0.0036s

Completed: 2026-04-16T14:52:51.209112+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.