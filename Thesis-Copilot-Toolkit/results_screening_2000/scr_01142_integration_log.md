# Integration Log: scr_01142
Started: 2026-04-16T14:19:17.510575+00:00
Description: Screening scr_01142 ds=physionet_real graph=kalofolias miss=[0.1] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: kalofolias built OK
    tv | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.6779s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0517e-05 | t=0.0814s
    trss | MR=0.2 | seed=0 | MAE=2.1597e-06 | t=0.6513s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8115e-05 | t=24.1650s
    tv | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.5360s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0543e-05 | t=0.0123s
    trss | MR=0.2 | seed=1 | MAE=2.2282e-06 | t=0.2299s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.8294e-05 | t=16.8591s
    tv | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.2290s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3206e-05 | t=0.0101s
    trss | MR=0.2 | seed=0 | MAE=2.3886e-06 | t=0.0297s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.3058e-05 | t=28.9107s

Completed: 2026-04-16T14:19:17.511469+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.