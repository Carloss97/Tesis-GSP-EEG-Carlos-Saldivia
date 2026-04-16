# Integration Log: scr_00114
Started: 2026-04-16T15:09:40.178248+00:00
Description: Screening scr_00114 ds=iv100hz_mat graph=knn miss=2ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=2.0300e+01 | t=0.0036s
    nearest | MR=2ch | seed=0 | MAE=3.2925e+01 | t=0.0057s
    tikhonov | MR=2ch | seed=0 | MAE=8.2813e+01 | t=0.0229s
    tv | MR=2ch | seed=0 | MAE=1.5888e+01 | t=0.5369s
    trss | MR=2ch | seed=0 | MAE=1.5723e+01 | t=0.2438s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.5864e+02 | t=0.0353s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.9459e+02 | t=24.7404s
    mean | MR=2ch | seed=1 | MAE=2.0537e+01 | t=0.0032s
    nearest | MR=2ch | seed=1 | MAE=3.3573e+01 | t=0.0044s
    tikhonov | MR=2ch | seed=1 | MAE=8.3408e+01 | t=0.0339s
    tv | MR=2ch | seed=1 | MAE=1.8400e+01 | t=0.9842s
    trss | MR=2ch | seed=1 | MAE=1.6440e+01 | t=0.7777s

Completed: 2026-04-16T15:09:40.179494+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.