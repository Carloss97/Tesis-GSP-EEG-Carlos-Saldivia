# Integration Log: scr_01300
Started: 2026-04-16T08:31:34.219637+00:00
Description: Screening scr_01300 ds=bci_iv2a_real_s2 graph=knn miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=2.9531e-02 | t=0.1458s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6400e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.4513e-02 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.1673e-01 | t=1.2652s
    tv | MR=0.2 | seed=1 | MAE=2.8796e-02 | t=0.1459s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.6300e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.4619e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.1743e-01 | t=2.8586s
    tv | MR=0.2 | seed=0 | MAE=2.9530e-02 | t=0.1456s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6893e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.5414e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9987e-01 | t=2.6776s

Completed: 2026-04-16T08:31:34.220487+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.