# Integration Log: scr_00902
Started: 2026-04-16T12:13:13.139059+00:00
Description: Screening scr_00902 ds=physionet_real graph=gaussian miss=2ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.1915s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5482e-05 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=2.1605e-06 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7202e-05 | t=5.1846s
    tv | MR=0.2 | seed=1 | MAE=5.2167e-06 | t=0.2408s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5499e-05 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=2.2244e-06 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7316e-05 | t=9.6550s
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.3732s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8356e-05 | t=0.0093s
    trss | MR=0.2 | seed=0 | MAE=2.3869e-06 | t=0.0205s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2305e-05 | t=3.4841s

Completed: 2026-04-16T12:13:13.139902+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.