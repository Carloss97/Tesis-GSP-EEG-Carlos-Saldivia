# Integration Log: scr_00341
Started: 2026-04-16T13:05:20.753218+00:00
Description: Screening scr_00341 ds=bci_iv2a_real_s3 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0027s
    tikhonov | MR=0.1 | seed=0 | MAE=1.6053e-06 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=3.0422e-07 | t=0.1607s
    trss | MR=0.1 | seed=0 | MAE=2.6523e-07 | t=0.0173s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.7461e-06 | t=0.0079s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.5097e-06 | t=5.4880s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0044s
    tikhonov | MR=0.1 | seed=1 | MAE=1.5892e-06 | t=0.0058s
    tv | MR=0.1 | seed=1 | MAE=2.8474e-07 | t=0.1671s
    trss | MR=0.1 | seed=1 | MAE=2.5138e-07 | t=0.0174s

Completed: 2026-04-16T13:05:20.754070+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.