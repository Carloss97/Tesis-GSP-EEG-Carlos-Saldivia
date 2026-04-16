# Integration Log: scr_01240
Started: 2026-04-16T08:24:03.707983+00:00
Description: Screening scr_01240 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.1878s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8690e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.1467e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.8104e-01 | t=1.3097s
    tv | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.1858s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.8658e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.1935e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.8230e-01 | t=1.2494s
    tv | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.1950s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0040e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.2551e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.8742e-01 | t=1.3061s

Completed: 2026-04-16T08:24:03.708856+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.