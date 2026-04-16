# Integration Log: scr_01098
Started: 2026-04-16T13:43:39.221359+00:00
Description: Screening scr_01098 ds=iv100hz_mat graph=knn miss=[0.1] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=4.2133e+01 | t=0.2760s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0243e+02 | t=0.0155s
    trss | MR=0.2 | seed=0 | MAE=1.2822e+01 | t=0.1176s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6094e+02 | t=11.7558s
    tv | MR=0.2 | seed=1 | MAE=4.2421e+01 | t=0.3517s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0275e+02 | t=0.0127s
    trss | MR=0.2 | seed=1 | MAE=1.2982e+01 | t=0.1226s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6121e+02 | t=21.9342s
    tv | MR=0.2 | seed=0 | MAE=4.2161e+01 | t=0.5563s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2748e+02 | t=0.0134s
    trss | MR=0.2 | seed=0 | MAE=1.8183e+01 | t=0.1102s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7262e+02 | t=6.9118s

Completed: 2026-04-16T13:43:39.222179+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.