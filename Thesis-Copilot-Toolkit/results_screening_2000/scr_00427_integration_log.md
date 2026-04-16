# Integration Log: scr_00427
Started: 2026-04-16T13:27:17.680366+00:00
Description: Screening scr_00427 ds=iris_graph_signal graph=aew miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0016s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0032s
    tikhonov | MR=0.1 | seed=0 | MAE=1.3169e-01 | t=0.0035s
    tv | MR=0.1 | seed=0 | MAE=1.0497e-01 | t=0.1196s
    trss | MR=0.1 | seed=0 | MAE=8.0596e-02 | t=0.0038s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.2150e-01 | t=0.0045s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.6663e-01 | t=5.0944s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0014s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0014s
    tikhonov | MR=0.1 | seed=1 | MAE=1.4471e-01 | t=0.0040s
    tv | MR=0.1 | seed=1 | MAE=1.2292e-01 | t=0.0845s
    trss | MR=0.1 | seed=1 | MAE=9.4878e-02 | t=0.0052s

Completed: 2026-04-16T13:27:17.681246+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.