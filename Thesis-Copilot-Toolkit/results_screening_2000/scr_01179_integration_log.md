# Integration Log: scr_01179
Started: 2026-04-16T15:07:38.587788+00:00
Description: Screening scr_01179 ds=bci_iv2a_real_s1 graph=aew miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=3.0157e-06 | t=0.5824s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5242e-06 | t=0.0687s
    trss | MR=0.2 | seed=0 | MAE=1.0001e-06 | t=0.1859s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.1423e-06 | t=16.7360s
    tv | MR=0.2 | seed=1 | MAE=3.3563e-06 | t=0.5599s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.8527e-06 | t=0.0125s
    trss | MR=0.2 | seed=1 | MAE=1.2712e-06 | t=0.1192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.3257e-06 | t=29.4276s
    tv | MR=0.2 | seed=0 | MAE=3.0253e-06 | t=0.1611s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.2277e-06 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=1.1914e-06 | t=0.0206s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0298e-05 | t=10.7979s

Completed: 2026-04-16T15:07:38.588786+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.