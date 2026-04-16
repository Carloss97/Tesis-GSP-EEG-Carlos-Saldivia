# Integration Log: scr_01496
Started: 2026-04-16T08:56:19.997223+00:00
Description: Screening scr_01496 ds=movielens_graph_signal graph=vknng miss=[0.4] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=3.6198e-02 | t=0.1435s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.7391e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=6.2012e-02 | t=0.0201s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2582e-01 | t=1.3092s
    tv | MR=0.2 | seed=1 | MAE=4.0343e-02 | t=0.1444s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3729e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=7.3845e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2500e-01 | t=1.3740s
    tv | MR=0.2 | seed=0 | MAE=3.6353e-02 | t=0.1456s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0518e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=5.8520e-02 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3379e-01 | t=1.3350s

Completed: 2026-04-16T08:56:19.998090+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.