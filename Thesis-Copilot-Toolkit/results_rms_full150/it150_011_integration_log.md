# Integration Log: it150_011
Started: 2026-04-15T00:46:04.133899+00:00
Description: Bulk normalized run it150_011 dataset=synthetic_broad graph=knn miss=[0.1] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=5.4881e-02 | t=0.0090s
    nearest | MR=0.1 | seed=0 | MAE=7.5105e-02 | t=0.0051s
    tikhonov | MR=0.1 | seed=0 | MAE=2.0337e-01 | t=0.0143s
    tv | MR=0.1 | seed=0 | MAE=5.6654e-02 | t=0.2189s
    trss | MR=0.1 | seed=0 | MAE=4.0943e-02 | t=0.0186s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.0029e-01 | t=0.0114s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.0600e-01 | t=7.7985s
    mean | MR=0.1 | seed=1 | MAE=5.4906e-02 | t=0.0067s
    nearest | MR=0.1 | seed=1 | MAE=7.4297e-02 | t=0.0062s
    tikhonov | MR=0.1 | seed=1 | MAE=2.0368e-01 | t=0.0095s
    tv | MR=0.1 | seed=1 | MAE=5.7210e-02 | t=0.2100s
    trss | MR=0.1 | seed=1 | MAE=4.0180e-02 | t=0.0191s

Completed: 2026-04-15T00:46:04.134936+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.