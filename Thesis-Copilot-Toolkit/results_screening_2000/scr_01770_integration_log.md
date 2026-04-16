# Integration Log: scr_01770
Started: 2026-04-16T09:34:45.006046+00:00
Description: Screening scr_01770 ds=iv100hz_mat graph=gaussian miss=3ch mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=5.9108e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=1.1659e-02 | t=0.1862s
    trss | MR=0.2 | seed=0 | MAE=1.2033e-02 | t=0.0218s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.5109e-02 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0836e-01 | t=1.2938s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=5.9178e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=1.0126e-02 | t=0.1843s
    trss | MR=0.2 | seed=1 | MAE=1.2085e-02 | t=0.0212s

Completed: 2026-04-16T09:34:45.006891+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.