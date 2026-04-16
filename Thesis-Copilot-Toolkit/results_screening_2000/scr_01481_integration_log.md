# Integration Log: scr_01481
Started: 2026-04-16T08:54:18.750175+00:00
Description: Screening scr_01481 ds=bci_iv2a_real_s3 graph=knng miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=6.5831e-02 | t=0.1486s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7593e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.2325e-02 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2274e-01 | t=1.3591s
    tv | MR=0.2 | seed=1 | MAE=6.8935e-02 | t=0.1582s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7788e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.4044e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.2137e-01 | t=1.8355s
    tv | MR=0.2 | seed=0 | MAE=6.5823e-02 | t=0.1611s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0861e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.5224e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.0645e-01 | t=1.2524s

Completed: 2026-04-16T08:54:18.750875+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.