# Integration Log: scr_00547
Started: 2026-04-16T14:10:08.766231+00:00
Description: Screening scr_00547 ds=iris_graph_signal graph=knn miss=[0.3] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=2.7644e-01 | t=0.0014s
    nearest | MR=0.3 | seed=0 | MAE=3.5475e-01 | t=0.0568s
    tikhonov | MR=0.3 | seed=0 | MAE=3.7033e-01 | t=0.0078s
    tv | MR=0.3 | seed=0 | MAE=2.7751e-01 | t=0.1768s
    trss | MR=0.3 | seed=0 | MAE=2.5786e-01 | t=0.0042s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=4.5695e-01 | t=0.0048s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=6.6315e-01 | t=6.6416s
    mean | MR=0.3 | seed=1 | MAE=2.5974e-01 | t=0.0014s
    nearest | MR=0.3 | seed=1 | MAE=3.7471e-01 | t=0.0020s
    tikhonov | MR=0.3 | seed=1 | MAE=3.7736e-01 | t=0.0170s
    tv | MR=0.3 | seed=1 | MAE=2.6133e-01 | t=0.0674s
    trss | MR=0.3 | seed=1 | MAE=2.4933e-01 | t=0.0027s

Completed: 2026-04-16T14:10:08.766921+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.