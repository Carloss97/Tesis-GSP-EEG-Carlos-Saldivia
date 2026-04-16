# Integration Log: scr_00344
Started: 2026-04-16T13:06:04.466093+00:00
Description: Screening scr_00344 ds=movielens_graph_signal graph=knn miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0027s
    tikhonov | MR=0.1 | seed=0 | MAE=7.9187e-02 | t=0.0058s
    tv | MR=0.1 | seed=0 | MAE=1.4587e-02 | t=0.1437s
    trss | MR=0.1 | seed=0 | MAE=2.0427e-02 | t=0.1244s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.5502e-01 | t=0.0126s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4780e-01 | t=4.4879s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0070s
    tikhonov | MR=0.1 | seed=1 | MAE=8.1472e-02 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=1.9081e-02 | t=0.1513s
    trss | MR=0.1 | seed=1 | MAE=2.6570e-02 | t=0.0970s

Completed: 2026-04-16T13:06:04.466958+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.