# Integration Log: scr_00437
Started: 2026-04-16T13:31:05.546354+00:00
Description: Screening scr_00437 ds=bci_iv2a_real_s3 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=6.4516e-07 | t=0.0078s
    tikhonov | MR=0.2 | seed=0 | MAE=1.5391e-06 | t=0.0117s
    tv | MR=0.2 | seed=0 | MAE=7.3138e-07 | t=0.3944s
    trss | MR=0.2 | seed=0 | MAE=6.6728e-07 | t=0.2748s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.5584e-06 | t=0.0085s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.0691e-06 | t=15.9115s
    mean | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=6.4235e-07 | t=0.0052s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5341e-06 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=7.3461e-07 | t=0.1491s
    trss | MR=0.2 | seed=1 | MAE=6.7187e-07 | t=0.0178s

Completed: 2026-04-16T13:31:05.547223+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.