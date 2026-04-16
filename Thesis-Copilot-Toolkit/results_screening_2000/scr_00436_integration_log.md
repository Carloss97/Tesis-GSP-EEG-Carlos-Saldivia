# Integration Log: scr_00436
Started: 2026-04-16T13:30:19.949004+00:00
Description: Screening scr_00436 ds=bci_iv2a_real_s2 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.0036s
    nearest | MR=0.2 | seed=0 | MAE=8.0037e-07 | t=0.0092s
    tikhonov | MR=0.2 | seed=0 | MAE=1.7935e-06 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=8.7642e-07 | t=0.1567s
    trss | MR=0.2 | seed=0 | MAE=7.7309e-07 | t=0.0178s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.7050e-06 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3211e-05 | t=13.9891s
    mean | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.0033s
    nearest | MR=0.2 | seed=1 | MAE=8.8678e-07 | t=0.0088s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8083e-06 | t=0.0263s
    tv | MR=0.2 | seed=1 | MAE=9.0510e-07 | t=0.1585s
    trss | MR=0.2 | seed=1 | MAE=7.9083e-07 | t=0.0177s

Completed: 2026-04-16T13:30:19.949970+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.