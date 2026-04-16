# Integration Log: scr_00460
Started: 2026-04-16T13:38:09.644874+00:00
Description: Screening scr_00460 ds=bci_iv2a_real_s2 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.0111s
    nearest | MR=0.2 | seed=0 | MAE=8.0037e-07 | t=0.0079s
    tikhonov | MR=0.2 | seed=0 | MAE=2.4257e-06 | t=0.0278s
    tv | MR=0.2 | seed=0 | MAE=8.7643e-07 | t=0.2996s
    trss | MR=0.2 | seed=0 | MAE=7.3425e-07 | t=0.3898s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.0770e-06 | t=0.0148s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5830e-05 | t=10.0895s
    mean | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=8.8678e-07 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=2.4368e-06 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=9.0511e-07 | t=0.1751s
    trss | MR=0.2 | seed=1 | MAE=7.4561e-07 | t=0.0195s

Completed: 2026-04-16T13:38:09.646466+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.