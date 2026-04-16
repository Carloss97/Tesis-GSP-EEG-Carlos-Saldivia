# Integration Log: scr_01099
Started: 2026-04-16T13:44:21.758262+00:00
Description: Screening scr_01099 ds=iris_graph_signal graph=knn miss=[0.1] mode=lambda

## Dataset: iris_graph_signal | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=1.1964e-01 | t=0.0617s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2859e-01 | t=0.0025s
    trss | MR=0.2 | seed=0 | MAE=7.5322e-02 | t=0.0027s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.1579e-01 | t=0.6701s
    tv | MR=0.2 | seed=1 | MAE=1.3691e-01 | t=0.1047s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3484e-01 | t=0.0039s
    trss | MR=0.2 | seed=1 | MAE=8.3789e-02 | t=0.0038s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.1664e-01 | t=3.3779s
    tv | MR=0.2 | seed=0 | MAE=1.2279e-01 | t=0.0933s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7710e-01 | t=0.0046s
    trss | MR=0.2 | seed=0 | MAE=7.6621e-02 | t=0.0037s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7619e-01 | t=7.9955s

Completed: 2026-04-16T13:44:21.759391+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.