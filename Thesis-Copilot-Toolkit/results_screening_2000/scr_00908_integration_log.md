# Integration Log: scr_00908
Started: 2026-04-16T12:17:03.015179+00:00
Description: Screening scr_00908 ds=movielens_graph_signal graph=gaussian miss=2ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=4.4089e-02 | t=0.3078s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1401e-01 | t=0.0329s
    trss | MR=0.2 | seed=0 | MAE=7.5416e-02 | t=0.0384s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2054e-01 | t=2.8595s
    tv | MR=0.2 | seed=1 | MAE=4.2790e-02 | t=0.1956s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1568e-01 | t=0.0114s
    trss | MR=0.2 | seed=1 | MAE=8.1860e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2314e-01 | t=2.1877s
    tv | MR=0.2 | seed=0 | MAE=4.4098e-02 | t=0.3399s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3553e-01 | t=0.0129s
    trss | MR=0.2 | seed=0 | MAE=7.0991e-02 | t=0.0554s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3020e-01 | t=2.1820s

Completed: 2026-04-16T12:17:03.016043+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.