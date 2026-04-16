# Integration Log: scr_01350
Started: 2026-04-16T08:38:04.930321+00:00
Description: Screening scr_01350 ds=iv100hz_mat graph=gaussian miss=[0.3] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=1.1596e-02 | t=0.1858s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.6542e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.6568e-03 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3597e-02 | t=2.8536s
    tv | MR=0.2 | seed=1 | MAE=1.1192e-02 | t=0.1972s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=3.6616e-02 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=3.6372e-03 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.3610e-02 | t=2.9416s
    tv | MR=0.2 | seed=0 | MAE=1.1190e-02 | t=0.2152s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.7473e-02 | t=0.0088s
    trss | MR=0.2 | seed=0 | MAE=5.2136e-03 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.9050e-02 | t=2.6310s

Completed: 2026-04-16T08:38:04.931018+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.