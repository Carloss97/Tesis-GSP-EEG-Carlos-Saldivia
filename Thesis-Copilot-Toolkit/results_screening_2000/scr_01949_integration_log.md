# Integration Log: scr_01949
Started: 2026-04-16T10:00:02.024654+00:00
Description: Screening scr_01949 ds=bci_iv2a_real_s3 graph=knn miss=[0.2] mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6510e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5968e-02 | t=0.1488s
    trss | MR=0.2 | seed=0 | MAE=6.0854e-02 | t=0.0207s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.9232e-01 | t=0.0083s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.6205e-01 | t=2.6897s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=1.6716e-01 | t=0.0056s
    tv | MR=0.2 | seed=1 | MAE=6.8824e-02 | t=0.1447s
    trss | MR=0.2 | seed=1 | MAE=6.3060e-02 | t=0.0213s

Completed: 2026-04-16T10:00:02.025516+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.