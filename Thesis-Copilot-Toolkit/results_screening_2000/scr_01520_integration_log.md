# Integration Log: scr_01520
Started: 2026-04-16T08:59:29.724240+00:00
Description: Screening scr_01520 ds=movielens_graph_signal graph=knn miss=1ch mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3647e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=5.8767e-02 | t=0.1390s
    trss | MR=0.2 | seed=0 | MAE=7.4155e-02 | t=0.0196s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.4699e-01 | t=0.0083s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5487e-01 | t=1.3461s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=1.4270e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.5984e-02 | t=0.1414s
    trss | MR=0.2 | seed=1 | MAE=8.5039e-02 | t=0.0198s

Completed: 2026-04-16T08:59:29.725059+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.