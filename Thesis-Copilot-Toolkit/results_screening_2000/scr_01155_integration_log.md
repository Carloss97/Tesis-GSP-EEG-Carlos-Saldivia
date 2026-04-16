# Integration Log: scr_01155
Started: 2026-04-16T14:37:24.273358+00:00
Description: Screening scr_01155 ds=bci_iv2a_real_s1 graph=knng miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=3.0351e-06 | t=0.1654s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.5777e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=7.7974e-07 | t=0.0228s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.8196e-06 | t=26.2515s
    tv | MR=0.2 | seed=1 | MAE=3.3729e-06 | t=0.6816s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.8324e-06 | t=0.0261s
    trss | MR=0.2 | seed=1 | MAE=9.4006e-07 | t=0.5119s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.9894e-06 | t=6.0563s
    tv | MR=0.2 | seed=0 | MAE=3.0354e-06 | t=0.8937s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.8751e-06 | t=0.0778s
    trss | MR=0.2 | seed=0 | MAE=1.0319e-06 | t=0.4635s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1342e-05 | t=21.1534s

Completed: 2026-04-16T14:37:24.274503+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.