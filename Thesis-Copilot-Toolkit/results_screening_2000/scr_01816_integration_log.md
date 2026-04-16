# Integration Log: scr_01816
Started: 2026-04-16T09:41:00.624289+00:00
Description: Screening scr_01816 ds=bci_iv2a_real_s2 graph=vknng miss=3ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=6.1660e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=3.0785e-02 | t=0.1488s
    trss | MR=0.2 | seed=0 | MAE=2.8284e-02 | t=0.0208s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8839e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7059e-01 | t=2.8663s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=6.1090e-02 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.1431s
    trss | MR=0.2 | seed=1 | MAE=2.7654e-02 | t=0.0204s

Completed: 2026-04-16T09:41:00.625163+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.