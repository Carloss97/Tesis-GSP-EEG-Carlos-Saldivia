# Integration Log: scr_00472
Started: 2026-04-16T13:42:08.301171+00:00
Description: Screening scr_00472 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=8.0037e-07 | t=0.0054s
    tikhonov | MR=0.2 | seed=0 | MAE=3.1100e-06 | t=0.0059s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.5710s
    trss | MR=0.2 | seed=0 | MAE=6.5818e-07 | t=0.6697s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.3384e-06 | t=0.0124s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7292e-05 | t=13.6522s
    mean | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=8.8678e-07 | t=0.0069s
    tikhonov | MR=0.2 | seed=1 | MAE=3.1091e-06 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.1932s
    trss | MR=0.2 | seed=1 | MAE=6.9089e-07 | t=0.0183s

Completed: 2026-04-16T13:42:08.302017+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.