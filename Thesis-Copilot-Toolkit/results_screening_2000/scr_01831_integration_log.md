# Integration Log: scr_01831
Started: 2026-04-16T09:43:19.005551+00:00
Description: Screening scr_01831 ds=iris_graph_signal graph=aew miss=3ch mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0009s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0012s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3253e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.1092e-01 | t=0.0524s
    trss | MR=0.2 | seed=0 | MAE=8.1404e-02 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2290e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.6750e-01 | t=0.0229s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=1 | MAE=1.4631e-01 | t=0.0023s
    tv | MR=0.2 | seed=1 | MAE=1.2383e-01 | t=0.0515s
    trss | MR=0.2 | seed=1 | MAE=9.6426e-02 | t=0.0026s

Completed: 2026-04-16T09:43:19.006384+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.