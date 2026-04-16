# Integration Log: scr_00656
Started: 2026-04-16T15:05:07.309280+00:00
Description: Screening scr_00656 ds=movielens_graph_signal graph=knn miss=[0.4] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.4 | seed=0 | MAE=9.1473e-02 | t=0.0611s
    nearest | MR=0.4 | seed=0 | MAE=1.0507e-01 | t=0.0413s
    tikhonov | MR=0.4 | seed=0 | MAE=1.1869e-01 | t=0.0096s
    tv | MR=0.4 | seed=0 | MAE=9.1767e-02 | t=0.6608s
    trss | MR=0.4 | seed=0 | MAE=1.1551e-01 | t=0.6535s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.5414e-01 | t=0.0122s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.4994e-01 | t=9.8970s
    mean | MR=0.4 | seed=1 | MAE=8.7528e-02 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=9.3427e-02 | t=0.0467s
    tikhonov | MR=0.4 | seed=1 | MAE=1.1777e-01 | t=0.0134s
    tv | MR=0.4 | seed=1 | MAE=8.7554e-02 | t=0.6796s
    trss | MR=0.4 | seed=1 | MAE=1.1085e-01 | t=0.9045s

Completed: 2026-04-16T15:05:07.310297+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.