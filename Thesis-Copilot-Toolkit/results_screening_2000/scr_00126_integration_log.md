# Integration Log: scr_00126
Started: 2026-04-16T15:15:57.338625+00:00
Description: Screening scr_00126 ds=iv100hz_mat graph=knn miss=2ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k5 built OK
    mean | MR=2ch | seed=0 | MAE=2.0300e+01 | t=0.0196s
    nearest | MR=2ch | seed=0 | MAE=3.2925e+01 | t=0.0044s
    tikhonov | MR=2ch | seed=0 | MAE=1.0542e+02 | t=0.0421s
    tv | MR=2ch | seed=0 | MAE=1.4325e+01 | t=0.7001s
    trss | MR=2ch | seed=0 | MAE=1.5424e+01 | t=0.5657s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.8283e+02 | t=0.0874s
    temporal_laplacian | MR=2ch | seed=0 | MAE=2.1417e+02 | t=31.5782s
    mean | MR=2ch | seed=1 | MAE=2.0537e+01 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=3.3573e+01 | t=0.0046s
    tikhonov | MR=2ch | seed=1 | MAE=1.0576e+02 | t=0.0087s
    tv | MR=2ch | seed=1 | MAE=1.5275e+01 | t=0.8778s
    trss | MR=2ch | seed=1 | MAE=1.5785e+01 | t=0.1752s

Completed: 2026-04-16T15:15:57.339822+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.