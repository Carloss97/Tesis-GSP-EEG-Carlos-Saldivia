# Integration Log: scr_00530
Started: 2026-04-16T14:02:36.400101+00:00
Description: Screening scr_00530 ds=physionet_real graph=aew miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=5.7680e-06 | t=0.0483s
    tikhonov | MR=0.2 | seed=0 | MAE=6.3957e-06 | t=0.0105s
    tv | MR=0.2 | seed=0 | MAE=5.1529e-06 | t=0.6162s
    trss | MR=0.2 | seed=0 | MAE=2.5458e-06 | t=0.4628s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1988e-05 | t=0.0166s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9686e-05 | t=17.5757s
    mean | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=5.8832e-06 | t=0.0051s
    tikhonov | MR=0.2 | seed=1 | MAE=6.3175e-06 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=5.1633e-06 | t=0.1485s
    trss | MR=0.2 | seed=1 | MAE=2.4610e-06 | t=0.0203s

Completed: 2026-04-16T14:02:36.400995+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.