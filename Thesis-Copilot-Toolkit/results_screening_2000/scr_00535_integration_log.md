# Integration Log: scr_00535
Started: 2026-04-16T14:05:45.460156+00:00
Description: Screening scr_00535 ds=iris_graph_signal graph=aew miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0014s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0014s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3169e-01 | t=0.0038s
    tv | MR=0.2 | seed=0 | MAE=1.0497e-01 | t=0.0968s
    trss | MR=0.2 | seed=0 | MAE=8.0596e-02 | t=0.0037s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2150e-01 | t=0.0037s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.6663e-01 | t=10.9083s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0014s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0014s
    tikhonov | MR=0.2 | seed=1 | MAE=1.4471e-01 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=1.2292e-01 | t=0.1025s
    trss | MR=0.2 | seed=1 | MAE=9.4878e-02 | t=0.0040s

Completed: 2026-04-16T14:05:45.461000+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.