# Integration Log: scr_00678
Started: 2026-04-16T15:16:52.847022+00:00
Description: Screening scr_00678 ds=iv100hz_mat graph=knn miss=[0.4] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0557e+02 | t=0.0032s
    nearest | MR=0.4 | seed=0 | MAE=1.5725e+02 | t=0.0604s
    tikhonov | MR=0.4 | seed=0 | MAE=1.6976e+02 | t=0.0755s
    tv | MR=0.4 | seed=0 | MAE=1.0302e+02 | t=0.8502s
    trss | MR=0.4 | seed=0 | MAE=9.0892e+01 | t=1.3200s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.1293e+02 | t=0.0774s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=2.6120e+02 | t=32.6049s
    mean | MR=0.4 | seed=1 | MAE=1.0515e+02 | t=0.0032s
    nearest | MR=0.4 | seed=1 | MAE=1.5788e+02 | t=0.0147s
    tikhonov | MR=0.4 | seed=1 | MAE=1.7003e+02 | t=0.0086s
    tv | MR=0.4 | seed=1 | MAE=9.7326e+01 | t=0.7763s
    trss | MR=0.4 | seed=1 | MAE=9.1380e+01 | t=0.4846s

Completed: 2026-04-16T15:16:52.847976+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.