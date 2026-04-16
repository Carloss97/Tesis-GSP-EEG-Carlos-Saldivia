# Integration Log: scr_01010
Started: 2026-04-16T12:52:33.361553+00:00
Description: Screening scr_01010 ds=physionet_real graph=gaussian miss=3ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.1986s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5482e-05 | t=0.0085s
    trss | MR=0.2 | seed=0 | MAE=2.1605e-06 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7202e-05 | t=10.1389s
    tv | MR=0.2 | seed=1 | MAE=5.2167e-06 | t=0.3649s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5499e-05 | t=0.0087s
    trss | MR=0.2 | seed=1 | MAE=2.2244e-06 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7316e-05 | t=4.9107s
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.3650s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8356e-05 | t=0.0168s
    trss | MR=0.2 | seed=0 | MAE=2.3869e-06 | t=0.0211s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2305e-05 | t=2.0459s

Completed: 2026-04-16T12:52:33.362837+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.