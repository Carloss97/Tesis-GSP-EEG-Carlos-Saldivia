# Integration Log: scr_00512
Started: 2026-04-16T13:57:04.037324+00:00
Description: Screening scr_00512 ds=movielens_graph_signal graph=knng miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=4.5789e-02 | t=0.0078s
    tikhonov | MR=0.2 | seed=0 | MAE=8.1140e-02 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=4.3916e-02 | t=0.4202s
    trss | MR=0.2 | seed=0 | MAE=5.3505e-02 | t=0.5755s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4545e-01 | t=0.0832s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4810e-01 | t=12.7942s
    mean | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.0023s
    nearest | MR=0.2 | seed=1 | MAE=4.0779e-02 | t=0.0054s
    tikhonov | MR=0.2 | seed=1 | MAE=8.6786e-02 | t=0.0116s
    tv | MR=0.2 | seed=1 | MAE=4.2889e-02 | t=0.1452s
    trss | MR=0.2 | seed=1 | MAE=5.8609e-02 | t=0.0191s

Completed: 2026-04-16T13:57:04.038021+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.