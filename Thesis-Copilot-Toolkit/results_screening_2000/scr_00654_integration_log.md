# Integration Log: scr_00654
Started: 2026-04-16T15:03:49.156010+00:00
Description: Screening scr_00654 ds=iv100hz_mat graph=knn miss=[0.4] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0557e+02 | t=0.0041s
    nearest | MR=0.4 | seed=0 | MAE=1.5725e+02 | t=0.0137s
    tikhonov | MR=0.4 | seed=0 | MAE=1.5574e+02 | t=0.0086s
    tv | MR=0.4 | seed=0 | MAE=1.2218e+02 | t=0.5745s
    trss | MR=0.4 | seed=0 | MAE=1.0161e+02 | t=0.9130s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.9326e+02 | t=0.0467s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=2.2411e+02 | t=21.7082s
    mean | MR=0.4 | seed=1 | MAE=1.0515e+02 | t=0.0032s
    nearest | MR=0.4 | seed=1 | MAE=1.5788e+02 | t=0.1121s
    tikhonov | MR=0.4 | seed=1 | MAE=1.5667e+02 | t=0.0088s
    tv | MR=0.4 | seed=1 | MAE=1.2090e+02 | t=0.6293s
    trss | MR=0.4 | seed=1 | MAE=1.0097e+02 | t=0.1757s

Completed: 2026-04-16T15:03:49.156876+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.