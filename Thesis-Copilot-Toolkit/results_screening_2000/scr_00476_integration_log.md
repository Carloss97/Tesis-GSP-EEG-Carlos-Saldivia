# Integration Log: scr_00476
Started: 2026-04-16T13:44:22.204644+00:00
Description: Screening scr_00476 ds=movielens_graph_signal graph=gaussian miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.0074s
    nearest | MR=0.2 | seed=0 | MAE=4.5789e-02 | t=0.0089s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2437e-01 | t=0.0095s
    tv | MR=0.2 | seed=0 | MAE=4.4103e-02 | t=0.5398s
    trss | MR=0.2 | seed=0 | MAE=5.3450e-02 | t=0.3755s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7811e-01 | t=0.0746s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5732e-01 | t=14.9666s
    mean | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.0033s
    nearest | MR=0.2 | seed=1 | MAE=4.0779e-02 | t=0.0081s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2583e-01 | t=0.0087s
    tv | MR=0.2 | seed=1 | MAE=4.2783e-02 | t=0.3831s
    trss | MR=0.2 | seed=1 | MAE=5.6188e-02 | t=0.4814s

Completed: 2026-04-16T13:44:22.205758+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.