# Integration Log: scr_00632
Started: 2026-04-16T14:52:52.441891+00:00
Description: Screening scr_00632 ds=movielens_graph_signal graph=vknng miss=[0.3] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.0030s
    nearest | MR=0.3 | seed=0 | MAE=6.7099e-02 | t=0.0102s
    tikhonov | MR=0.3 | seed=0 | MAE=9.8071e-02 | t=0.0128s
    tv | MR=0.3 | seed=0 | MAE=6.3092e-02 | t=0.4238s
    trss | MR=0.3 | seed=0 | MAE=7.6179e-02 | t=0.3409s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.5356e-01 | t=0.0679s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5463e-01 | t=24.7479s
    mean | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=6.3035e-02 | t=0.0534s
    tikhonov | MR=0.3 | seed=1 | MAE=1.0006e-01 | t=0.0107s
    tv | MR=0.3 | seed=1 | MAE=6.5224e-02 | t=0.8211s
    trss | MR=0.3 | seed=1 | MAE=8.1023e-02 | t=0.4419s

Completed: 2026-04-16T14:52:52.442818+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.