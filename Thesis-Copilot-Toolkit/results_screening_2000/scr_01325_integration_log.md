# Integration Log: scr_01325
Started: 2026-04-16T08:34:44.905430+00:00
Description: Screening scr_01325 ds=bci_iv2a_real_s3 graph=knn miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=6.5826e-02 | t=0.1605s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0348e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.0829e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7283e-01 | t=1.3624s
    tv | MR=0.2 | seed=1 | MAE=6.8927e-02 | t=0.1630s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.0465e-01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=3.2712e-02 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.7128e-01 | t=1.2349s
    tv | MR=0.2 | seed=0 | MAE=6.5821e-02 | t=0.1641s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.4819e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=3.3160e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7448e-01 | t=1.2768s

Completed: 2026-04-16T08:34:44.906324+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.