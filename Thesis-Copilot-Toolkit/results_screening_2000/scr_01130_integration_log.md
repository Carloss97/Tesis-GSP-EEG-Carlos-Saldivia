# Integration Log: scr_01130
Started: 2026-04-16T14:07:17.031193+00:00
Description: Screening scr_01130 ds=physionet_real graph=gaussian miss=[0.1] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.7730s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5393e-05 | t=0.0145s
    trss | MR=0.2 | seed=0 | MAE=2.1567e-06 | t=0.1982s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7080e-05 | t=8.0135s
    tv | MR=0.2 | seed=1 | MAE=5.2167e-06 | t=0.3645s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5410e-05 | t=0.0448s
    trss | MR=0.2 | seed=1 | MAE=2.2202e-06 | t=0.0662s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7195e-05 | t=16.7979s
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.2297s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8283e-05 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=2.3815e-06 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2204e-05 | t=18.2227s

Completed: 2026-04-16T14:07:17.032062+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.