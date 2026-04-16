# Integration Log: scr_00524
Started: 2026-04-16T14:02:00.022269+00:00
Description: Screening scr_00524 ds=movielens_graph_signal graph=vknng miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=4.5789e-02 | t=0.0415s
    tikhonov | MR=0.2 | seed=0 | MAE=8.3597e-02 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=4.3934e-02 | t=0.3872s
    trss | MR=0.2 | seed=0 | MAE=5.3411e-02 | t=0.7542s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4781e-01 | t=0.0162s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4916e-01 | t=15.1090s
    mean | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=4.0779e-02 | t=0.0051s
    tikhonov | MR=0.2 | seed=1 | MAE=8.9247e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=4.2878e-02 | t=0.2259s
    trss | MR=0.2 | seed=1 | MAE=5.8702e-02 | t=0.2148s

Completed: 2026-04-16T14:02:00.023388+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.