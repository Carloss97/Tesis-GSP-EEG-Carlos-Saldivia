# Integration Log: scr_01950
Started: 2026-04-16T10:00:16.647051+00:00
Description: Screening scr_01950 ds=iv100hz_mat graph=knn miss=[0.2] mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=4.0927e-02 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=1.6549e-02 | t=0.1470s
    trss | MR=0.2 | seed=0 | MAE=1.3699e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.8058e-02 | t=0.0090s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.1624e-02 | t=1.3470s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=4.1033e-02 | t=0.0056s
    tv | MR=0.2 | seed=1 | MAE=1.6116e-02 | t=0.1400s
    trss | MR=0.2 | seed=1 | MAE=1.3713e-02 | t=0.0198s

Completed: 2026-04-16T10:00:16.647922+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.