# Integration Log: scr_00916
Started: 2026-04-16T12:19:10.409249+00:00
Description: Screening scr_00916 ds=bci_iv2a_real_s2 graph=gaussian miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.3728s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5387e-06 | t=0.0155s
    trss | MR=0.2 | seed=0 | MAE=3.6928e-07 | t=0.4489s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1729e-05 | t=7.0636s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.3300s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.5777e-06 | t=0.0124s
    trss | MR=0.2 | seed=1 | MAE=3.8400e-07 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1742e-05 | t=2.1344s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.1883s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8591e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=4.0866e-07 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4146e-05 | t=7.9629s

Completed: 2026-04-16T12:19:10.410144+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.