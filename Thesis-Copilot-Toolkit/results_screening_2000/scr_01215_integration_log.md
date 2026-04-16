# Integration Log: scr_01215
Started: 2026-04-16T08:20:53.247573+00:00
Description: Screening scr_01215 ds=bci_iv2a_real_s1 graph=knn miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=6.9291e-02 | t=0.1588s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8163e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.6287e-02 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.0268e-01 | t=2.6664s
    tv | MR=0.2 | seed=1 | MAE=6.8250e-02 | t=0.1590s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7974e-01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=1.6128e-02 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.0235e-01 | t=2.6152s
    tv | MR=0.2 | seed=0 | MAE=6.9305e-02 | t=0.1595s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2996e-01 | t=0.0084s
    trss | MR=0.2 | seed=0 | MAE=2.0721e-02 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7799e-01 | t=3.1201s

Completed: 2026-04-16T08:20:53.248423+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.