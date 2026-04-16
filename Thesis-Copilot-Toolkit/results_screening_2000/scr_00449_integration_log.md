# Integration Log: scr_00449
Started: 2026-04-16T13:34:51.104123+00:00
Description: Screening scr_00449 ds=bci_iv2a_real_s3 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=6.4516e-07 | t=0.0076s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8672e-06 | t=0.0090s
    tv | MR=0.2 | seed=0 | MAE=7.3140e-07 | t=0.2319s
    trss | MR=0.2 | seed=0 | MAE=6.4542e-07 | t=0.2600s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8546e-06 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.7120e-06 | t=4.9300s
    mean | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=6.4235e-07 | t=0.0194s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8609e-06 | t=0.0132s
    tv | MR=0.2 | seed=1 | MAE=7.3462e-07 | t=0.2990s
    trss | MR=0.2 | seed=1 | MAE=6.5052e-07 | t=0.0181s

Completed: 2026-04-16T13:34:51.120802+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.