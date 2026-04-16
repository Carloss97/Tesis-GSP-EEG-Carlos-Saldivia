# Integration Log: scr_00740
Started: 2026-04-16T11:51:56.268807+00:00
Description: Screening scr_00740 ds=movielens_graph_signal graph=vknng miss=[0.4] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=0.4 | seed=0 | MAE=9.1473e-02 | t=0.0021s
    nearest | MR=0.4 | seed=0 | MAE=1.0507e-01 | t=0.0085s
    tikhonov | MR=0.4 | seed=0 | MAE=1.2119e-01 | t=0.0058s
    tv | MR=0.4 | seed=0 | MAE=9.1607e-02 | t=0.1456s
    trss | MR=0.4 | seed=0 | MAE=1.1495e-01 | t=0.0208s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.5740e-01 | t=0.0078s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5083e-01 | t=2.2014s
    mean | MR=0.4 | seed=1 | MAE=8.7528e-02 | t=0.0022s
    nearest | MR=0.4 | seed=1 | MAE=9.3427e-02 | t=0.0095s
    tikhonov | MR=0.4 | seed=1 | MAE=1.1776e-01 | t=0.0091s
    tv | MR=0.4 | seed=1 | MAE=8.7507e-02 | t=0.1580s
    trss | MR=0.4 | seed=1 | MAE=1.0732e-01 | t=0.0199s

Completed: 2026-04-16T11:51:56.269560+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.