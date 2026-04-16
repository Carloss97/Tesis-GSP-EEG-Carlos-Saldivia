# Integration Log: scr_00595
Started: 2026-04-16T14:33:36.730143+00:00
Description: Screening scr_00595 ds=iris_graph_signal graph=gaussian miss=[0.3] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.3 | seed=0 | MAE=2.7644e-01 | t=0.0009s
    nearest | MR=0.3 | seed=0 | MAE=3.5475e-01 | t=0.0013s
    tikhonov | MR=0.3 | seed=0 | MAE=2.8845e-01 | t=0.0023s
    tv | MR=0.3 | seed=0 | MAE=2.7070e-01 | t=0.0529s
    trss | MR=0.3 | seed=0 | MAE=2.5538e-01 | t=0.0028s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=3.2490e-01 | t=0.0027s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=4.5295e-01 | t=8.0061s
    mean | MR=0.3 | seed=1 | MAE=2.5974e-01 | t=0.0014s
    nearest | MR=0.3 | seed=1 | MAE=3.7471e-01 | t=0.0020s
    tikhonov | MR=0.3 | seed=1 | MAE=2.8703e-01 | t=0.0045s
    tv | MR=0.3 | seed=1 | MAE=2.5923e-01 | t=0.2540s
    trss | MR=0.3 | seed=1 | MAE=2.4612e-01 | t=0.0038s

Completed: 2026-04-16T14:33:36.731000+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.