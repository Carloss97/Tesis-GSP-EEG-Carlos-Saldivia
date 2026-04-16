# Integration Log: scr_00506
Started: 2026-04-16T13:53:26.743652+00:00
Description: Screening scr_00506 ds=physionet_real graph=knng miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.0037s
    nearest | MR=0.2 | seed=0 | MAE=5.7680e-06 | t=0.0079s
    tikhonov | MR=0.2 | seed=0 | MAE=7.1307e-06 | t=0.0215s
    tv | MR=0.2 | seed=0 | MAE=5.1643e-06 | t=0.2261s
    trss | MR=0.2 | seed=0 | MAE=2.5858e-06 | t=0.0178s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3061e-05 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.1539e-05 | t=16.7381s
    mean | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.0027s
    nearest | MR=0.2 | seed=1 | MAE=5.8832e-06 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=7.0581e-06 | t=0.0060s
    tv | MR=0.2 | seed=1 | MAE=5.1750e-06 | t=0.1608s
    trss | MR=0.2 | seed=1 | MAE=2.5065e-06 | t=0.0182s

Completed: 2026-04-16T13:53:26.744649+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.