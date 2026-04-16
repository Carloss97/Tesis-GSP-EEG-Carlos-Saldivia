# Integration Log: scr_01588
Started: 2026-04-16T09:08:48.238008+00:00
Description: Screening scr_01588 ds=bci_iv2a_real_s2 graph=knng miss=1ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=8.0845e-02 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1523s
    trss | MR=0.2 | seed=0 | MAE=2.6797e-02 | t=0.0198s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0303e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9064e-01 | t=1.2563s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=8.0060e-02 | t=0.0061s
    tv | MR=0.2 | seed=1 | MAE=3.0058e-02 | t=0.1504s
    trss | MR=0.2 | seed=1 | MAE=2.6206e-02 | t=0.0198s

Completed: 2026-04-16T09:08:48.238861+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.