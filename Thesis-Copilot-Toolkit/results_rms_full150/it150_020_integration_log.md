# Integration Log: it150_020
Started: 2026-04-15T00:25:50.041551+00:00
Description: Bulk normalized run it150_020 dataset=movielens_graph_signal graph=knn miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=1.5567e-02 | t=0.0041s
    tikhonov | MR=0.1 | seed=0 | MAE=8.8160e-02 | t=0.0071s
    tv | MR=0.1 | seed=0 | MAE=1.7345e-02 | t=0.1689s
    trss | MR=0.1 | seed=0 | MAE=2.4535e-02 | t=0.0185s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.6826e-01 | t=0.0101s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.5655e-01 | t=1.8838s
    mean | MR=0.1 | seed=1 | MAE=2.1103e-02 | t=0.0035s
    nearest | MR=0.1 | seed=1 | MAE=2.3466e-02 | t=0.0046s
    tikhonov | MR=0.1 | seed=1 | MAE=8.9529e-02 | t=0.0089s
    tv | MR=0.1 | seed=1 | MAE=2.1141e-02 | t=0.2927s
    trss | MR=0.1 | seed=1 | MAE=2.9443e-02 | t=0.0386s

Completed: 2026-04-15T00:25:50.042475+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.