# Integration Log: scr_01022
Started: 2026-04-16T12:56:38.545840+00:00
Description: Screening scr_01022 ds=physionet_real graph=gaussian miss=3ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.2029s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5393e-05 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=2.1567e-06 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7080e-05 | t=6.7585s
    tv | MR=0.2 | seed=1 | MAE=5.2167e-06 | t=0.3811s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5410e-05 | t=0.0139s
    trss | MR=0.2 | seed=1 | MAE=2.2202e-06 | t=0.0908s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7195e-05 | t=4.5165s
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.3693s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8283e-05 | t=0.0152s
    trss | MR=0.2 | seed=0 | MAE=2.3815e-06 | t=0.1216s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2204e-05 | t=2.2149s

Completed: 2026-04-16T12:56:38.546760+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.