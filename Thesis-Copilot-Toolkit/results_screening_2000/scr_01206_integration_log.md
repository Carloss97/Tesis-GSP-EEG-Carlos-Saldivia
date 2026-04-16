# Integration Log: scr_01206
Started: 2026-04-16T08:20:07.722370+00:00
Description: Screening scr_01206 ds=iv100hz_mat graph=knn miss=[0.2] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=1.3914e-02 | t=0.1462s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.7790e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.8005e-03 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3167e-02 | t=1.4971s
    tv | MR=0.2 | seed=1 | MAE=1.2914e-02 | t=0.1450s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=3.8026e-02 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=3.7992e-03 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.3186e-02 | t=2.6595s
    tv | MR=0.2 | seed=0 | MAE=1.3420e-02 | t=0.1465s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8697e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=5.4759e-03 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.7914e-02 | t=2.4824s

Completed: 2026-04-16T08:20:07.723070+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.