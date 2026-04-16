# Integration Log: scr_00794
Started: 2026-04-16T11:57:30.515812+00:00
Description: Screening scr_00794 ds=physionet_real graph=gaussian miss=1ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.2149s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5482e-05 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=2.1605e-06 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7202e-05 | t=2.5874s
    tv | MR=0.2 | seed=1 | MAE=5.2167e-06 | t=0.2078s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5499e-05 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=2.2244e-06 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7316e-05 | t=2.7214s
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.1883s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8356e-05 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=2.3869e-06 | t=0.0182s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2305e-05 | t=2.5027s

Completed: 2026-04-16T11:57:30.516688+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.