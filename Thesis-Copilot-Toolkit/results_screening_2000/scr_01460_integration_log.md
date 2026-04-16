# Integration Log: scr_01460
Started: 2026-04-16T08:51:51.866208+00:00
Description: Screening scr_01460 ds=movielens_graph_signal graph=gaussian miss=[0.4] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6458e-02 | t=0.1876s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5439e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=6.2823e-02 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2498e-01 | t=1.2796s
    tv | MR=0.2 | seed=1 | MAE=4.0251e-02 | t=0.1861s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.8231e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=7.1373e-02 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2338e-01 | t=1.2870s
    tv | MR=0.2 | seed=0 | MAE=3.6494e-02 | t=0.1863s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1585e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=5.9422e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3266e-01 | t=1.3151s

Completed: 2026-04-16T08:51:51.867132+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.