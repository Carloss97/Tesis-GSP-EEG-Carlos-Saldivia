# Integration Log: scr_00557
Started: 2026-04-16T14:14:11.373375+00:00
Description: Screening scr_00557 ds=bci_iv2a_real_s3 graph=knn miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.0021s
    nearest | MR=0.3 | seed=0 | MAE=9.1472e-07 | t=0.0081s
    tikhonov | MR=0.3 | seed=0 | MAE=2.0448e-06 | t=0.0060s
    tv | MR=0.3 | seed=0 | MAE=1.0521e-06 | t=0.2287s
    trss | MR=0.3 | seed=0 | MAE=9.1656e-07 | t=0.2610s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.9193e-06 | t=0.0248s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.8370e-06 | t=20.5224s
    mean | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=9.0879e-07 | t=0.0136s
    tikhonov | MR=0.3 | seed=1 | MAE=2.0428e-06 | t=0.0127s
    tv | MR=0.3 | seed=1 | MAE=1.0249e-06 | t=0.2752s
    trss | MR=0.3 | seed=1 | MAE=9.2133e-07 | t=0.2501s

Completed: 2026-04-16T14:14:11.374285+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.