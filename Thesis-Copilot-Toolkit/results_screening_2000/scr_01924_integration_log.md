# Integration Log: scr_01924
Started: 2026-04-16T09:56:19.935306+00:00
Description: Screening scr_01924 ds=bci_iv2a_real_s2 graph=vknng miss=[0.1] mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=6.1660e-02 | t=0.0066s
    tv | MR=0.2 | seed=0 | MAE=3.0785e-02 | t=0.1462s
    trss | MR=0.2 | seed=0 | MAE=2.8284e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8839e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7059e-01 | t=1.5521s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=6.1090e-02 | t=0.0056s
    tv | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.1398s
    trss | MR=0.2 | seed=1 | MAE=2.7654e-02 | t=0.0201s

Completed: 2026-04-16T09:56:19.936160+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.