# Integration Log: scr_00138
Started: 2026-04-16T15:23:13.364892+00:00
Description: Screening scr_00138 ds=iv100hz_mat graph=knn miss=2ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k7 built OK
    mean | MR=2ch | seed=0 | MAE=2.0300e+01 | t=0.0039s
    nearest | MR=2ch | seed=0 | MAE=3.2925e+01 | t=0.0058s
    tikhonov | MR=2ch | seed=0 | MAE=1.1879e+02 | t=0.0116s
    tv | MR=2ch | seed=0 | MAE=1.3851e+01 | t=0.3541s
    trss | MR=2ch | seed=0 | MAE=1.4773e+01 | t=0.1742s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.9382e+02 | t=0.0332s
    temporal_laplacian | MR=2ch | seed=0 | MAE=2.3416e+02 | t=20.5777s
    mean | MR=2ch | seed=1 | MAE=2.0537e+01 | t=0.0040s
    nearest | MR=2ch | seed=1 | MAE=3.3573e+01 | t=0.0053s
    tikhonov | MR=2ch | seed=1 | MAE=1.1899e+02 | t=0.0176s
    tv | MR=2ch | seed=1 | MAE=1.4633e+01 | t=0.6183s
    trss | MR=2ch | seed=1 | MAE=1.5067e+01 | t=0.7418s

Completed: 2026-04-16T15:23:13.366285+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.