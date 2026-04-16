# Integration Log: scr_01722
Started: 2026-04-16T09:27:58.915539+00:00
Description: Screening scr_01722 ds=iv100hz_mat graph=aew miss=2ch mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=3.7172e-02 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=1.2975e-02 | t=0.1448s
    trss | MR=0.2 | seed=0 | MAE=1.2537e-02 | t=0.0201s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.4633e-02 | t=0.0088s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.8731e-02 | t=2.8642s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=3.7305e-02 | t=0.0060s
    tv | MR=0.2 | seed=1 | MAE=1.3140e-02 | t=0.1498s
    trss | MR=0.2 | seed=1 | MAE=1.2630e-02 | t=0.0201s

Completed: 2026-04-16T09:27:58.916402+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.