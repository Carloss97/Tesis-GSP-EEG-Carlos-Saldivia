# Integration Log: scr_00332
Started: 2026-04-16T15:39:24.204920+00:00
Description: Screening scr_00332 ds=movielens_graph_signal graph=knn miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0176s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0251s
    tikhonov | MR=0.1 | seed=0 | MAE=6.0689e-02 | t=0.0405s
    tv | MR=0.1 | seed=0 | MAE=1.4582e-02 | t=0.7151s
    trss | MR=0.1 | seed=0 | MAE=1.8472e-02 | t=0.1925s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.3736e-01 | t=0.0379s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4103e-01 | t=19.9707s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0034s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0043s
    tikhonov | MR=0.1 | seed=1 | MAE=6.5891e-02 | t=0.1587s
    tv | MR=0.1 | seed=1 | MAE=1.9183e-02 | t=0.6508s
    trss | MR=0.1 | seed=1 | MAE=2.7762e-02 | t=0.2143s

Completed: 2026-04-16T15:39:24.205970+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.