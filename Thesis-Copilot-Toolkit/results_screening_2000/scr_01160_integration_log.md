# Integration Log: scr_01160
Started: 2026-04-16T14:47:53.470197+00:00
Description: Screening scr_01160 ds=movielens_graph_signal graph=knng miss=[0.1] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=4.3438e-02 | t=0.6949s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.8185e-02 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=7.7680e-02 | t=1.1326s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1704e-01 | t=14.0659s
    tv | MR=0.2 | seed=1 | MAE=4.3170e-02 | t=0.4002s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3908e-02 | t=0.0247s
    trss | MR=0.2 | seed=1 | MAE=8.2977e-02 | t=0.2837s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2145e-01 | t=25.6639s
    tv | MR=0.2 | seed=0 | MAE=4.3742e-02 | t=0.4033s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0172e-01 | t=0.0360s
    trss | MR=0.2 | seed=0 | MAE=7.3134e-02 | t=0.4812s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2433e-01 | t=24.5919s

Completed: 2026-04-16T14:47:53.471066+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.