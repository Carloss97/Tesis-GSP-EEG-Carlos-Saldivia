# Integration Log: scr_01503
Started: 2026-04-16T08:56:50.010934+00:00
Description: Screening scr_01503 ds=bci_iv2a_real_s1 graph=aew miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=6.8677e-02 | t=0.1588s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2889e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=2.0066e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.3841e-01 | t=2.6293s
    tv | MR=0.2 | seed=1 | MAE=6.7619e-02 | t=0.1569s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.2824e-01 | t=0.0088s
    trss | MR=0.2 | seed=1 | MAE=2.0456e-02 | t=0.0212s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.3803e-01 | t=2.6324s
    tv | MR=0.2 | seed=0 | MAE=6.8984e-02 | t=0.1748s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5186e-01 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=2.4877e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8097e-01 | t=1.2435s

Completed: 2026-04-16T08:56:50.011796+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.