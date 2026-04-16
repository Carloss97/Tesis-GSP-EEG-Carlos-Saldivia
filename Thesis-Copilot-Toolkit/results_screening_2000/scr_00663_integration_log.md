# Integration Log: scr_00663
Started: 2026-04-16T15:07:06.517506+00:00
Description: Screening scr_00663 ds=bci_iv2a_real_s1 graph=knn miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=0.0042s
    nearest | MR=0.4 | seed=0 | MAE=6.5281e-06 | t=0.0217s
    tikhonov | MR=0.4 | seed=0 | MAE=9.2603e-06 | t=0.0090s
    tv | MR=0.4 | seed=0 | MAE=6.3027e-06 | t=0.4958s
    trss | MR=0.4 | seed=0 | MAE=4.6720e-06 | t=0.1596s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.2516e-05 | t=0.0761s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.7573e-05 | t=29.4720s
    mean | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=6.8607e-06 | t=0.0139s
    tikhonov | MR=0.4 | seed=1 | MAE=9.2016e-06 | t=0.0393s
    tv | MR=0.4 | seed=1 | MAE=6.2501e-06 | t=0.3509s
    trss | MR=0.4 | seed=1 | MAE=4.6727e-06 | t=0.7082s

Completed: 2026-04-16T15:07:06.518937+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.