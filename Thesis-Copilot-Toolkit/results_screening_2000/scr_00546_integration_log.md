# Integration Log: scr_00546
Started: 2026-04-16T14:09:57.685655+00:00
Description: Screening scr_00546 ds=iv100hz_mat graph=knn miss=[0.3] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=7.3919e+01 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=1.1253e+02 | t=0.0121s
    tikhonov | MR=0.3 | seed=0 | MAE=1.2831e+02 | t=0.0103s
    tv | MR=0.3 | seed=0 | MAE=7.6711e+01 | t=0.3329s
    trss | MR=0.3 | seed=0 | MAE=6.6796e+01 | t=0.0191s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.8002e+02 | t=0.0086s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.1374e+02 | t=18.7654s
    mean | MR=0.3 | seed=1 | MAE=7.2756e+01 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=1.1224e+02 | t=0.0116s
    tikhonov | MR=0.3 | seed=1 | MAE=1.2836e+02 | t=0.0171s
    tv | MR=0.3 | seed=1 | MAE=8.1001e+01 | t=0.3858s
    trss | MR=0.3 | seed=1 | MAE=6.5274e+01 | t=0.1864s

Completed: 2026-04-16T14:09:57.686419+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.