# Integration Log: scr_01002
Started: 2026-04-16T12:50:54.495662+00:00
Description: Screening scr_01002 ds=iv100hz_mat graph=knn miss=3ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=3.9045e+01 | t=0.1573s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1018e+02 | t=0.0084s
    trss | MR=0.2 | seed=0 | MAE=1.2509e+01 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6536e+02 | t=3.3198s
    tv | MR=0.2 | seed=1 | MAE=4.0518e+01 | t=0.2791s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1005e+02 | t=0.0180s
    trss | MR=0.2 | seed=1 | MAE=1.2666e+01 | t=0.2510s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6527e+02 | t=8.4053s
    tv | MR=0.2 | seed=0 | MAE=3.8955e+01 | t=0.1509s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3821e+02 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.7509e+01 | t=0.0203s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8200e+02 | t=4.8890s

Completed: 2026-04-16T12:50:54.496352+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.