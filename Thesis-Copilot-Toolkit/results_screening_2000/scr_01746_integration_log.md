# Integration Log: scr_01746
Started: 2026-04-16T09:31:20.801186+00:00
Description: Screening scr_01746 ds=iv100hz_mat graph=knn miss=3ch mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=4.8556e-02 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=1.4274e-02 | t=0.1464s
    trss | MR=0.2 | seed=0 | MAE=1.3301e-02 | t=0.0198s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.6773e-02 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.9183e-02 | t=1.3070s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=4.8707e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=1.3432e-02 | t=0.1458s
    trss | MR=0.2 | seed=1 | MAE=1.3433e-02 | t=0.0197s

Completed: 2026-04-16T09:31:20.801957+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.