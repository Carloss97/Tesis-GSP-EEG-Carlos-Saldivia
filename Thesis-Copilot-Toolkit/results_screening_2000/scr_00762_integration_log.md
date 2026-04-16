# Integration Log: scr_00762
Started: 2026-04-16T11:53:52.766531+00:00
Description: Screening scr_00762 ds=iv100hz_mat graph=knn miss=1ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1206e+01 | t=0.1405s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.9974e+01 | t=0.0093s
    trss | MR=0.2 | seed=0 | MAE=1.2847e+01 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5872e+02 | t=1.3610s
    tv | MR=0.2 | seed=1 | MAE=5.1152e+01 | t=0.1509s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.1246e+01 | t=0.0087s
    trss | MR=0.2 | seed=1 | MAE=1.2922e+01 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5936e+02 | t=1.3104s
    tv | MR=0.2 | seed=0 | MAE=4.9607e+01 | t=0.1440s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0930e+02 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=1.8138e+01 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6636e+02 | t=1.2888s

Completed: 2026-04-16T11:53:52.767400+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.