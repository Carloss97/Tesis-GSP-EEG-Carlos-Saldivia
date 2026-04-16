# Integration Log: scr_01299
Started: 2026-04-16T08:31:15.994972+00:00
Description: Screening scr_01299 ds=bci_iv2a_real_s1 graph=knn miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=6.9289e-02 | t=0.1530s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3744e-01 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.8926e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4015e-01 | t=1.2531s
    tv | MR=0.2 | seed=1 | MAE=6.8249e-02 | t=0.1459s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.3595e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.9399e-02 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.4118e-01 | t=1.2540s
    tv | MR=0.2 | seed=0 | MAE=6.9304e-02 | t=0.1467s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6865e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=2.3155e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8676e-01 | t=1.2567s

Completed: 2026-04-16T08:31:15.995819+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.