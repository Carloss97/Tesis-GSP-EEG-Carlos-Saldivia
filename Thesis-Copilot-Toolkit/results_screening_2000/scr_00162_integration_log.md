# Integration Log: scr_00162
Started: 2026-04-16T15:35:43.252292+00:00
Description: Screening scr_00162 ds=iv100hz_mat graph=gaussian miss=2ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=2ch | seed=0 | MAE=2.0300e+01 | t=0.0510s
    nearest | MR=2ch | seed=0 | MAE=3.2925e+01 | t=0.0080s
    tikhonov | MR=2ch | seed=0 | MAE=1.0148e+02 | t=0.0212s
    tv | MR=2ch | seed=0 | MAE=1.2289e+01 | t=1.2525s
    trss | MR=2ch | seed=0 | MAE=1.4800e+01 | t=0.2948s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.8172e+02 | t=0.0549s
    temporal_laplacian | MR=2ch | seed=0 | MAE=2.2467e+02 | t=19.1738s
    mean | MR=2ch | seed=1 | MAE=2.0537e+01 | t=0.0039s
    nearest | MR=2ch | seed=1 | MAE=3.3573e+01 | t=0.0061s
    tikhonov | MR=2ch | seed=1 | MAE=1.0174e+02 | t=0.0089s
    tv | MR=2ch | seed=1 | MAE=1.2851e+01 | t=0.8129s
    trss | MR=2ch | seed=1 | MAE=1.5152e+01 | t=0.4091s

Completed: 2026-04-16T15:35:43.253517+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.