# Integration Log: scr_00728
Started: 2026-04-16T11:51:16.425666+00:00
Description: Screening scr_00728 ds=movielens_graph_signal graph=knng miss=[0.4] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=0.4 | seed=0 | MAE=9.1473e-02 | t=0.0021s
    nearest | MR=0.4 | seed=0 | MAE=1.0507e-01 | t=0.0181s
    tikhonov | MR=0.4 | seed=0 | MAE=1.1985e-01 | t=0.0058s
    tv | MR=0.4 | seed=0 | MAE=9.1624e-02 | t=0.1421s
    trss | MR=0.4 | seed=0 | MAE=1.1489e-01 | t=0.0199s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.5610e-01 | t=0.0138s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5022e-01 | t=2.4490s
    mean | MR=0.4 | seed=1 | MAE=8.7528e-02 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=9.3427e-02 | t=0.0088s
    tikhonov | MR=0.4 | seed=1 | MAE=1.1608e-01 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=8.7506e-02 | t=0.1439s
    trss | MR=0.4 | seed=1 | MAE=1.0750e-01 | t=0.0210s

Completed: 2026-04-16T11:51:16.426349+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.