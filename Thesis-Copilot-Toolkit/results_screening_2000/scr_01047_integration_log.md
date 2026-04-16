# Integration Log: scr_01047
Started: 2026-04-16T13:06:24.597878+00:00
Description: Screening scr_01047 ds=bci_iv2a_real_s1 graph=knng miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=3.0351e-06 | t=0.1632s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.5777e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=7.7974e-07 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.8196e-06 | t=4.3608s
    tv | MR=0.2 | seed=1 | MAE=3.3729e-06 | t=0.3803s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.8324e-06 | t=0.0133s
    trss | MR=0.2 | seed=1 | MAE=9.4006e-07 | t=0.1447s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.9894e-06 | t=4.4459s
    tv | MR=0.2 | seed=0 | MAE=3.0354e-06 | t=0.3134s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.8751e-06 | t=0.0189s
    trss | MR=0.2 | seed=0 | MAE=1.0319e-06 | t=0.1334s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1342e-05 | t=2.3898s

Completed: 2026-04-16T13:06:24.598660+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.