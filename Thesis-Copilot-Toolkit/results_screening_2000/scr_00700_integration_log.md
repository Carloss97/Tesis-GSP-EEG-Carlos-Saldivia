# Integration Log: scr_00700
Started: 2026-04-16T15:29:05.025998+00:00
Description: Screening scr_00700 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.0033s
    nearest | MR=0.4 | seed=0 | MAE=1.7309e-06 | t=0.0189s
    tikhonov | MR=0.4 | seed=0 | MAE=3.4382e-06 | t=0.0142s
    tv | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=1.0118s
    trss | MR=0.4 | seed=0 | MAE=1.4569e-06 | t=0.4138s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=5.4208e-06 | t=0.0128s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.7600e-05 | t=29.2680s
    mean | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.0046s
    nearest | MR=0.4 | seed=1 | MAE=1.7485e-06 | t=0.0297s
    tikhonov | MR=0.4 | seed=1 | MAE=3.3985e-06 | t=0.0359s
    tv | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=1.0008s
    trss | MR=0.4 | seed=1 | MAE=1.4107e-06 | t=0.0772s

Completed: 2026-04-16T15:29:05.027225+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.