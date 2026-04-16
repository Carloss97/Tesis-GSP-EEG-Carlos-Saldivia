# Integration Log: it150_092
Started: 2026-04-15T00:39:00.586789+00:00
Description: Bulk normalized run it150_092 dataset=movielens_graph_signal graph=aew miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.0029s
    nearest | MR=0.1 | seed=0 | MAE=1.5567e-02 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=2.7103e-02 | t=0.0077s
    tv | MR=0.1 | seed=0 | MAE=1.7412e-02 | t=0.1867s
    trss | MR=0.1 | seed=0 | MAE=2.0577e-02 | t=0.0211s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=8.3893e-02 | t=0.0097s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.1857e-01 | t=1.7182s
    mean | MR=0.1 | seed=1 | MAE=2.1103e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=2.3466e-02 | t=0.0033s
    tikhonov | MR=0.1 | seed=1 | MAE=3.4163e-02 | t=0.0078s
    tv | MR=0.1 | seed=1 | MAE=2.1512e-02 | t=0.1865s
    trss | MR=0.1 | seed=1 | MAE=2.8572e-02 | t=0.0196s

Completed: 2026-04-15T00:39:00.587550+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.