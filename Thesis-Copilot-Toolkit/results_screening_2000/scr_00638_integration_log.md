# Integration Log: scr_00638
Started: 2026-04-16T14:53:45.432887+00:00
Description: Screening scr_00638 ds=physionet_real graph=aew miss=[0.3] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: aew built OK
    mean | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.0034s
    nearest | MR=0.3 | seed=0 | MAE=8.1341e-06 | t=0.0163s
    tikhonov | MR=0.3 | seed=0 | MAE=7.4553e-06 | t=0.1054s
    tv | MR=0.3 | seed=0 | MAE=7.0761e-06 | t=0.5093s
    trss | MR=0.3 | seed=0 | MAE=3.6631e-06 | t=0.5474s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.2692e-05 | t=0.0365s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=3.0857e-05 | t=24.0695s
    mean | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.0035s
    nearest | MR=0.3 | seed=1 | MAE=8.0659e-06 | t=0.0115s
    tikhonov | MR=0.3 | seed=1 | MAE=7.5296e-06 | t=0.0165s
    tv | MR=0.3 | seed=1 | MAE=7.2348e-06 | t=0.3082s
    trss | MR=0.3 | seed=1 | MAE=3.6961e-06 | t=0.1790s

Completed: 2026-04-16T14:53:45.433921+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.