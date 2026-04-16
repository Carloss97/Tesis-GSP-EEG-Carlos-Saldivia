# Integration Log: scr_01974
Started: 2026-04-16T10:03:44.339510+00:00
Description: Screening scr_01974 ds=iv100hz_mat graph=knn miss=[0.2] mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=5.3524e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=1.4366e-02 | t=0.1532s
    trss | MR=0.2 | seed=0 | MAE=1.2657e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.0996e-02 | t=0.0085s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.6773e-02 | t=2.5528s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0036s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=5.3680e-02 | t=0.0072s
    tv | MR=0.2 | seed=1 | MAE=1.4148e-02 | t=0.1502s
    trss | MR=0.2 | seed=1 | MAE=1.2819e-02 | t=0.0204s

Completed: 2026-04-16T10:03:44.340215+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.