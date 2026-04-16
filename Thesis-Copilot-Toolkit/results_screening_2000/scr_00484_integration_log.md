# Integration Log: scr_00484
Started: 2026-04-16T13:46:13.191185+00:00
Description: Screening scr_00484 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=8.0037e-07 | t=0.0079s
    tikhonov | MR=0.2 | seed=0 | MAE=3.1100e-06 | t=0.0577s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.4498s
    trss | MR=0.2 | seed=0 | MAE=6.5818e-07 | t=0.1113s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.3384e-06 | t=0.0145s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7292e-05 | t=19.4791s
    mean | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=8.8678e-07 | t=0.0101s
    tikhonov | MR=0.2 | seed=1 | MAE=3.1091e-06 | t=0.0113s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.5681s
    trss | MR=0.2 | seed=1 | MAE=6.9089e-07 | t=0.2355s

Completed: 2026-04-16T13:46:13.192021+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.