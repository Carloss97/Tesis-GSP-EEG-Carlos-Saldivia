# Integration Log: scr_01122
Started: 2026-04-16T14:03:38.630732+00:00
Description: Screening scr_01122 ds=iv100hz_mat graph=gaussian miss=[0.1] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=3.3577e+01 | t=0.4757s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2011e+02 | t=0.0169s
    trss | MR=0.2 | seed=0 | MAE=1.2017e+01 | t=0.0774s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7972e+02 | t=11.7574s
    tv | MR=0.2 | seed=1 | MAE=3.3829e+01 | t=0.1967s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.2003e+02 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=1.2036e+01 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.7922e+02 | t=8.7969s
    tv | MR=0.2 | seed=0 | MAE=3.3547e+01 | t=0.6361s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5080e+02 | t=0.0356s
    trss | MR=0.2 | seed=0 | MAE=1.6656e+01 | t=0.1658s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0673e+02 | t=14.7599s

Completed: 2026-04-16T14:03:38.631536+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.