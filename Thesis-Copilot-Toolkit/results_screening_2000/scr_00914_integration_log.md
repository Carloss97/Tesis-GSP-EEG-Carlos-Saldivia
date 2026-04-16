# Integration Log: scr_00914
Started: 2026-04-16T12:17:50.603195+00:00
Description: Screening scr_00914 ds=physionet_real graph=gaussian miss=2ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.2238s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5393e-05 | t=0.0088s
    trss | MR=0.2 | seed=0 | MAE=2.1567e-06 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7080e-05 | t=5.3312s
    tv | MR=0.2 | seed=1 | MAE=5.2167e-06 | t=0.4196s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5410e-05 | t=0.0129s
    trss | MR=0.2 | seed=1 | MAE=2.2202e-06 | t=0.0863s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7195e-05 | t=3.1481s
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.4229s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8283e-05 | t=0.0208s
    trss | MR=0.2 | seed=0 | MAE=2.3815e-06 | t=0.0900s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2204e-05 | t=2.6184s

Completed: 2026-04-16T12:17:50.603927+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.