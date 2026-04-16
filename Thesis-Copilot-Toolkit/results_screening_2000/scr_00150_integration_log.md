# Integration Log: scr_00150
Started: 2026-04-16T15:30:01.226517+00:00
Description: Screening scr_00150 ds=iv100hz_mat graph=gaussian miss=2ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=2ch | seed=0 | MAE=2.0300e+01 | t=0.0037s
    nearest | MR=2ch | seed=0 | MAE=3.2925e+01 | t=0.0053s
    tikhonov | MR=2ch | seed=0 | MAE=1.3433e+02 | t=0.0110s
    tv | MR=2ch | seed=0 | MAE=1.1939e+01 | t=0.3977s
    trss | MR=2ch | seed=0 | MAE=1.3969e+01 | t=0.1833s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.0474e+02 | t=0.0279s
    temporal_laplacian | MR=2ch | seed=0 | MAE=2.6591e+02 | t=25.8893s
    mean | MR=2ch | seed=1 | MAE=2.0537e+01 | t=0.0043s
    nearest | MR=2ch | seed=1 | MAE=3.3573e+01 | t=0.0435s
    tikhonov | MR=2ch | seed=1 | MAE=1.3439e+02 | t=0.0151s
    tv | MR=2ch | seed=1 | MAE=1.2631e+01 | t=0.6718s
    trss | MR=2ch | seed=1 | MAE=1.4213e+01 | t=0.1080s

Completed: 2026-04-16T15:30:01.227573+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.