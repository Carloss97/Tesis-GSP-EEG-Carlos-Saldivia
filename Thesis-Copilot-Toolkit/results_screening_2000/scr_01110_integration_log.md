# Integration Log: scr_01110
Started: 2026-04-16T13:53:30.252452+00:00
Description: Screening scr_01110 ds=iv100hz_mat graph=knn miss=[0.1] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=3.9045e+01 | t=0.1520s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1018e+02 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.2509e+01 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6536e+02 | t=20.2551s
    tv | MR=0.2 | seed=1 | MAE=4.0518e+01 | t=0.1769s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1005e+02 | t=0.0134s
    trss | MR=0.2 | seed=1 | MAE=1.2666e+01 | t=0.0231s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6527e+02 | t=22.9962s
    tv | MR=0.2 | seed=0 | MAE=3.8955e+01 | t=0.4535s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3821e+02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.7509e+01 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8200e+02 | t=3.0644s

Completed: 2026-04-16T13:53:30.253149+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.