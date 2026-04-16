# Integration Log: scr_01338
Started: 2026-04-16T08:36:35.776161+00:00
Description: Screening scr_01338 ds=iv100hz_mat graph=gaussian miss=[0.3] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=1.0087e-02 | t=0.1840s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5931e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.6321e-03 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.0335e-02 | t=1.3220s
    tv | MR=0.2 | seed=1 | MAE=1.0479e-02 | t=0.1865s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.5941e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.5765e-03 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=7.0266e-02 | t=2.7170s
    tv | MR=0.2 | seed=0 | MAE=1.0842e-02 | t=0.1855s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.9243e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=5.0087e-03 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.1136e-02 | t=2.6123s

Completed: 2026-04-16T08:36:35.777006+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.