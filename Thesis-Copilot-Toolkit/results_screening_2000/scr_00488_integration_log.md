# Integration Log: scr_00488
Started: 2026-04-16T13:48:28.001557+00:00
Description: Screening scr_00488 ds=movielens_graph_signal graph=gaussian miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=4.5789e-02 | t=0.0406s
    tikhonov | MR=0.2 | seed=0 | MAE=9.4757e-02 | t=0.0086s
    tv | MR=0.2 | seed=0 | MAE=4.4070e-02 | t=0.6931s
    trss | MR=0.2 | seed=0 | MAE=5.2846e-02 | t=0.3197s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5967e-01 | t=0.0467s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4815e-01 | t=17.0714s
    mean | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=4.0779e-02 | t=0.0086s
    tikhonov | MR=0.2 | seed=1 | MAE=9.8879e-02 | t=0.0116s
    tv | MR=0.2 | seed=1 | MAE=4.2801e-02 | t=0.3308s
    trss | MR=0.2 | seed=1 | MAE=5.7976e-02 | t=0.7625s

Completed: 2026-04-16T13:48:28.002455+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.