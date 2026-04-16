# Integration Log: scr_00447
Started: 2026-04-16T13:33:46.317132+00:00
Description: Screening scr_00447 ds=bci_iv2a_real_s1 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.2140e-06 | t=0.0049s
    tikhonov | MR=0.2 | seed=0 | MAE=7.1368e-06 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=3.0355e-06 | t=0.1758s
    trss | MR=0.2 | seed=0 | MAE=2.1361e-06 | t=0.2278s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1378e-05 | t=0.0152s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6688e-05 | t=21.5410s
    mean | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=3.5344e-06 | t=0.0090s
    tikhonov | MR=0.2 | seed=1 | MAE=7.3199e-06 | t=0.0086s
    tv | MR=0.2 | seed=1 | MAE=3.3732e-06 | t=0.3463s
    trss | MR=0.2 | seed=1 | MAE=2.4203e-06 | t=0.4154s

Completed: 2026-04-16T13:33:46.317997+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.