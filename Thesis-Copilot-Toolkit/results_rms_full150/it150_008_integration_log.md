# Integration Log: it150_008
Started: 2026-04-15T00:23:40.307056+00:00
Description: Bulk normalized run it150_008 dataset=movielens_graph_signal graph=knn miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.0025s
    nearest | MR=0.1 | seed=0 | MAE=1.5567e-02 | t=0.0040s
    tikhonov | MR=0.1 | seed=0 | MAE=6.7635e-02 | t=0.0082s
    tv | MR=0.1 | seed=0 | MAE=1.7363e-02 | t=0.1877s
    trss | MR=0.1 | seed=0 | MAE=2.2534e-02 | t=0.0186s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.4849e-01 | t=0.0107s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.5085e-01 | t=2.2366s
    mean | MR=0.1 | seed=1 | MAE=2.1103e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=2.3466e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=1 | MAE=7.1677e-02 | t=0.0081s
    tv | MR=0.1 | seed=1 | MAE=2.1238e-02 | t=0.1991s
    trss | MR=0.1 | seed=1 | MAE=3.0237e-02 | t=0.0184s

Completed: 2026-04-15T00:23:40.307894+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.