# Integration Log: scr_01052
Started: 2026-04-16T13:09:35.893816+00:00
Description: Screening scr_01052 ds=movielens_graph_signal graph=knng miss=3ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=4.3438e-02 | t=0.3483s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.8185e-02 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=7.7680e-02 | t=0.1758s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1704e-01 | t=9.1861s
    tv | MR=0.2 | seed=1 | MAE=4.3170e-02 | t=0.1422s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3908e-02 | t=0.0084s
    trss | MR=0.2 | seed=1 | MAE=8.2977e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2145e-01 | t=4.5408s
    tv | MR=0.2 | seed=0 | MAE=4.3742e-02 | t=0.3627s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0172e-01 | t=0.0178s
    trss | MR=0.2 | seed=0 | MAE=7.3134e-02 | t=0.2613s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2433e-01 | t=4.5239s

Completed: 2026-04-16T13:09:35.894733+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.