# Integration Log: it150_128
Started: 2026-04-15T00:55:59.510231+00:00
Description: Bulk normalized run it150_128 dataset=movielens_graph_signal graph=gaussian miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=3.6531e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.6765e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3151e-01 | t=0.0073s
    tv | MR=0.2 | seed=0 | MAE=3.6528e-02 | t=0.2278s
    trss | MR=0.2 | seed=0 | MAE=4.5219e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9288e-01 | t=0.0102s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6811e-01 | t=1.8854s
    mean | MR=0.2 | seed=1 | MAE=4.0219e-02 | t=0.0032s
    nearest | MR=0.2 | seed=1 | MAE=4.7049e-02 | t=0.0055s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3082e-01 | t=0.0081s
    tv | MR=0.2 | seed=1 | MAE=4.0219e-02 | t=0.2743s
    trss | MR=0.2 | seed=1 | MAE=4.9681e-02 | t=0.0195s

Completed: 2026-04-15T00:55:59.511251+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.