# Integration Log: scr_01304
Started: 2026-04-16T08:32:19.473408+00:00
Description: Screening scr_01304 ds=movielens_graph_signal graph=knn miss=[0.3] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6152e-02 | t=0.1407s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.5056e-02 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=6.2610e-02 | t=0.0202s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2403e-01 | t=2.7205s
    tv | MR=0.2 | seed=1 | MAE=4.0259e-02 | t=0.1416s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.1036e-02 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=7.3387e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2388e-01 | t=2.5144s
    tv | MR=0.2 | seed=0 | MAE=3.6309e-02 | t=0.1409s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0070e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=5.9405e-02 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3112e-01 | t=2.7342s

Completed: 2026-04-16T08:32:19.474358+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.