# Integration Log: scr_01373
Started: 2026-04-16T08:40:46.684837+00:00
Description: Screening scr_01373 ds=bci_iv2a_real_s3 graph=knng miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=6.5831e-02 | t=0.1719s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7593e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.2325e-02 | t=0.0203s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2274e-01 | t=1.2667s
    tv | MR=0.2 | seed=1 | MAE=6.8935e-02 | t=0.1507s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7788e-01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=3.4044e-02 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.2137e-01 | t=1.2575s
    tv | MR=0.2 | seed=0 | MAE=6.5823e-02 | t=0.1514s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0861e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.5224e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.0645e-01 | t=1.2741s

Completed: 2026-04-16T08:40:46.685564+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.