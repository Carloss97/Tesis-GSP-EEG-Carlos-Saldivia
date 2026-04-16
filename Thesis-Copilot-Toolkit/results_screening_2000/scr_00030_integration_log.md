# Integration Log: scr_00030
Started: 2026-04-16T15:31:46.362759+00:00
Description: Screening scr_00030 ds=iv100hz_mat graph=knn miss=1ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k7 built OK
    mean | MR=1ch | seed=0 | MAE=1.1091e+01 | t=0.0472s
    nearest | MR=1ch | seed=0 | MAE=1.6962e+01 | t=0.0382s
    tikhonov | MR=1ch | seed=0 | MAE=1.1299e+02 | t=0.0125s
    tv | MR=1ch | seed=0 | MAE=7.8322e+00 | t=1.0344s
    trss | MR=1ch | seed=0 | MAE=7.6742e+00 | t=0.2878s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.9156e+02 | t=0.0313s
    temporal_laplacian | MR=1ch | seed=0 | MAE=2.3150e+02 | t=20.5386s
    mean | MR=1ch | seed=1 | MAE=1.0242e+01 | t=0.0369s
    nearest | MR=1ch | seed=1 | MAE=1.6572e+01 | t=0.0038s
    tikhonov | MR=1ch | seed=1 | MAE=1.1289e+02 | t=0.0742s
    tv | MR=1ch | seed=1 | MAE=7.0832e+00 | t=0.8648s
    trss | MR=1ch | seed=1 | MAE=7.4632e+00 | t=0.3385s

Completed: 2026-04-16T15:31:46.365164+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.