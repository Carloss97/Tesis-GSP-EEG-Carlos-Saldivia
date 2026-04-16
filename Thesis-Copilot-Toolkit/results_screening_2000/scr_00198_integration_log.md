# Integration Log: scr_00198
Started: 2026-04-16T14:27:44.733439+00:00
Description: Screening scr_00198 ds=iv100hz_mat graph=vknng miss=2ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: vknng built OK
    mean | MR=2ch | seed=0 | MAE=2.0300e+01 | t=0.0038s
    nearest | MR=2ch | seed=0 | MAE=3.2925e+01 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=8.5494e+01 | t=0.0086s
    tv | MR=2ch | seed=0 | MAE=1.4026e+01 | t=0.5064s
    trss | MR=2ch | seed=0 | MAE=1.4107e+01 | t=0.0166s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.6418e+02 | t=0.0086s
    temporal_laplacian | MR=2ch | seed=0 | MAE=2.0089e+02 | t=27.8282s
    mean | MR=2ch | seed=1 | MAE=2.0537e+01 | t=0.0257s
    nearest | MR=2ch | seed=1 | MAE=3.3573e+01 | t=0.0079s
    tikhonov | MR=2ch | seed=1 | MAE=8.6007e+01 | t=0.0234s
    tv | MR=2ch | seed=1 | MAE=1.5710e+01 | t=0.6294s
    trss | MR=2ch | seed=1 | MAE=1.4780e+01 | t=0.3162s

Completed: 2026-04-16T14:27:44.734376+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.