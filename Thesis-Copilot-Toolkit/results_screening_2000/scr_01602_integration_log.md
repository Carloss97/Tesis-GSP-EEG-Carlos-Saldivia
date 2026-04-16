# Integration Log: scr_01602
Started: 2026-04-16T09:11:05.263005+00:00
Description: Screening scr_01602 ds=iv100hz_mat graph=vknng miss=1ch mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=4.1395e-02 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=1.3358e-02 | t=0.1429s
    trss | MR=0.2 | seed=0 | MAE=1.2543e-02 | t=0.0199s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.0008e-02 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.3924e-02 | t=1.2997s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=4.1496e-02 | t=0.0061s
    tv | MR=0.2 | seed=1 | MAE=1.2900e-02 | t=0.1429s
    trss | MR=0.2 | seed=1 | MAE=1.2601e-02 | t=0.0196s

Completed: 2026-04-16T09:11:05.263870+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.