# Integration Log: scr_01302
Started: 2026-04-16T08:31:59.391556+00:00
Description: Screening scr_01302 ds=iv100hz_mat graph=knn miss=[0.3] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=1.5679e-02 | t=0.1410s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.2619e-02 | t=0.0086s
    trss | MR=0.2 | seed=0 | MAE=3.8477e-03 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2276e-02 | t=1.3490s
    tv | MR=0.2 | seed=1 | MAE=1.6902e-02 | t=0.1406s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=3.2742e-02 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=3.8665e-03 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.2198e-02 | t=1.2924s
    tv | MR=0.2 | seed=0 | MAE=1.5650e-02 | t=0.1432s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1107e-02 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=5.5533e-03 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.5504e-02 | t=1.3220s

Completed: 2026-04-16T08:31:59.392252+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.