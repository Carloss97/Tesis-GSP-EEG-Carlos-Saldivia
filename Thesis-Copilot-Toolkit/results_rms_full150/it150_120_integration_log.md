# Integration Log: it150_120
Started: 2026-04-15T00:55:17.176175+00:00
Description: Bulk normalized run it150_120 dataset=synthetic_16ch graph=knn miss=[0.2] mode=base

## Dataset: synthetic_16ch | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2957e-01 | t=0.0024s
    nearest | MR=0.2 | seed=0 | MAE=1.6337e-01 | t=0.0061s
    tikhonov | MR=0.2 | seed=0 | MAE=3.1248e-01 | t=0.0085s
    tv | MR=0.2 | seed=0 | MAE=1.2986e-01 | t=0.1756s
    trss | MR=0.2 | seed=0 | MAE=9.5589e-02 | t=0.0179s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.9650e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4530e-01 | t=0.7048s
    mean | MR=0.2 | seed=1 | MAE=1.2838e-01 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=1.7359e-01 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=3.1175e-01 | t=0.0069s
    tv | MR=0.2 | seed=1 | MAE=1.2861e-01 | t=0.1639s
    trss | MR=0.2 | seed=1 | MAE=9.6594e-02 | t=0.0163s

Completed: 2026-04-15T00:55:17.176958+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.