# Integration Log: scr_01071
Started: 2026-04-16T13:19:17.569730+00:00
Description: Screening scr_01071 ds=bci_iv2a_real_s1 graph=aew miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=3.0157e-06 | t=0.3330s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5242e-06 | t=0.0125s
    trss | MR=0.2 | seed=0 | MAE=1.0001e-06 | t=0.2824s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.1423e-06 | t=12.5457s
    tv | MR=0.2 | seed=1 | MAE=3.3563e-06 | t=0.1553s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.8527e-06 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=1.2712e-06 | t=0.0208s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.3257e-06 | t=15.6706s
    tv | MR=0.2 | seed=0 | MAE=3.0253e-06 | t=0.1585s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.2277e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.1914e-06 | t=0.0203s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0298e-05 | t=16.8521s

Completed: 2026-04-16T13:19:17.570518+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.