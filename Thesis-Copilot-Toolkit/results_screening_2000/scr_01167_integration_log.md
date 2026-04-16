# Integration Log: scr_01167
Started: 2026-04-16T14:52:03.677904+00:00
Description: Screening scr_01167 ds=bci_iv2a_real_s1 graph=vknng miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=3.0346e-06 | t=0.6814s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.7043e-06 | t=0.0646s
    trss | MR=0.2 | seed=0 | MAE=1.0104e-06 | t=0.1467s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.8888e-06 | t=15.7596s
    tv | MR=0.2 | seed=1 | MAE=3.3726e-06 | t=0.1590s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.0223e-06 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=1.2847e-06 | t=0.0210s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.0921e-06 | t=18.0904s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.8809s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.5039e-06 | t=0.0161s
    trss | MR=0.2 | seed=0 | MAE=1.1873e-06 | t=0.3052s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.7292e-06 | t=15.3163s

Completed: 2026-04-16T14:52:03.678877+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.