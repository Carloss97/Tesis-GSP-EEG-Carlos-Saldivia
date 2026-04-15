# Integration Log: it150_118
Started: 2026-04-15T00:55:04.597352+00:00
Description: Bulk normalized run it150_118 dataset=synthetic_beta graph=knn miss=[0.2] mode=base

## Dataset: synthetic_beta | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2957e-01 | t=0.0024s
    nearest | MR=0.2 | seed=0 | MAE=1.6337e-01 | t=0.0044s
    tikhonov | MR=0.2 | seed=0 | MAE=3.1248e-01 | t=0.0067s
    tv | MR=0.2 | seed=0 | MAE=1.2986e-01 | t=0.1730s
    trss | MR=0.2 | seed=0 | MAE=9.5589e-02 | t=0.0174s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.9650e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4530e-01 | t=1.7311s
    mean | MR=0.2 | seed=1 | MAE=1.2838e-01 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=1.7359e-01 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=3.1175e-01 | t=0.0097s
    tv | MR=0.2 | seed=1 | MAE=1.2861e-01 | t=0.1814s
    trss | MR=0.2 | seed=1 | MAE=9.6594e-02 | t=0.0169s

Completed: 2026-04-15T00:55:04.598071+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.