# Integration Log: scr_01124
Started: 2026-04-16T14:05:48.773944+00:00
Description: Screening scr_01124 ds=movielens_graph_signal graph=gaussian miss=[0.1] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=4.4089e-02 | t=0.6647s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1401e-01 | t=0.0138s
    trss | MR=0.2 | seed=0 | MAE=7.5416e-02 | t=0.0877s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2054e-01 | t=8.2269s
    tv | MR=0.2 | seed=1 | MAE=4.2790e-02 | t=0.1967s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1568e-01 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=8.1860e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2314e-01 | t=21.7320s
    tv | MR=0.2 | seed=0 | MAE=4.4098e-02 | t=0.2222s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3553e-01 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=7.0991e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3020e-01 | t=18.3658s

Completed: 2026-04-16T14:05:48.774642+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.