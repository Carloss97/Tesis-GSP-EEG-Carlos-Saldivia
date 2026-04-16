# Integration Log: scr_00545
Started: 2026-04-16T14:09:16.657764+00:00
Description: Screening scr_00545 ds=bci_iv2a_real_s3 graph=knn miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.0038s
    nearest | MR=0.3 | seed=0 | MAE=9.1472e-07 | t=0.0107s
    tikhonov | MR=0.3 | seed=0 | MAE=1.7703e-06 | t=0.0103s
    tv | MR=0.3 | seed=0 | MAE=1.0521e-06 | t=0.3103s
    trss | MR=0.3 | seed=0 | MAE=9.5876e-07 | t=0.0200s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.6641e-06 | t=0.0080s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.2479e-06 | t=24.4188s
    mean | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.0021s
    nearest | MR=0.3 | seed=1 | MAE=9.0879e-07 | t=0.0064s
    tikhonov | MR=0.3 | seed=1 | MAE=1.7435e-06 | t=0.0057s
    tv | MR=0.3 | seed=1 | MAE=1.0249e-06 | t=0.1499s
    trss | MR=0.3 | seed=1 | MAE=9.5742e-07 | t=0.0192s

Completed: 2026-04-16T14:09:16.658519+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.