# Integration Log: scr_01348
Started: 2026-04-16T08:37:34.041404+00:00
Description: Screening scr_01348 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.1870s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8690e-01 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.1467e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.8104e-01 | t=1.2587s
    tv | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.1844s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.8658e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.1935e-02 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.8230e-01 | t=1.3137s
    tv | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.1861s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0040e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.2551e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.8742e-01 | t=1.2890s

Completed: 2026-04-16T08:37:34.042094+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.