# Integration Log: scr_01493
Started: 2026-04-16T08:55:48.316810+00:00
Description: Screening scr_01493 ds=bci_iv2a_real_s3 graph=vknng miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=6.5830e-02 | t=0.1417s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5428e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=3.9749e-02 | t=0.0201s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.2511e-01 | t=1.3156s
    tv | MR=0.2 | seed=1 | MAE=6.8928e-02 | t=0.1415s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5592e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.9897e-02 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.2444e-01 | t=1.4062s
    tv | MR=0.2 | seed=0 | MAE=6.5823e-02 | t=0.1410s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7130e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=4.1479e-02 | t=0.0201s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7691e-01 | t=1.3697s

Completed: 2026-04-16T08:55:48.317507+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.