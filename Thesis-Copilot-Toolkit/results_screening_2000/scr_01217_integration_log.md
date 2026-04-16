# Integration Log: scr_01217
Started: 2026-04-16T08:21:18.373098+00:00
Description: Screening scr_01217 ds=bci_iv2a_real_s3 graph=knn miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=6.5826e-02 | t=0.1612s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0348e-01 | t=0.0086s
    trss | MR=0.2 | seed=0 | MAE=3.0829e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7283e-01 | t=1.3293s
    tv | MR=0.2 | seed=1 | MAE=6.8927e-02 | t=0.1639s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.0465e-01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=3.2712e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.7128e-01 | t=1.3423s
    tv | MR=0.2 | seed=0 | MAE=6.5821e-02 | t=0.1692s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.4819e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=3.3160e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7448e-01 | t=1.2947s

Completed: 2026-04-16T08:21:18.373950+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.