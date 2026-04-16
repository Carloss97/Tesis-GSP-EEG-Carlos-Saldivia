# Integration Log: scr_00680
Started: 2026-04-16T15:18:44.789304+00:00
Description: Screening scr_00680 ds=movielens_graph_signal graph=knn miss=[0.4] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.4 | seed=0 | MAE=9.1473e-02 | t=0.0033s
    nearest | MR=0.4 | seed=0 | MAE=1.0507e-01 | t=0.0148s
    tikhonov | MR=0.4 | seed=0 | MAE=1.3342e-01 | t=0.0317s
    tv | MR=0.4 | seed=0 | MAE=9.1512e-02 | t=0.4832s
    trss | MR=0.4 | seed=0 | MAE=1.1245e-01 | t=0.0477s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.6786e-01 | t=0.0153s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5509e-01 | t=23.5622s
    mean | MR=0.4 | seed=1 | MAE=8.7528e-02 | t=0.0032s
    nearest | MR=0.4 | seed=1 | MAE=9.3427e-02 | t=0.0457s
    tikhonov | MR=0.4 | seed=1 | MAE=1.3585e-01 | t=0.0292s
    tv | MR=0.4 | seed=1 | MAE=8.7526e-02 | t=0.5919s
    trss | MR=0.4 | seed=1 | MAE=1.0762e-01 | t=0.1225s

Completed: 2026-04-16T15:18:44.790163+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.