# Integration Log: scr_01398
Started: 2026-04-16T08:44:00.352188+00:00
Description: Screening scr_01398 ds=iv100hz_mat graph=aew miss=[0.3] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=1.1963e-02 | t=0.1412s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.9706e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.5301e-03 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1654e-02 | t=1.3297s
    tv | MR=0.2 | seed=1 | MAE=1.3497e-02 | t=0.1415s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.9832e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.5809e-03 | t=0.0201s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.1607e-02 | t=1.3744s
    tv | MR=0.2 | seed=0 | MAE=1.3547e-02 | t=0.1413s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.7488e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=5.0372e-03 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.4213e-02 | t=1.4459s

Completed: 2026-04-16T08:44:00.353093+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.