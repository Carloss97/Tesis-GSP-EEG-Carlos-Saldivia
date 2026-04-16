# Integration Log: scr_00186
Started: 2026-04-16T14:21:34.201488+00:00
Description: Screening scr_00186 ds=iv100hz_mat graph=knng miss=2ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knng built OK
    mean | MR=2ch | seed=0 | MAE=2.0300e+01 | t=0.0031s
    nearest | MR=2ch | seed=0 | MAE=3.2925e+01 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=8.2912e+01 | t=0.1114s
    tv | MR=2ch | seed=0 | MAE=1.3573e+01 | t=0.6002s
    trss | MR=2ch | seed=0 | MAE=1.4332e+01 | t=0.0758s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.6135e+02 | t=0.0124s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.9837e+02 | t=17.9316s
    mean | MR=2ch | seed=1 | MAE=2.0537e+01 | t=0.0031s
    nearest | MR=2ch | seed=1 | MAE=3.3573e+01 | t=0.0053s
    tikhonov | MR=2ch | seed=1 | MAE=8.3459e+01 | t=0.0272s
    tv | MR=2ch | seed=1 | MAE=1.5122e+01 | t=0.2683s
    trss | MR=2ch | seed=1 | MAE=1.5023e+01 | t=0.2250s

Completed: 2026-04-16T14:21:34.202834+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.