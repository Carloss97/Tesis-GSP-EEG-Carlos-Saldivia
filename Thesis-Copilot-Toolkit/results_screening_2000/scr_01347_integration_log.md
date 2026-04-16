# Integration Log: scr_01347
Started: 2026-04-16T08:37:21.337496+00:00
Description: Screening scr_01347 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.2245s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.5543e-01 | t=0.0108s
    trss | MR=0.2 | seed=0 | MAE=1.6729e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.1949e-01 | t=2.8409s
    tv | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.1875s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.5194e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.6375e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.1842e-01 | t=2.8682s
    tv | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.1854s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.0613e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.1751e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.9989e-01 | t=2.6433s

Completed: 2026-04-16T08:37:21.338363+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.