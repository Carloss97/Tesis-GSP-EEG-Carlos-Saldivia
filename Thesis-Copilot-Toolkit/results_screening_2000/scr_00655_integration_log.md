# Integration Log: scr_00655
Started: 2026-04-16T15:04:15.953919+00:00
Description: Screening scr_00655 ds=iris_graph_signal graph=knn miss=[0.4] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.4 | seed=0 | MAE=2.7644e-01 | t=0.0015s
    nearest | MR=0.4 | seed=0 | MAE=3.5475e-01 | t=0.0021s
    tikhonov | MR=0.4 | seed=0 | MAE=3.7033e-01 | t=0.0351s
    tv | MR=0.4 | seed=0 | MAE=2.7751e-01 | t=0.2370s
    trss | MR=0.4 | seed=0 | MAE=2.5786e-01 | t=0.0038s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=4.5695e-01 | t=0.0038s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=6.6315e-01 | t=3.6572s
    mean | MR=0.4 | seed=1 | MAE=2.5974e-01 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=3.7471e-01 | t=0.0021s
    tikhonov | MR=0.4 | seed=1 | MAE=3.7736e-01 | t=0.0046s
    tv | MR=0.4 | seed=1 | MAE=2.6133e-01 | t=0.1028s
    trss | MR=0.4 | seed=1 | MAE=2.4933e-01 | t=0.0043s

Completed: 2026-04-16T15:04:15.954934+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.