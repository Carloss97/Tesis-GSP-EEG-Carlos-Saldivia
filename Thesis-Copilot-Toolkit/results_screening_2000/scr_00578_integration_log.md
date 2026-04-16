# Integration Log: scr_00578
Started: 2026-04-16T14:23:48.221354+00:00
Description: Screening scr_00578 ds=physionet_real graph=gaussian miss=[0.3] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.0042s
    nearest | MR=0.3 | seed=0 | MAE=8.1341e-06 | t=0.0416s
    tikhonov | MR=0.3 | seed=0 | MAE=1.8794e-05 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.3328s
    trss | MR=0.3 | seed=0 | MAE=5.5699e-06 | t=0.1167s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.2451e-05 | t=0.0163s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=3.9520e-05 | t=25.9312s
    mean | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=8.0659e-06 | t=0.0113s
    tikhonov | MR=0.3 | seed=1 | MAE=1.8835e-05 | t=0.0425s
    tv | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.8245s
    trss | MR=0.3 | seed=1 | MAE=5.5930e-06 | t=0.6178s

Completed: 2026-04-16T14:23:48.222766+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.