# Integration Log: scr_00750
Started: 2026-04-16T11:52:28.372936+00:00
Description: Screening scr_00750 ds=iv100hz_mat graph=aew miss=[0.4] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: aew built OK
    mean | MR=0.4 | seed=0 | MAE=1.0557e+02 | t=0.0021s
    nearest | MR=0.4 | seed=0 | MAE=1.5725e+02 | t=0.0084s
    tikhonov | MR=0.4 | seed=0 | MAE=1.4585e+02 | t=0.0057s
    tv | MR=0.4 | seed=0 | MAE=1.0744e+02 | t=0.1454s
    trss | MR=0.4 | seed=0 | MAE=9.3082e+01 | t=0.0196s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.8704e+02 | t=0.0082s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=2.1528e+02 | t=1.3120s
    mean | MR=0.4 | seed=1 | MAE=1.0515e+02 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=1.5788e+02 | t=0.0085s
    tikhonov | MR=0.4 | seed=1 | MAE=1.4676e+02 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=1.0208e+02 | t=0.1430s
    trss | MR=0.4 | seed=1 | MAE=9.2693e+01 | t=0.0216s

Completed: 2026-04-16T11:52:28.373756+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.