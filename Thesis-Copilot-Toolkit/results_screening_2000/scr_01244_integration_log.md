# Integration Log: scr_01244
Started: 2026-04-16T08:24:49.487265+00:00
Description: Screening scr_01244 ds=movielens_graph_signal graph=gaussian miss=[0.2] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6458e-02 | t=0.1919s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5439e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=6.2823e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2498e-01 | t=1.4312s
    tv | MR=0.2 | seed=1 | MAE=4.0251e-02 | t=0.1862s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.8231e-02 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=7.1373e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2338e-01 | t=1.4252s
    tv | MR=0.2 | seed=0 | MAE=3.6494e-02 | t=0.1845s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1585e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=5.9422e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3266e-01 | t=1.2500s

Completed: 2026-04-16T08:24:49.488078+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.