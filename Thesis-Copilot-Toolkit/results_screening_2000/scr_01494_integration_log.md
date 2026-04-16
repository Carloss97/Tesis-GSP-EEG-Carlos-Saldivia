# Integration Log: scr_01494
Started: 2026-04-16T08:56:05.152216+00:00
Description: Screening scr_01494 ds=iv100hz_mat graph=vknng miss=[0.4] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=1.4101e-02 | t=0.1407s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.2418e-02 | t=0.0107s
    trss | MR=0.2 | seed=0 | MAE=3.5810e-03 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2658e-02 | t=2.6267s
    tv | MR=0.2 | seed=1 | MAE=1.2991e-02 | t=0.1438s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=3.2530e-02 | t=0.0084s
    trss | MR=0.2 | seed=1 | MAE=3.5984e-03 | t=0.0202s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.2627e-02 | t=2.6186s
    tv | MR=0.2 | seed=0 | MAE=1.3651e-02 | t=0.1492s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1624e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=5.1335e-03 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6418e-02 | t=2.6289s

Completed: 2026-04-16T08:56:05.153078+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.