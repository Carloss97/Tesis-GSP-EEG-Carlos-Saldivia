# Integration Log: scr_00746
Started: 2026-04-16T11:52:05.122006+00:00
Description: Screening scr_00746 ds=physionet_real graph=aew miss=[0.4] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: aew built OK
    mean | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.0022s
    nearest | MR=0.4 | seed=0 | MAE=1.1571e-05 | t=0.0085s
    tikhonov | MR=0.4 | seed=0 | MAE=9.4508e-06 | t=0.0058s
    tv | MR=0.4 | seed=0 | MAE=1.0421e-05 | t=0.1490s
    trss | MR=0.4 | seed=0 | MAE=5.8105e-06 | t=0.0204s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.4098e-05 | t=0.0080s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=3.2635e-05 | t=2.5542s
    mean | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=1.1385e-05 | t=0.0087s
    tikhonov | MR=0.4 | seed=1 | MAE=9.3246e-06 | t=0.0063s
    tv | MR=0.4 | seed=1 | MAE=1.0389e-05 | t=0.1532s
    trss | MR=0.4 | seed=1 | MAE=5.5967e-06 | t=0.0203s

Completed: 2026-04-16T11:52:05.122861+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.