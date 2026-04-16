# Integration Log: scr_00482
Started: 2026-04-16T13:45:03.350410+00:00
Description: Screening scr_00482 ds=physionet_real graph=gaussian miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=5.7680e-06 | t=0.0050s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8115e-05 | t=0.0061s
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.2093s
    trss | MR=0.2 | seed=0 | MAE=3.8972e-06 | t=0.0194s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2249e-05 | t=0.0301s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.9178e-05 | t=15.9542s
    mean | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=5.8832e-06 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8111e-05 | t=0.0060s
    tv | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.2998s
    trss | MR=0.2 | seed=1 | MAE=3.9395e-06 | t=0.1238s

Completed: 2026-04-16T13:45:03.352265+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.