# Integration Log: it150_119
Started: 2026-04-15T00:55:12.284889+00:00
Description: Bulk normalized run it150_119 dataset=synthetic_broad graph=knn miss=[0.2] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=1.0968e-01 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=1.4989e-01 | t=0.0047s
    tikhonov | MR=0.2 | seed=0 | MAE=3.0517e-01 | t=0.0090s
    tv | MR=0.2 | seed=0 | MAE=1.1112e-01 | t=0.1855s
    trss | MR=0.2 | seed=0 | MAE=8.5704e-02 | t=0.0209s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8611e-01 | t=0.0102s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.2137e-01 | t=1.8366s
    mean | MR=0.2 | seed=1 | MAE=1.1027e-01 | t=0.0027s
    nearest | MR=0.2 | seed=1 | MAE=1.5218e-01 | t=0.0065s
    tikhonov | MR=0.2 | seed=1 | MAE=3.0492e-01 | t=0.0069s
    tv | MR=0.2 | seed=1 | MAE=1.1176e-01 | t=0.1890s
    trss | MR=0.2 | seed=1 | MAE=8.6628e-02 | t=0.0196s

Completed: 2026-04-15T00:55:12.285628+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.