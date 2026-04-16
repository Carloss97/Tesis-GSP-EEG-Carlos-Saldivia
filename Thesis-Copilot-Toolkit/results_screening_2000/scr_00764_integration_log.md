# Integration Log: scr_00764
Started: 2026-04-16T11:54:07.806722+00:00
Description: Screening scr_00764 ds=movielens_graph_signal graph=knn miss=1ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3349e-02 | t=0.1423s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.8406e-02 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=8.0976e-02 | t=0.0181s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1653e-01 | t=1.4448s
    tv | MR=0.2 | seed=1 | MAE=4.3375e-02 | t=0.1420s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.2770e-02 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=8.3600e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2095e-01 | t=1.5038s
    tv | MR=0.2 | seed=0 | MAE=4.3672e-02 | t=0.1405s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0090e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=7.6456e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2361e-01 | t=1.3139s

Completed: 2026-04-16T11:54:07.807573+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.