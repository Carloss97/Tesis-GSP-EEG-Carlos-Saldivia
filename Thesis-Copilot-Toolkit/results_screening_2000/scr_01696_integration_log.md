# Integration Log: scr_01696
Started: 2026-04-16T09:24:02.389957+00:00
Description: Screening scr_01696 ds=bci_iv2a_real_s2 graph=knng miss=2ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=8.0845e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1502s
    trss | MR=0.2 | seed=0 | MAE=2.6797e-02 | t=0.0197s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0303e-01 | t=0.0092s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9064e-01 | t=1.2441s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=8.0060e-02 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=3.0058e-02 | t=0.1493s
    trss | MR=0.2 | seed=1 | MAE=2.6206e-02 | t=0.0201s

Completed: 2026-04-16T09:24:02.390878+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.