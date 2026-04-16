# Integration Log: scr_00353
Started: 2026-04-16T13:07:10.716446+00:00
Description: Screening scr_00353 ds=bci_iv2a_real_s3 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0031s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0044s
    tikhonov | MR=0.1 | seed=0 | MAE=1.8502e-06 | t=0.0086s
    tv | MR=0.1 | seed=0 | MAE=3.0421e-07 | t=0.1950s
    trss | MR=0.1 | seed=0 | MAE=2.4794e-07 | t=0.0161s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.9183e-06 | t=0.0079s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.8797e-06 | t=6.9619s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=1.8374e-06 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=2.8474e-07 | t=0.1713s
    trss | MR=0.1 | seed=1 | MAE=2.3291e-07 | t=0.0166s

Completed: 2026-04-16T13:07:10.717337+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.