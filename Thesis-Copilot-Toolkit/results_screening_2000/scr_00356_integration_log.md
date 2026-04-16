# Integration Log: scr_00356
Started: 2026-04-16T13:08:01.960457+00:00
Description: Screening scr_00356 ds=movielens_graph_signal graph=knn miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0033s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0042s
    tikhonov | MR=0.1 | seed=0 | MAE=9.5868e-02 | t=0.0065s
    tv | MR=0.1 | seed=0 | MAE=1.4581e-02 | t=0.1516s
    trss | MR=0.1 | seed=0 | MAE=2.1503e-02 | t=0.0165s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.6674e-01 | t=0.0087s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.5122e-01 | t=9.7118s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=9.6293e-02 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=1.9060e-02 | t=0.1494s
    trss | MR=0.1 | seed=1 | MAE=2.6096e-02 | t=0.0160s

Completed: 2026-04-16T13:08:01.961353+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.