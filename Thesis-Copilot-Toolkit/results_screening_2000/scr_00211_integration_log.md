# Integration Log: scr_00211
Started: 2026-04-16T14:34:10.795051+00:00
Description: Screening scr_00211 ds=iris_graph_signal graph=aew miss=2ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=2ch | seed=0 | MAE=2.7644e-01 | t=0.0328s
    nearest | MR=2ch | seed=0 | MAE=3.5475e-01 | t=0.0028s
    tikhonov | MR=2ch | seed=0 | MAE=2.6057e-01 | t=0.0049s
    tv | MR=2ch | seed=0 | MAE=2.5582e-01 | t=0.1053s
    trss | MR=2ch | seed=0 | MAE=1.9668e-01 | t=0.0039s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=3.1975e-01 | t=0.0039s
    temporal_laplacian | MR=2ch | seed=0 | MAE=5.3908e-01 | t=18.2617s
    mean | MR=2ch | seed=1 | MAE=2.5974e-01 | t=0.0016s
    nearest | MR=2ch | seed=1 | MAE=3.7471e-01 | t=0.0024s
    tikhonov | MR=2ch | seed=1 | MAE=2.3524e-01 | t=0.0036s
    tv | MR=2ch | seed=1 | MAE=2.3899e-01 | t=0.1308s
    trss | MR=2ch | seed=1 | MAE=1.7823e-01 | t=0.0059s

Completed: 2026-04-16T14:34:10.796015+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.