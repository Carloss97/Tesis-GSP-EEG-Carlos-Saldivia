# Integration Log: scr_01960
Started: 2026-04-16T10:01:28.330037+00:00
Description: Screening scr_01960 ds=bci_iv2a_real_s2 graph=knn miss=[0.2] mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=8.8358e-02 | t=0.0059s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1549s
    trss | MR=0.2 | seed=0 | MAE=2.5877e-02 | t=0.0201s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0752e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2079e-01 | t=1.3751s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=8.7683e-02 | t=0.0068s
    tv | MR=0.2 | seed=1 | MAE=3.0058e-02 | t=0.1866s
    trss | MR=0.2 | seed=1 | MAE=2.5193e-02 | t=0.0224s

Completed: 2026-04-16T10:01:28.330878+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.