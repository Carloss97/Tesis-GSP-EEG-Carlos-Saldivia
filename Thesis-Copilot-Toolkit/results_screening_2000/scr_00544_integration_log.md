# Integration Log: scr_00544
Started: 2026-04-16T14:08:29.213699+00:00
Description: Screening scr_00544 ds=bci_iv2a_real_s2 graph=knn miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.0035s
    nearest | MR=0.3 | seed=0 | MAE=1.2061e-06 | t=0.0141s
    tikhonov | MR=0.3 | seed=0 | MAE=2.0571e-06 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.2786s
    trss | MR=0.3 | seed=0 | MAE=1.0928e-06 | t=0.0198s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=4.8088e-06 | t=0.0083s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.3719e-05 | t=23.8013s
    mean | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.0219s
    nearest | MR=0.3 | seed=1 | MAE=1.1920e-06 | t=0.0073s
    tikhonov | MR=0.3 | seed=1 | MAE=2.0446e-06 | t=0.0062s
    tv | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.1711s
    trss | MR=0.3 | seed=1 | MAE=1.0610e-06 | t=0.0215s

Completed: 2026-04-16T14:08:29.214550+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.