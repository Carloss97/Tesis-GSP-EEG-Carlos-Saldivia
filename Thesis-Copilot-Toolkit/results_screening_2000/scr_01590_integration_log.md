# Integration Log: scr_01590
Started: 2026-04-16T09:09:21.348642+00:00
Description: Screening scr_01590 ds=iv100hz_mat graph=knng miss=1ch mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=4.0521e-02 | t=0.0061s
    tv | MR=0.2 | seed=0 | MAE=1.2964e-02 | t=0.1434s
    trss | MR=0.2 | seed=0 | MAE=1.2705e-02 | t=0.0194s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.8994e-02 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.2986e-02 | t=1.3408s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=4.0614e-02 | t=0.0056s
    tv | MR=0.2 | seed=1 | MAE=1.3874e-02 | t=0.1423s
    trss | MR=0.2 | seed=1 | MAE=1.2763e-02 | t=0.0196s

Completed: 2026-04-16T09:09:21.349357+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.