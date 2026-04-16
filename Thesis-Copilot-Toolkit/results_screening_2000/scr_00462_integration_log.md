# Integration Log: scr_00462
Started: 2026-04-16T13:39:28.434508+00:00
Description: Screening scr_00462 ds=iv100hz_mat graph=knn miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2754e+01 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=8.0647e+01 | t=0.0078s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3758e+02 | t=0.0112s
    tv | MR=0.2 | seed=0 | MAE=3.8909e+01 | t=0.3298s
    trss | MR=0.2 | seed=0 | MAE=4.0255e+01 | t=0.2332s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0078e+02 | t=0.0404s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4414e+02 | t=17.3205s
    mean | MR=0.2 | seed=1 | MAE=5.2652e+01 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=8.0770e+01 | t=0.0103s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3760e+02 | t=0.0258s
    tv | MR=0.2 | seed=1 | MAE=4.1732e+01 | t=0.4906s
    trss | MR=0.2 | seed=1 | MAE=4.0657e+01 | t=0.3987s

Completed: 2026-04-16T13:39:28.435397+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.