# Integration Log: scr_00978
Started: 2026-04-16T12:42:21.227217+00:00
Description: Screening scr_00978 ds=iv100hz_mat graph=knn miss=3ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1206e+01 | t=0.2801s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.9974e+01 | t=0.0144s
    trss | MR=0.2 | seed=0 | MAE=1.2847e+01 | t=0.0859s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5872e+02 | t=2.1485s
    tv | MR=0.2 | seed=1 | MAE=5.1152e+01 | t=0.1416s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.1246e+01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.2922e+01 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5936e+02 | t=4.9775s
    tv | MR=0.2 | seed=0 | MAE=4.9607e+01 | t=0.3048s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0930e+02 | t=0.0122s
    trss | MR=0.2 | seed=0 | MAE=1.8138e+01 | t=0.0919s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6636e+02 | t=5.3150s

Completed: 2026-04-16T12:42:21.228103+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.