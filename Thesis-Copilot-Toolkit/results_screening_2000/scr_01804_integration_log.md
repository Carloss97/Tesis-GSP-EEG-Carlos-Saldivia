# Integration Log: scr_01804
Started: 2026-04-16T09:39:18.258073+00:00
Description: Screening scr_01804 ds=bci_iv2a_real_s2 graph=knng miss=3ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=8.0845e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1510s
    trss | MR=0.2 | seed=0 | MAE=2.6797e-02 | t=0.0201s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0303e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9064e-01 | t=1.2649s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=8.0060e-02 | t=0.0056s
    tv | MR=0.2 | seed=1 | MAE=3.0058e-02 | t=0.1512s
    trss | MR=0.2 | seed=1 | MAE=2.6206e-02 | t=0.0207s

Completed: 2026-04-16T09:39:18.258891+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.