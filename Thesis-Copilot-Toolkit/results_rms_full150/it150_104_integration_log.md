# Integration Log: it150_104
Started: 2026-04-15T00:41:03.569013+00:00
Description: Bulk normalized run it150_104 dataset=movielens_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=3.6531e-02 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=3.6765e-02 | t=0.0045s
    tikhonov | MR=0.2 | seed=0 | MAE=7.8963e-02 | t=0.0074s
    tv | MR=0.2 | seed=0 | MAE=3.6412e-02 | t=0.1938s
    trss | MR=0.2 | seed=0 | MAE=4.4546e-02 | t=0.0197s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5204e-01 | t=0.0089s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5712e-01 | t=1.6977s
    mean | MR=0.2 | seed=1 | MAE=4.0219e-02 | t=0.0023s
    nearest | MR=0.2 | seed=1 | MAE=4.7049e-02 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=8.4449e-02 | t=0.0084s
    tv | MR=0.2 | seed=1 | MAE=4.0230e-02 | t=0.1853s
    trss | MR=0.2 | seed=1 | MAE=5.4127e-02 | t=0.0203s

Completed: 2026-04-15T00:41:03.569789+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.