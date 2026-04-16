# Integration Log: scr_01528
Started: 2026-04-16T09:00:20.176829+00:00
Description: Screening scr_01528 ds=bci_iv2a_real_s2 graph=knn miss=1ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=8.8358e-02 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1611s
    trss | MR=0.2 | seed=0 | MAE=2.5877e-02 | t=0.0191s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0752e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2079e-01 | t=1.6824s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=8.7683e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.0058e-02 | t=0.1536s
    trss | MR=0.2 | seed=1 | MAE=2.5193e-02 | t=0.0196s

Completed: 2026-04-16T09:00:20.177776+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.