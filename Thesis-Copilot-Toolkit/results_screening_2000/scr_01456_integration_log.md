# Integration Log: scr_01456
Started: 2026-04-16T08:51:03.871233+00:00
Description: Screening scr_01456 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.1850s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8690e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.1467e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.8104e-01 | t=2.6264s
    tv | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.1881s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.8658e-01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=1.1935e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.8230e-01 | t=3.0155s
    tv | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.1852s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0040e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.2551e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.8742e-01 | t=1.5789s

Completed: 2026-04-16T08:51:03.872101+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.