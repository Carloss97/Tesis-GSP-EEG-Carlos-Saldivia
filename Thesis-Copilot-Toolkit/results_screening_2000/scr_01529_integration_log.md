# Integration Log: scr_01529
Started: 2026-04-16T09:00:34.506289+00:00
Description: Screening scr_01529 ds=bci_iv2a_real_s3 graph=knn miss=1ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0651e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=6.5968e-02 | t=0.1535s
    trss | MR=0.2 | seed=0 | MAE=5.6991e-02 | t=0.0193s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.3011e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3703e-01 | t=1.2836s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0805e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.8823e-02 | t=0.1535s
    trss | MR=0.2 | seed=1 | MAE=5.9810e-02 | t=0.0196s

Completed: 2026-04-16T09:00:34.506970+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.