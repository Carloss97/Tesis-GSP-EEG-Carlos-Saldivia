# Integration Log: scr_01515
Started: 2026-04-16T08:58:21.295603+00:00
Description: Screening scr_01515 ds=bci_iv2a_real_s1 graph=knn miss=1ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.5951e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.0453e-02 | t=0.1475s
    trss | MR=0.2 | seed=0 | MAE=4.9756e-02 | t=0.0201s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8600e-01 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.6257e-01 | t=1.3073s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5667e-01 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=6.9158e-02 | t=0.1587s
    trss | MR=0.2 | seed=1 | MAE=5.0139e-02 | t=0.0195s

Completed: 2026-04-16T08:58:21.296460+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.