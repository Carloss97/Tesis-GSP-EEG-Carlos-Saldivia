# Integration Log: scr_00643
Started: 2026-04-16T14:58:02.547163+00:00
Description: Screening scr_00643 ds=iris_graph_signal graph=aew miss=[0.3] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=0.3 | seed=0 | MAE=2.7644e-01 | t=0.0017s
    nearest | MR=0.3 | seed=0 | MAE=3.5475e-01 | t=0.0020s
    tikhonov | MR=0.3 | seed=0 | MAE=2.6057e-01 | t=0.0035s
    tv | MR=0.3 | seed=0 | MAE=2.5582e-01 | t=0.2752s
    trss | MR=0.3 | seed=0 | MAE=1.9668e-01 | t=0.0037s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=3.1975e-01 | t=0.0038s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.3908e-01 | t=4.9921s
    mean | MR=0.3 | seed=1 | MAE=2.5974e-01 | t=0.0017s
    nearest | MR=0.3 | seed=1 | MAE=3.7471e-01 | t=0.0023s
    tikhonov | MR=0.3 | seed=1 | MAE=2.3524e-01 | t=0.0139s
    tv | MR=0.3 | seed=1 | MAE=2.3899e-01 | t=0.3296s
    trss | MR=0.3 | seed=1 | MAE=1.7823e-01 | t=0.0038s

Completed: 2026-04-16T14:58:02.548026+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.