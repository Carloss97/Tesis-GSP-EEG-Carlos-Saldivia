# Integration Log: scr_01431
Started: 2026-04-16T08:47:44.154285+00:00
Description: Screening scr_01431 ds=bci_iv2a_real_s1 graph=knn miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=6.9291e-02 | t=0.1608s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8163e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.6287e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.0268e-01 | t=1.3271s
    tv | MR=0.2 | seed=1 | MAE=6.8250e-02 | t=0.1613s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7974e-01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=1.6128e-02 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.0235e-01 | t=1.2946s
    tv | MR=0.2 | seed=0 | MAE=6.9305e-02 | t=0.1596s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2996e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=2.0721e-02 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7799e-01 | t=1.2473s

Completed: 2026-04-16T08:47:44.155333+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.