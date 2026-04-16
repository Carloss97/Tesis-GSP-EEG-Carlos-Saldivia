# Integration Log: scr_00590
Started: 2026-04-16T14:29:21.818510+00:00
Description: Screening scr_00590 ds=physionet_real graph=gaussian miss=[0.3] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.0030s
    nearest | MR=0.3 | seed=0 | MAE=8.1341e-06 | t=0.0102s
    tikhonov | MR=0.3 | seed=0 | MAE=1.8726e-05 | t=0.0237s
    tv | MR=0.3 | seed=0 | MAE=7.1408e-06 | t=0.5297s
    trss | MR=0.3 | seed=0 | MAE=5.5543e-06 | t=0.2194s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.2428e-05 | t=0.0141s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=3.9489e-05 | t=30.0138s
    mean | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=8.0659e-06 | t=0.0102s
    tikhonov | MR=0.3 | seed=1 | MAE=1.8767e-05 | t=0.0098s
    tv | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.5412s
    trss | MR=0.3 | seed=1 | MAE=5.5771e-06 | t=0.2774s

Completed: 2026-04-16T14:29:21.819346+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.