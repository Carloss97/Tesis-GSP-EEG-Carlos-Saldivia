# Integration Log: scr_01491
Started: 2026-04-16T08:55:22.349070+00:00
Description: Screening scr_01491 ds=bci_iv2a_real_s1 graph=vknng miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=6.9290e-02 | t=0.1483s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2983e-01 | t=0.0086s
    trss | MR=0.2 | seed=0 | MAE=2.2627e-02 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.2989e-01 | t=2.5398s
    tv | MR=0.2 | seed=1 | MAE=6.8252e-02 | t=0.1530s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.2813e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=2.3703e-02 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.3018e-01 | t=2.8574s
    tv | MR=0.2 | seed=0 | MAE=6.9305e-02 | t=0.1436s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5138e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.6609e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.6105e-01 | t=2.0266s

Completed: 2026-04-16T08:55:22.349879+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.