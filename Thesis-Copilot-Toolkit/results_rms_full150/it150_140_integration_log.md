# Integration Log: it150_140
Started: 2026-04-15T00:57:22.570020+00:00
Description: Bulk normalized run it150_140 dataset=movielens_graph_signal graph=gaussian miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=3.6531e-02 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=3.6765e-02 | t=0.0057s
    tikhonov | MR=0.2 | seed=0 | MAE=9.8276e-02 | t=0.0069s
    tv | MR=0.2 | seed=0 | MAE=3.6512e-02 | t=0.2337s
    trss | MR=0.2 | seed=0 | MAE=4.4821e-02 | t=0.0199s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7231e-01 | t=0.0091s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5835e-01 | t=1.7440s
    mean | MR=0.2 | seed=1 | MAE=4.0219e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=4.7049e-02 | t=0.0052s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0054e-01 | t=0.0074s
    tv | MR=0.2 | seed=1 | MAE=4.0227e-02 | t=0.2344s
    trss | MR=0.2 | seed=1 | MAE=5.1463e-02 | t=0.0189s

Completed: 2026-04-15T00:57:22.570725+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.