# Integration Log: it110_iris_graph_baseline
Started: 2026-04-06T19:16:23.741264+00:00
Description: Iris graph-signal baseline

## Dataset: iris_graph_signal | rows=168
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0023s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0018s
    tikhonov | MR=0.1 | seed=0 | MAE=2.6471e-01 | t=0.0049s
    tv | MR=0.1 | seed=0 | MAE=1.2578e-01 | t=0.0997s
    trss | MR=0.1 | seed=0 | MAE=1.0362e-01 | t=0.0073s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1982e-01 | t=0.0073s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.3675e-01 | t=0.0149s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0027s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0018s
    tikhonov | MR=0.1 | seed=1 | MAE=2.6943e-01 | t=0.0048s
    tv | MR=0.1 | seed=1 | MAE=1.3774e-01 | t=0.1000s
    trss | MR=0.1 | seed=1 | MAE=1.1253e-01 | t=0.0075s

Completed: 2026-04-06T19:16:23.742959+00:00
Total rows: 168
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.