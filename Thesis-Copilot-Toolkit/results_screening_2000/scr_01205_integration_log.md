# Integration Log: scr_01205
Started: 2026-04-16T08:19:49.444723+00:00
Description: Screening scr_01205 ds=bci_iv2a_real_s3 graph=knn miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=6.5829e-02 | t=0.1547s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8700e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.1664e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2711e-01 | t=1.2800s
    tv | MR=0.2 | seed=1 | MAE=6.8932e-02 | t=0.1580s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.8851e-01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=3.3432e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.2510e-01 | t=1.3135s
    tv | MR=0.2 | seed=0 | MAE=6.5822e-02 | t=0.1518s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2509e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=3.4453e-02 | t=0.0208s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.1914e-01 | t=1.3063s

Completed: 2026-04-16T08:19:49.445421+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.