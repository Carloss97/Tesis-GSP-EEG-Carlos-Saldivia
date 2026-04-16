# Integration Log: scr_01743
Started: 2026-04-16T09:30:28.878395+00:00
Description: Screening scr_01743 ds=bci_iv2a_real_s1 graph=knn miss=3ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.9976e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.0455e-02 | t=0.1650s
    trss | MR=0.2 | seed=0 | MAE=5.0462e-02 | t=0.0194s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.2409e-01 | t=0.0090s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.2265e-01 | t=1.2380s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.9563e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.9160e-02 | t=0.1572s
    trss | MR=0.2 | seed=1 | MAE=5.0678e-02 | t=0.0198s

Completed: 2026-04-16T09:30:28.879139+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.