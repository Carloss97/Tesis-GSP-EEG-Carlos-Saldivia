# Integration Log: scr_00448
Started: 2026-04-16T13:34:27.560556+00:00
Description: Screening scr_00448 ds=bci_iv2a_real_s2 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=8.0037e-07 | t=0.0057s
    tikhonov | MR=0.2 | seed=0 | MAE=2.1508e-06 | t=0.0062s
    tv | MR=0.2 | seed=0 | MAE=8.7644e-07 | t=0.1859s
    trss | MR=0.2 | seed=0 | MAE=7.4709e-07 | t=0.0197s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.9383e-06 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4905e-05 | t=11.2659s
    mean | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=8.8678e-07 | t=0.0077s
    tikhonov | MR=0.2 | seed=1 | MAE=2.1640e-06 | t=0.0317s
    tv | MR=0.2 | seed=1 | MAE=9.0511e-07 | t=0.5841s
    trss | MR=0.2 | seed=1 | MAE=7.6162e-07 | t=0.1403s

Completed: 2026-04-16T13:34:27.561546+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.