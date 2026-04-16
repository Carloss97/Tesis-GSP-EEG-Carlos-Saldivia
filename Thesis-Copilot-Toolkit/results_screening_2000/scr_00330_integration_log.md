# Integration Log: scr_00330
Started: 2026-04-16T15:37:56.759302+00:00
Description: Screening scr_00330 ds=iv100hz_mat graph=knn miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0582s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0049s
    tikhonov | MR=0.1 | seed=0 | MAE=8.2813e+01 | t=0.0141s
    tv | MR=0.1 | seed=0 | MAE=1.5888e+01 | t=0.9404s
    trss | MR=0.1 | seed=0 | MAE=1.5723e+01 | t=0.1737s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.5864e+02 | t=0.0758s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.9459e+02 | t=15.6351s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0039s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0188s
    tikhonov | MR=0.1 | seed=1 | MAE=8.3408e+01 | t=0.0194s
    tv | MR=0.1 | seed=1 | MAE=1.8400e+01 | t=0.4418s
    trss | MR=0.1 | seed=1 | MAE=1.6440e+01 | t=0.3014s

Completed: 2026-04-16T15:37:56.760587+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.