# Integration Log: scr_01851
Started: 2026-04-16T09:45:46.790390+00:00
Description: Screening scr_01851 ds=bci_iv2a_real_s1 graph=knn miss=[0.1] mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.9976e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=7.0455e-02 | t=0.1575s
    trss | MR=0.2 | seed=0 | MAE=5.0462e-02 | t=0.0204s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.2409e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.2265e-01 | t=1.2463s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0025s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=1.9563e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.9160e-02 | t=0.1584s
    trss | MR=0.2 | seed=1 | MAE=5.0678e-02 | t=0.0200s

Completed: 2026-04-16T09:45:46.791261+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.