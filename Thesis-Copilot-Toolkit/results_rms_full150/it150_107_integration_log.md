# Integration Log: it150_107
Started: 2026-04-15T00:54:39.697058+00:00
Description: Bulk normalized run it150_107 dataset=synthetic_broad graph=knn miss=[0.2] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.0968e-01 | t=0.0102s
    nearest | MR=0.2 | seed=0 | MAE=1.4989e-01 | t=0.0111s
    tikhonov | MR=0.2 | seed=0 | MAE=2.4852e-01 | t=0.0183s
    tv | MR=0.2 | seed=0 | MAE=1.1538e-01 | t=0.4805s
    trss | MR=0.2 | seed=0 | MAE=8.6793e-02 | t=0.0207s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2279e-01 | t=0.0132s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2987e-01 | t=4.2694s
    mean | MR=0.2 | seed=1 | MAE=1.1027e-01 | t=0.0045s
    nearest | MR=0.2 | seed=1 | MAE=1.5218e-01 | t=0.0107s
    tikhonov | MR=0.2 | seed=1 | MAE=2.4823e-01 | t=0.0228s
    tv | MR=0.2 | seed=1 | MAE=1.1486e-01 | t=0.2203s
    trss | MR=0.2 | seed=1 | MAE=8.7090e-02 | t=0.0209s

Completed: 2026-04-15T00:54:39.698319+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.