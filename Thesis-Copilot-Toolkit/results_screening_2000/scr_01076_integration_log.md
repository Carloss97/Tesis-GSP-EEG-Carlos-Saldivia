# Integration Log: scr_01076
Started: 2026-04-16T13:26:22.986880+00:00
Description: Screening scr_01076 ds=movielens_graph_signal graph=aew miss=3ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=4.1743e-02 | t=0.3930s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.1897e-02 | t=0.0128s
    trss | MR=0.2 | seed=0 | MAE=5.3236e-02 | t=0.1074s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0817e-01 | t=15.6932s
    tv | MR=0.2 | seed=1 | MAE=4.4378e-02 | t=0.4048s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=7.7433e-02 | t=0.0161s
    trss | MR=0.2 | seed=1 | MAE=5.4342e-02 | t=0.4795s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1400e-01 | t=20.2516s
    tv | MR=0.2 | seed=0 | MAE=4.2416e-02 | t=0.3560s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.4854e-02 | t=0.0192s
    trss | MR=0.2 | seed=0 | MAE=5.2845e-02 | t=0.0702s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0980e-01 | t=3.1539s

Completed: 2026-04-16T13:26:22.988324+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.