# Integration Log: scr_00350
Started: 2026-04-16T13:06:20.879707+00:00
Description: Screening scr_00350 ds=physionet_real graph=knn miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0027s
    tikhonov | MR=0.1 | seed=0 | MAE=8.2154e-06 | t=0.0069s
    tv | MR=0.1 | seed=0 | MAE=2.0831e-06 | t=0.1677s
    trss | MR=0.1 | seed=0 | MAE=1.0520e-06 | t=0.0160s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.5884e-05 | t=0.0081s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=3.4096e-05 | t=6.8728s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=8.1835e-06 | t=0.0056s
    tv | MR=0.1 | seed=1 | MAE=2.0437e-06 | t=0.1577s
    trss | MR=0.1 | seed=1 | MAE=1.0412e-06 | t=0.0169s

Completed: 2026-04-16T13:06:20.880581+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.