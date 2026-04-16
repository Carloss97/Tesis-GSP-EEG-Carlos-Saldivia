# Integration Log: scr_01178
Started: 2026-04-16T15:05:12.419788+00:00
Description: Screening scr_01178 ds=physionet_real graph=aew miss=[0.1] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=5.0092e-06 | t=0.8557s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.9059e-06 | t=0.0125s
    trss | MR=0.2 | seed=0 | MAE=1.7894e-06 | t=0.7297s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5080e-05 | t=18.5050s
    tv | MR=0.2 | seed=1 | MAE=5.0179e-06 | t=0.6988s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.8204e-06 | t=0.0193s
    trss | MR=0.2 | seed=1 | MAE=1.8476e-06 | t=0.2220s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5186e-05 | t=21.6860s
    tv | MR=0.2 | seed=0 | MAE=5.1026e-06 | t=0.3236s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.0609e-06 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=1.8667e-06 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8390e-05 | t=24.7947s

Completed: 2026-04-16T15:05:12.421428+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.