# Integration Log: scr_01184
Started: 2026-04-16T15:19:40.377783+00:00
Description: Screening scr_01184 ds=movielens_graph_signal graph=aew miss=[0.1] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=4.1743e-02 | t=0.4512s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.1897e-02 | t=0.0444s
    trss | MR=0.2 | seed=0 | MAE=5.3236e-02 | t=0.0697s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0817e-01 | t=31.1738s
    tv | MR=0.2 | seed=1 | MAE=4.4378e-02 | t=0.4222s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=7.7433e-02 | t=0.0533s
    trss | MR=0.2 | seed=1 | MAE=5.4342e-02 | t=0.4559s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1400e-01 | t=36.3877s
    tv | MR=0.2 | seed=0 | MAE=4.2416e-02 | t=0.3541s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.4854e-02 | t=0.0180s
    trss | MR=0.2 | seed=0 | MAE=5.2845e-02 | t=0.1134s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0980e-01 | t=21.5725s

Completed: 2026-04-16T15:19:40.378648+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.