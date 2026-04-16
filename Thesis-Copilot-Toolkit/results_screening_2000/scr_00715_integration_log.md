# Integration Log: scr_00715
Started: 2026-04-16T15:37:49.446983+00:00
Description: Screening scr_00715 ds=iris_graph_signal graph=kalofolias miss=[0.4] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=0.4 | seed=0 | MAE=2.7644e-01 | t=0.0031s
    nearest | MR=0.4 | seed=0 | MAE=3.5475e-01 | t=0.0024s
    tikhonov | MR=0.4 | seed=0 | MAE=5.4251e-01 | t=0.0048s
    tv | MR=0.4 | seed=0 | MAE=2.7644e-01 | t=0.1034s
    trss | MR=0.4 | seed=0 | MAE=2.2746e-01 | t=0.0051s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=5.2995e-01 | t=0.0066s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=8.2605e-01 | t=3.9771s
    mean | MR=0.4 | seed=1 | MAE=2.5974e-01 | t=0.0014s
    nearest | MR=0.4 | seed=1 | MAE=3.7471e-01 | t=0.0018s
    tikhonov | MR=0.4 | seed=1 | MAE=5.6879e-01 | t=0.0036s
    tv | MR=0.4 | seed=1 | MAE=2.5974e-01 | t=0.1935s
    trss | MR=0.4 | seed=1 | MAE=2.0041e-01 | t=0.0261s

Completed: 2026-04-16T15:37:49.448195+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.