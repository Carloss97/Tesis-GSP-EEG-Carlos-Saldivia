# Integration Log: scr_00569
Started: 2026-04-16T14:20:31.396181+00:00
Description: Screening scr_00569 ds=bci_iv2a_real_s3 graph=knn miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.0042s
    nearest | MR=0.3 | seed=0 | MAE=9.1472e-07 | t=0.0127s
    tikhonov | MR=0.3 | seed=0 | MAE=2.2393e-06 | t=0.0756s
    tv | MR=0.3 | seed=0 | MAE=1.0521e-06 | t=0.8057s
    trss | MR=0.3 | seed=0 | MAE=8.8116e-07 | t=0.5401s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=3.0546e-06 | t=0.0124s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=6.1296e-06 | t=25.8819s
    mean | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.0035s
    nearest | MR=0.3 | seed=1 | MAE=9.0879e-07 | t=0.0114s
    tikhonov | MR=0.3 | seed=1 | MAE=2.2199e-06 | t=0.0086s
    tv | MR=0.3 | seed=1 | MAE=1.0249e-06 | t=0.9641s
    trss | MR=0.3 | seed=1 | MAE=8.7061e-07 | t=0.5848s

Completed: 2026-04-16T14:20:31.397508+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.