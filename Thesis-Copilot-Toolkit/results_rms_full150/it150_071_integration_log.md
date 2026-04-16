# Integration Log: it150_071
Started: 2026-04-15T00:51:25.956007+00:00
Description: Bulk normalized run it150_071 dataset=synthetic_broad graph=knng miss=[0.1] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=5.4881e-02 | t=0.0034s
    nearest | MR=0.1 | seed=0 | MAE=7.5105e-02 | t=0.0052s
    tikhonov | MR=0.1 | seed=0 | MAE=2.2243e-01 | t=0.0097s
    tv | MR=0.1 | seed=0 | MAE=5.6498e-02 | t=0.2211s
    trss | MR=0.1 | seed=0 | MAE=4.1928e-02 | t=0.0198s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.2635e-01 | t=0.0103s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.1933e-01 | t=5.4274s
    mean | MR=0.1 | seed=1 | MAE=5.4906e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=7.4297e-02 | t=0.0035s
    tikhonov | MR=0.1 | seed=1 | MAE=2.2230e-01 | t=0.0089s
    tv | MR=0.1 | seed=1 | MAE=5.6500e-02 | t=0.2191s
    trss | MR=0.1 | seed=1 | MAE=4.0723e-02 | t=0.0198s

Completed: 2026-04-15T00:51:25.957389+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.