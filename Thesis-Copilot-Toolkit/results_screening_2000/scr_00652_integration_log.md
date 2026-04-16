# Integration Log: scr_00652
Started: 2026-04-16T15:02:02.258585+00:00
Description: Screening scr_00652 ds=bci_iv2a_real_s2 graph=knn miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.0031s
    nearest | MR=0.4 | seed=0 | MAE=1.7309e-06 | t=0.0175s
    tikhonov | MR=0.4 | seed=0 | MAE=2.4492e-06 | t=0.0160s
    tv | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.2106s
    trss | MR=0.4 | seed=0 | MAE=1.5742e-06 | t=0.0213s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=4.9473e-06 | t=0.0080s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.4479e-05 | t=29.8932s
    mean | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.0025s
    nearest | MR=0.4 | seed=1 | MAE=1.7485e-06 | t=0.0098s
    tikhonov | MR=0.4 | seed=1 | MAE=2.4048e-06 | t=0.0089s
    tv | MR=0.4 | seed=1 | MAE=1.7507e-06 | t=0.1913s
    trss | MR=0.4 | seed=1 | MAE=1.5505e-06 | t=0.0199s

Completed: 2026-04-16T15:02:02.259327+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.