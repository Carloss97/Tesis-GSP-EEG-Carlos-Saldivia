# Integration Log: scr_00614
Started: 2026-04-16T14:41:27.974473+00:00
Description: Screening scr_00614 ds=physionet_real graph=knng miss=[0.3] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knng built OK
    mean | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=8.1341e-06 | t=0.0108s
    tikhonov | MR=0.3 | seed=0 | MAE=8.1454e-06 | t=0.0115s
    tv | MR=0.3 | seed=0 | MAE=7.0900e-06 | t=0.8637s
    trss | MR=0.3 | seed=0 | MAE=3.7284e-06 | t=0.3299s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.3713e-05 | t=0.1110s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=3.2577e-05 | t=28.0846s
    mean | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=8.0659e-06 | t=0.0093s
    tikhonov | MR=0.3 | seed=1 | MAE=8.2373e-06 | t=0.0079s
    tv | MR=0.3 | seed=1 | MAE=7.2491e-06 | t=0.6607s
    trss | MR=0.3 | seed=1 | MAE=3.7837e-06 | t=0.1743s

Completed: 2026-04-16T14:41:27.975604+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.