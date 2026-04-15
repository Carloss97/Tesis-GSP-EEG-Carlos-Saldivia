# Integration Log: it150_080
Started: 2026-04-15T00:37:00.982558+00:00
Description: Bulk normalized run it150_080 dataset=movielens_graph_signal graph=vknng miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.0022s
    nearest | MR=0.1 | seed=0 | MAE=1.5567e-02 | t=0.0039s
    tikhonov | MR=0.1 | seed=0 | MAE=7.4668e-02 | t=0.0073s
    tv | MR=0.1 | seed=0 | MAE=1.7334e-02 | t=0.1925s
    trss | MR=0.1 | seed=0 | MAE=2.2691e-02 | t=0.0191s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.5652e-01 | t=0.0122s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.5345e-01 | t=2.7934s
    mean | MR=0.1 | seed=1 | MAE=2.1103e-02 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=2.3466e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=7.8632e-02 | t=0.0087s
    tv | MR=0.1 | seed=1 | MAE=2.1163e-02 | t=0.2079s
    trss | MR=0.1 | seed=1 | MAE=3.0984e-02 | t=0.0198s

Completed: 2026-04-15T00:37:00.983627+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.