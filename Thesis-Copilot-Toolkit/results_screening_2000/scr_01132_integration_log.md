# Integration Log: scr_01132
Started: 2026-04-16T14:10:14.688105+00:00
Description: Screening scr_01132 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.6502s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5387e-06 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=3.6928e-07 | t=0.1861s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1729e-05 | t=15.7447s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.1872s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.5777e-06 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=3.8400e-07 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1742e-05 | t=2.6346s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.2075s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8591e-06 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=4.0866e-07 | t=0.3411s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4146e-05 | t=17.2136s

Completed: 2026-04-16T14:10:14.689527+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.