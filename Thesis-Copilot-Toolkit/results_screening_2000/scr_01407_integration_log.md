# Integration Log: scr_01407
Started: 2026-04-16T08:44:45.667538+00:00
Description: Screening scr_01407 ds=bci_iv2a_real_s1 graph=knn miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=6.9289e-02 | t=0.1467s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3744e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.8926e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4015e-01 | t=1.2621s
    tv | MR=0.2 | seed=1 | MAE=6.8249e-02 | t=0.1457s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.3595e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.9399e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.4118e-01 | t=1.3198s
    tv | MR=0.2 | seed=0 | MAE=6.9304e-02 | t=0.1472s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6865e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.3155e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8676e-01 | t=1.3001s

Completed: 2026-04-16T08:44:45.668404+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.