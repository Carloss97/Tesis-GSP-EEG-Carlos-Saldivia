# Integration Log: scr_01733
Started: 2026-04-16T09:29:23.409257+00:00
Description: Screening scr_01733 ds=bci_iv2a_real_s3 graph=knn miss=3ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0075s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6510e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=6.5968e-02 | t=0.1524s
    trss | MR=0.2 | seed=0 | MAE=6.0854e-02 | t=0.0190s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.9232e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.6205e-01 | t=2.6031s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.6716e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.8824e-02 | t=0.1581s
    trss | MR=0.2 | seed=1 | MAE=6.3060e-02 | t=0.0199s

Completed: 2026-04-16T09:29:23.410002+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.