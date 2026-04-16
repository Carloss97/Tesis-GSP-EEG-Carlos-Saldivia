# Integration Log: scr_01148
Started: 2026-04-16T14:32:42.973584+00:00
Description: Screening scr_01148 ds=movielens_graph_signal graph=kalofolias miss=[0.1] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: kalofolias built OK
    tv | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.2013s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9956e-01 | t=0.0151s
    trss | MR=0.2 | seed=0 | MAE=9.5641e-02 | t=0.1418s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7808e-01 | t=26.0237s
    tv | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.7027s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.0111e-01 | t=0.0130s
    trss | MR=0.2 | seed=1 | MAE=1.0144e-01 | t=0.2684s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.8092e-01 | t=19.6617s
    tv | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.6080s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9956e-01 | t=0.0137s
    trss | MR=0.2 | seed=0 | MAE=9.0662e-02 | t=0.1137s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7808e-01 | t=24.5984s

Completed: 2026-04-16T14:32:42.974450+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.