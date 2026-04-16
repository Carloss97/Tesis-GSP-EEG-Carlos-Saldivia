# Integration Log: scr_01024
Started: 2026-04-16T12:58:03.043802+00:00
Description: Screening scr_01024 ds=bci_iv2a_real_s2 graph=gaussian miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.4090s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5387e-06 | t=0.0215s
    trss | MR=0.2 | seed=0 | MAE=3.6928e-07 | t=0.0637s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1729e-05 | t=2.2546s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.2232s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.5777e-06 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=3.8400e-07 | t=0.0211s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1742e-05 | t=13.4447s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.3021s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8591e-06 | t=0.0117s
    trss | MR=0.2 | seed=0 | MAE=4.0866e-07 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4146e-05 | t=7.0008s

Completed: 2026-04-16T12:58:03.044533+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.