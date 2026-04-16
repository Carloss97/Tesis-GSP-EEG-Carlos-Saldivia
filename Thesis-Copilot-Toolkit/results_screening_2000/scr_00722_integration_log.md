# Integration Log: scr_00722
Started: 2026-04-16T15:40:03.170759+00:00
Description: Screening scr_00722 ds=physionet_real graph=knng miss=[0.4] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knng built OK
    mean | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.0036s
    nearest | MR=0.4 | seed=0 | MAE=1.1571e-05 | t=0.0331s
    tikhonov | MR=0.4 | seed=0 | MAE=1.0084e-05 | t=0.0298s
    tv | MR=0.4 | seed=0 | MAE=1.0437e-05 | t=0.5793s
    trss | MR=0.4 | seed=0 | MAE=5.9114e-06 | t=0.1431s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.5029e-05 | t=0.0608s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=3.4109e-05 | t=30.5098s
    mean | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.0045s
    nearest | MR=0.4 | seed=1 | MAE=1.1385e-05 | t=0.0248s
    tikhonov | MR=0.4 | seed=1 | MAE=9.9784e-06 | t=0.0202s
    tv | MR=0.4 | seed=1 | MAE=1.0406e-05 | t=0.5722s
    trss | MR=0.4 | seed=1 | MAE=5.7041e-06 | t=0.0521s

Completed: 2026-04-16T15:40:03.171638+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.