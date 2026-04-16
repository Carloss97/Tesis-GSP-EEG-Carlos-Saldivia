# Integration Log: it150_023
Started: 2026-04-15T00:47:00.345181+00:00
Description: Bulk normalized run it150_023 dataset=synthetic_broad graph=knn miss=[0.1] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=5.4881e-02 | t=0.0072s
    nearest | MR=0.1 | seed=0 | MAE=7.5105e-02 | t=0.0068s
    tikhonov | MR=0.1 | seed=0 | MAE=2.6810e-01 | t=0.0085s
    tv | MR=0.1 | seed=0 | MAE=5.5364e-02 | t=0.3747s
    trss | MR=0.1 | seed=0 | MAE=4.0735e-02 | t=0.0200s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.7073e-01 | t=0.0168s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.0423e-01 | t=2.1789s
    mean | MR=0.1 | seed=1 | MAE=5.4906e-02 | t=0.0035s
    nearest | MR=0.1 | seed=1 | MAE=7.4297e-02 | t=0.0054s
    tikhonov | MR=0.1 | seed=1 | MAE=2.6853e-01 | t=0.0087s
    tv | MR=0.1 | seed=1 | MAE=5.5497e-02 | t=0.2353s
    trss | MR=0.1 | seed=1 | MAE=4.0917e-02 | t=0.0195s

Completed: 2026-04-15T00:47:00.348613+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.