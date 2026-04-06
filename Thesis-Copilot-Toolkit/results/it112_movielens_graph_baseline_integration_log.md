# Integration Log: it112_movielens_graph_baseline
Started: 2026-04-06T19:19:39.237208+00:00
Description: MovieLens graph-signal baseline

## Dataset: movielens_graph_signal | rows=140
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0052s
    tikhonov | MR=0.1 | seed=0 | MAE=5.9092e-02 | t=0.0123s
    tv | MR=0.1 | seed=0 | MAE=1.4570e-02 | t=0.2811s
    trss | MR=0.1 | seed=0 | MAE=1.7555e-02 | t=0.0336s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.3606e-01 | t=0.0158s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4080e-01 | t=7.2346s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0035s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=6.4536e-02 | t=0.0124s
    tv | MR=0.1 | seed=1 | MAE=1.9193e-02 | t=0.2827s
    trss | MR=0.1 | seed=1 | MAE=2.7197e-02 | t=0.0329s

Completed: 2026-04-06T19:19:39.238553+00:00
Total rows: 140
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.