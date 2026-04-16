# Integration Log: scr_01614
Started: 2026-04-16T09:12:48.108033+00:00
Description: Screening scr_01614 ds=iv100hz_mat graph=aew miss=1ch mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=0 | MAE=3.7172e-02 | t=0.0060s
    tv | MR=0.2 | seed=0 | MAE=1.2975e-02 | t=0.1542s
    trss | MR=0.2 | seed=0 | MAE=1.2537e-02 | t=0.0202s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.4633e-02 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.8731e-02 | t=2.6362s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0024s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=3.7305e-02 | t=0.0063s
    tv | MR=0.2 | seed=1 | MAE=1.3140e-02 | t=0.1557s
    trss | MR=0.2 | seed=1 | MAE=1.2630e-02 | t=0.0216s

Completed: 2026-04-16T09:12:48.108915+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.