# Integration Log: scr_01158
Started: 2026-04-16T14:44:32.586023+00:00
Description: Screening scr_01158 ds=iv100hz_mat graph=knng miss=[0.1] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=4.2210e+01 | t=0.9915s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.7632e+01 | t=0.0955s
    trss | MR=0.2 | seed=0 | MAE=1.1947e+01 | t=0.3381s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5907e+02 | t=9.2106s
    tv | MR=0.2 | seed=1 | MAE=4.2807e+01 | t=0.1508s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=8.8637e+01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=1.2085e+01 | t=0.0229s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5951e+02 | t=26.6785s
    tv | MR=0.2 | seed=0 | MAE=4.0004e+01 | t=0.2502s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0821e+02 | t=0.0160s
    trss | MR=0.2 | seed=0 | MAE=1.6798e+01 | t=0.3735s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6734e+02 | t=28.3096s

Completed: 2026-04-16T14:44:32.587153+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.