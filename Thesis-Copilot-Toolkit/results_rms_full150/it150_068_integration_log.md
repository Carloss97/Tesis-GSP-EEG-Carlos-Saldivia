# Integration Log: it150_068
Started: 2026-04-15T00:34:59.401394+00:00
Description: Bulk normalized run it150_068 dataset=movielens_graph_signal graph=knng miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=1.5567e-02 | t=0.0048s
    tikhonov | MR=0.1 | seed=0 | MAE=7.1315e-02 | t=0.0082s
    tv | MR=0.1 | seed=0 | MAE=1.7336e-02 | t=0.2101s
    trss | MR=0.1 | seed=0 | MAE=2.2504e-02 | t=0.0207s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.5349e-01 | t=0.0109s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.5203e-01 | t=2.2513s
    mean | MR=0.1 | seed=1 | MAE=2.1103e-02 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=2.3466e-02 | t=0.0038s
    tikhonov | MR=0.1 | seed=1 | MAE=7.5505e-02 | t=0.0090s
    tv | MR=0.1 | seed=1 | MAE=2.1171e-02 | t=0.2030s
    trss | MR=0.1 | seed=1 | MAE=3.0841e-02 | t=0.0197s

Completed: 2026-04-15T00:34:59.402579+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.