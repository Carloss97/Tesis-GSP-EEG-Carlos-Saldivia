# Integration Log: scr_00734
Started: 2026-04-16T11:51:23.690801+00:00
Description: Screening scr_00734 ds=physionet_real graph=vknng miss=[0.4] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: vknng built OK
    mean | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.0020s
    nearest | MR=0.4 | seed=0 | MAE=1.1571e-05 | t=0.0084s
    tikhonov | MR=0.4 | seed=0 | MAE=1.0100e-05 | t=0.0057s
    tv | MR=0.4 | seed=0 | MAE=1.0429e-05 | t=0.1509s
    trss | MR=0.4 | seed=0 | MAE=5.9979e-06 | t=0.0207s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.4878e-05 | t=0.0079s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=3.3816e-05 | t=2.7107s
    mean | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.0021s
    nearest | MR=0.4 | seed=1 | MAE=1.1385e-05 | t=0.0085s
    tikhonov | MR=0.4 | seed=1 | MAE=9.9775e-06 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=1.0397e-05 | t=0.1454s
    trss | MR=0.4 | seed=1 | MAE=5.7911e-06 | t=0.0199s

Completed: 2026-04-16T11:51:23.691618+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.