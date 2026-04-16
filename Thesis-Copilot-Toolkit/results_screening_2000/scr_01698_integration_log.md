# Integration Log: scr_01698
Started: 2026-04-16T09:24:34.519036+00:00
Description: Screening scr_01698 ds=iv100hz_mat graph=knng miss=2ch mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=4.0521e-02 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=1.2964e-02 | t=0.1442s
    trss | MR=0.2 | seed=0 | MAE=1.2705e-02 | t=0.0197s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.8994e-02 | t=0.0104s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.2986e-02 | t=1.4454s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=1 | MAE=4.0614e-02 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=1.3874e-02 | t=0.1421s
    trss | MR=0.2 | seed=1 | MAE=1.2763e-02 | t=0.0202s

Completed: 2026-04-16T09:24:34.519867+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.