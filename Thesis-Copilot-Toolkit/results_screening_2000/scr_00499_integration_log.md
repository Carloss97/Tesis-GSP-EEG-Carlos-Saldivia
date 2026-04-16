# Integration Log: scr_00499
Started: 2026-04-16T13:51:53.962337+00:00
Description: Screening scr_00499 ds=iris_graph_signal graph=kalofolias miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0014s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0014s
    tikhonov | MR=0.2 | seed=0 | MAE=5.3900e-01 | t=0.0034s
    tv | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.1768s
    trss | MR=0.2 | seed=0 | MAE=9.3339e-02 | t=0.0037s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.3343e-01 | t=0.0038s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.2372e-01 | t=7.3886s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0345s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0014s
    tikhonov | MR=0.2 | seed=1 | MAE=5.3246e-01 | t=0.0034s
    tv | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.2280s
    trss | MR=0.2 | seed=1 | MAE=1.0295e-01 | t=0.0076s

Completed: 2026-04-16T13:51:53.963319+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.