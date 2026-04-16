# Integration Log: it150_056
Started: 2026-04-15T00:32:30.017841+00:00
Description: Bulk normalized run it150_056 dataset=movielens_graph_signal graph=kalofolias miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.0027s
    nearest | MR=0.1 | seed=0 | MAE=1.5567e-02 | t=0.0038s
    tikhonov | MR=0.1 | seed=0 | MAE=2.2263e-01 | t=0.0073s
    tv | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.2045s
    trss | MR=0.1 | seed=0 | MAE=3.2035e-02 | t=0.0192s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.1842e-01 | t=0.0095s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.8622e-01 | t=1.8839s
    mean | MR=0.1 | seed=1 | MAE=2.1103e-02 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=2.3466e-02 | t=0.0039s
    tikhonov | MR=0.1 | seed=1 | MAE=2.1683e-01 | t=0.0071s
    tv | MR=0.1 | seed=1 | MAE=2.1103e-02 | t=0.1950s
    trss | MR=0.1 | seed=1 | MAE=3.5028e-02 | t=0.0191s

Completed: 2026-04-15T00:32:30.019044+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.