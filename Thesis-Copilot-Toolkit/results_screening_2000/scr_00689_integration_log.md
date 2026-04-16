# Integration Log: scr_00689
Started: 2026-04-16T15:23:11.980198+00:00
Description: Screening scr_00689 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.0038s
    nearest | MR=0.4 | seed=0 | MAE=1.3679e-06 | t=0.0147s
    tikhonov | MR=0.4 | seed=0 | MAE=2.8394e-06 | t=0.0102s
    tv | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.3448s
    trss | MR=0.4 | seed=0 | MAE=1.1908e-06 | t=0.0440s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=3.3264e-06 | t=0.0266s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=6.6659e-06 | t=18.6102s
    mean | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=1.3378e-06 | t=0.0244s
    tikhonov | MR=0.4 | seed=1 | MAE=2.8380e-06 | t=0.0099s
    tv | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.6070s
    trss | MR=0.4 | seed=1 | MAE=1.1893e-06 | t=0.0549s

Completed: 2026-04-16T15:23:11.981236+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.