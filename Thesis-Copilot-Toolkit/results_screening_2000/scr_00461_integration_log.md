# Integration Log: scr_00461
Started: 2026-04-16T13:38:50.528925+00:00
Description: Screening scr_00461 ds=bci_iv2a_real_s3 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.4516e-07 | t=0.0050s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0757e-06 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.3138e-07 | t=0.3172s
    trss | MR=0.2 | seed=0 | MAE=6.0551e-07 | t=0.1738s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.0024e-06 | t=0.0408s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.0344e-06 | t=21.8294s
    mean | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=6.4235e-07 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0713e-06 | t=0.0060s
    tv | MR=0.2 | seed=1 | MAE=7.3461e-07 | t=0.2743s
    trss | MR=0.2 | seed=1 | MAE=6.1398e-07 | t=0.0200s

Completed: 2026-04-16T13:38:50.529816+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.