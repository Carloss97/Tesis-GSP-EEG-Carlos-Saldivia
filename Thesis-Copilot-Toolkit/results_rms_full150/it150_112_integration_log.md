# Integration Log: it150_112
Started: 2026-04-15T00:42:25.536978+00:00
Description: Bulk normalized run it150_112 dataset=bci_iv2a_real_s2 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.0024s
    nearest | MR=0.2 | seed=0 | MAE=2.7159e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=0 | MAE=8.4687e-02 | t=0.0088s
    tv | MR=0.2 | seed=0 | MAE=2.9529e-02 | t=0.2963s
    trss | MR=0.2 | seed=0 | MAE=2.4330e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0407e-01 | t=0.0119s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2096e-01 | t=3.6863s
    mean | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.0024s
    nearest | MR=0.2 | seed=1 | MAE=2.8346e-02 | t=0.0059s
    tikhonov | MR=0.2 | seed=1 | MAE=8.4215e-02 | t=0.0088s
    tv | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.2857s
    trss | MR=0.2 | seed=1 | MAE=2.3800e-02 | t=0.0210s

Completed: 2026-04-15T00:42:25.537925+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.