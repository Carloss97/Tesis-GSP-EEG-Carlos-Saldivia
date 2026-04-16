# Integration Log: scr_00631
Started: 2026-04-16T14:51:57.001104+00:00
Description: Screening scr_00631 ds=iris_graph_signal graph=vknng miss=[0.3] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=0.3 | seed=0 | MAE=2.7644e-01 | t=0.0016s
    nearest | MR=0.3 | seed=0 | MAE=3.5475e-01 | t=0.0020s
    tikhonov | MR=0.3 | seed=0 | MAE=3.6513e-01 | t=0.0035s
    tv | MR=0.3 | seed=0 | MAE=2.7676e-01 | t=0.1252s
    trss | MR=0.3 | seed=0 | MAE=2.3848e-01 | t=0.0037s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=4.5934e-01 | t=0.0043s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=7.0364e-01 | t=16.8922s
    mean | MR=0.3 | seed=1 | MAE=2.5974e-01 | t=0.0019s
    nearest | MR=0.3 | seed=1 | MAE=3.7471e-01 | t=0.0020s
    tikhonov | MR=0.3 | seed=1 | MAE=3.6275e-01 | t=0.0035s
    tv | MR=0.3 | seed=1 | MAE=2.5927e-01 | t=0.2846s
    trss | MR=0.3 | seed=1 | MAE=2.1786e-01 | t=0.0038s

Completed: 2026-04-16T14:51:57.002416+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.