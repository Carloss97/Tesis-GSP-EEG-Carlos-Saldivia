# Integration Log: scr_00376
Started: 2026-04-16T13:10:51.104211+00:00
Description: Screening scr_00376 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=2.9248e-06 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.2110s
    trss | MR=0.1 | seed=0 | MAE=2.3794e-07 | t=0.2820s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=5.2994e-06 | t=0.0123s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.7103e-05 | t=7.9773s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0029s
    tikhonov | MR=0.1 | seed=1 | MAE=2.9331e-06 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.2075s
    trss | MR=0.1 | seed=1 | MAE=2.5203e-07 | t=0.1703s

Completed: 2026-04-16T13:10:51.105610+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.