# Integration Log: scr_00518
Started: 2026-04-16T13:57:48.662149+00:00
Description: Screening scr_00518 ds=physionet_real graph=vknng miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.0038s
    nearest | MR=0.2 | seed=0 | MAE=5.7680e-06 | t=0.0102s
    tikhonov | MR=0.2 | seed=0 | MAE=7.0996e-06 | t=0.0114s
    tv | MR=0.2 | seed=0 | MAE=5.1584e-06 | t=0.3247s
    trss | MR=0.2 | seed=0 | MAE=2.6369e-06 | t=0.0182s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2911e-05 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.1188e-05 | t=25.3656s
    mean | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.0033s
    nearest | MR=0.2 | seed=1 | MAE=5.8832e-06 | t=0.0051s
    tikhonov | MR=0.2 | seed=1 | MAE=7.0195e-06 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=5.1689e-06 | t=0.1860s
    trss | MR=0.2 | seed=1 | MAE=2.5416e-06 | t=0.0172s

Completed: 2026-04-16T13:57:48.663048+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.