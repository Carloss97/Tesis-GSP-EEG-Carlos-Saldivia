# Integration Log: it150_044
Started: 2026-04-15T00:30:15.643406+00:00
Description: Bulk normalized run it150_044 dataset=movielens_graph_signal graph=gaussian miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.0024s
    nearest | MR=0.1 | seed=0 | MAE=1.5567e-02 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=8.7791e-02 | t=0.0068s
    tv | MR=0.1 | seed=0 | MAE=1.7327e-02 | t=0.2096s
    trss | MR=0.1 | seed=0 | MAE=2.3121e-02 | t=0.0191s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.6942e-01 | t=0.0107s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.5182e-01 | t=1.4959s
    mean | MR=0.1 | seed=1 | MAE=2.1103e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=2.3466e-02 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=8.9207e-02 | t=0.0068s
    tv | MR=0.1 | seed=1 | MAE=2.1118e-02 | t=0.2248s
    trss | MR=0.1 | seed=1 | MAE=2.8289e-02 | t=0.0179s

Completed: 2026-04-15T00:30:15.644457+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.