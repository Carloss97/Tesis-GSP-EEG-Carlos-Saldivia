# Integration Log: scr_00607
Started: 2026-04-16T14:39:28.753037+00:00
Description: Screening scr_00607 ds=iris_graph_signal graph=kalofolias miss=[0.3] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=0.3 | seed=0 | MAE=2.7644e-01 | t=0.0020s
    nearest | MR=0.3 | seed=0 | MAE=3.5475e-01 | t=0.0020s
    tikhonov | MR=0.3 | seed=0 | MAE=5.4251e-01 | t=0.0035s
    tv | MR=0.3 | seed=0 | MAE=2.7644e-01 | t=0.0906s
    trss | MR=0.3 | seed=0 | MAE=2.2746e-01 | t=0.0037s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=5.2995e-01 | t=0.0037s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=8.2605e-01 | t=5.0296s
    mean | MR=0.3 | seed=1 | MAE=2.5974e-01 | t=0.0022s
    nearest | MR=0.3 | seed=1 | MAE=3.7471e-01 | t=0.0020s
    tikhonov | MR=0.3 | seed=1 | MAE=5.6879e-01 | t=0.0039s
    tv | MR=0.3 | seed=1 | MAE=2.5974e-01 | t=0.3482s
    trss | MR=0.3 | seed=1 | MAE=2.0041e-01 | t=0.0699s

Completed: 2026-04-16T14:39:28.754597+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.