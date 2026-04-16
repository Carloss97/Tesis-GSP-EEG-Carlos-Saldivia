# Integration Log: scr_00570
Started: 2026-04-16T14:21:32.907462+00:00
Description: Screening scr_00570 ds=iv100hz_mat graph=knn miss=[0.3] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.3 | seed=0 | MAE=7.3919e+01 | t=0.0021s
    nearest | MR=0.3 | seed=0 | MAE=1.1253e+02 | t=0.0142s
    tikhonov | MR=0.3 | seed=0 | MAE=1.5030e+02 | t=0.0058s
    tv | MR=0.3 | seed=0 | MAE=5.7623e+01 | t=0.1901s
    trss | MR=0.3 | seed=0 | MAE=6.0513e+01 | t=0.0211s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.0531e+02 | t=0.0124s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.5190e+02 | t=20.5665s
    mean | MR=0.3 | seed=1 | MAE=7.2756e+01 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=1.1224e+02 | t=0.0359s
    tikhonov | MR=0.3 | seed=1 | MAE=1.5017e+02 | t=0.0098s
    tv | MR=0.3 | seed=1 | MAE=5.7919e+01 | t=0.3379s
    trss | MR=0.3 | seed=1 | MAE=5.8773e+01 | t=0.0304s

Completed: 2026-04-16T14:21:32.908657+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.