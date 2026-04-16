# Integration Log: scr_01323
Started: 2026-04-16T08:34:17.400352+00:00
Description: Screening scr_01323 ds=bci_iv2a_real_s1 graph=knn miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=6.9291e-02 | t=0.1606s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8163e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.6287e-02 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.0268e-01 | t=1.4282s
    tv | MR=0.2 | seed=1 | MAE=6.8250e-02 | t=0.1586s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7974e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.6128e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.0235e-01 | t=1.2691s
    tv | MR=0.2 | seed=0 | MAE=6.9305e-02 | t=0.1648s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2996e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.0721e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7799e-01 | t=1.2934s

Completed: 2026-04-16T08:34:17.401212+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.