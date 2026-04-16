# Integration Log: scr_01410
Started: 2026-04-16T08:45:29.209862+00:00
Description: Screening scr_01410 ds=iv100hz_mat graph=knn miss=[0.4] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=1.5679e-02 | t=0.1462s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.2619e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.8477e-03 | t=0.0213s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2276e-02 | t=1.2970s
    tv | MR=0.2 | seed=1 | MAE=1.6902e-02 | t=0.1405s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=3.2742e-02 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=3.8665e-03 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.2198e-02 | t=1.3835s
    tv | MR=0.2 | seed=0 | MAE=1.5650e-02 | t=0.1410s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1107e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=5.5533e-03 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.5504e-02 | t=1.4433s

Completed: 2026-04-16T08:45:29.210564+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.