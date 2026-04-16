# Integration Log: scr_00690
Started: 2026-04-16T15:24:19.426409+00:00
Description: Screening scr_00690 ds=iv100hz_mat graph=gaussian miss=[0.4] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0557e+02 | t=0.0032s
    nearest | MR=0.4 | seed=0 | MAE=1.5725e+02 | t=0.0183s
    tikhonov | MR=0.4 | seed=0 | MAE=1.7708e+02 | t=0.0275s
    tv | MR=0.4 | seed=0 | MAE=7.7888e+01 | t=0.6793s
    trss | MR=0.4 | seed=0 | MAE=8.5031e+01 | t=1.0290s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.1983e+02 | t=0.0513s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=2.8606e+02 | t=22.1687s
    mean | MR=0.4 | seed=1 | MAE=1.0515e+02 | t=0.0056s
    nearest | MR=0.4 | seed=1 | MAE=1.5788e+02 | t=0.0298s
    tikhonov | MR=0.4 | seed=1 | MAE=1.7660e+02 | t=0.0144s
    tv | MR=0.4 | seed=1 | MAE=8.2052e+01 | t=0.4245s
    trss | MR=0.4 | seed=1 | MAE=8.4924e+01 | t=0.0279s

Completed: 2026-04-16T15:24:19.427659+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.