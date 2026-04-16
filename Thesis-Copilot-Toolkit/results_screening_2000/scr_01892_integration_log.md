# Integration Log: scr_01892
Started: 2026-04-16T09:52:05.963493+00:00
Description: Screening scr_01892 ds=movielens_graph_signal graph=gaussian miss=[0.1] mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6023e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=5.9909e-02 | t=0.2426s
    trss | MR=0.2 | seed=0 | MAE=6.8727e-02 | t=0.0219s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6738e-01 | t=0.0095s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4497e-01 | t=2.4297s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5992e-01 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=6.6499e-02 | t=0.1882s
    trss | MR=0.2 | seed=1 | MAE=7.5924e-02 | t=0.0207s

Completed: 2026-04-16T09:52:05.964357+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.