# Integration Log: scr_00435
Started: 2026-04-16T13:29:35.003683+00:00
Description: Screening scr_00435 ds=bci_iv2a_real_s1 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.0038s
    nearest | MR=0.2 | seed=0 | MAE=3.2140e-06 | t=0.0081s
    tikhonov | MR=0.2 | seed=0 | MAE=5.8742e-06 | t=0.0095s
    tv | MR=0.2 | seed=0 | MAE=3.0355e-06 | t=0.3046s
    trss | MR=0.2 | seed=0 | MAE=2.1621e-06 | t=0.1771s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0100e-05 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5066e-05 | t=17.3450s
    mean | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=3.5344e-06 | t=0.0051s
    tikhonov | MR=0.2 | seed=1 | MAE=6.0884e-06 | t=0.0061s
    tv | MR=0.2 | seed=1 | MAE=3.3731e-06 | t=0.1674s
    trss | MR=0.2 | seed=1 | MAE=2.4498e-06 | t=0.0187s

Completed: 2026-04-16T13:29:35.004421+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.