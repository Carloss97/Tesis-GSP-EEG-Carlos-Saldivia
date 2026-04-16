# Integration Log: scr_00642
Started: 2026-04-16T14:57:37.166640+00:00
Description: Screening scr_00642 ds=iv100hz_mat graph=aew miss=[0.3] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: aew built OK
    mean | MR=0.3 | seed=0 | MAE=7.3919e+01 | t=0.0022s
    nearest | MR=0.3 | seed=0 | MAE=1.1253e+02 | t=0.0096s
    tikhonov | MR=0.3 | seed=0 | MAE=1.1885e+02 | t=0.0057s
    tv | MR=0.3 | seed=0 | MAE=5.7050e+01 | t=0.3421s
    trss | MR=0.3 | seed=0 | MAE=6.0395e+01 | t=0.3742s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.7332e+02 | t=0.0258s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.0531e+02 | t=20.2024s
    mean | MR=0.3 | seed=1 | MAE=7.2756e+01 | t=0.0044s
    nearest | MR=0.3 | seed=1 | MAE=1.1224e+02 | t=0.0102s
    tikhonov | MR=0.3 | seed=1 | MAE=1.1893e+02 | t=0.1003s
    tv | MR=0.3 | seed=1 | MAE=6.1640e+01 | t=0.3557s
    trss | MR=0.3 | seed=1 | MAE=5.9912e+01 | t=0.0350s

Completed: 2026-04-16T14:57:37.167517+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.