# Integration Log: scr_01448
Started: 2026-04-16T08:50:20.286428+00:00
Description: Screening scr_01448 ds=movielens_graph_signal graph=gaussian miss=[0.4] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6522e-02 | t=0.1889s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1698e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=6.2495e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2855e-01 | t=2.7223s
    tv | MR=0.2 | seed=1 | MAE=4.0222e-02 | t=0.1877s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1722e-01 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=6.8301e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2569e-01 | t=2.8563s
    tv | MR=0.2 | seed=0 | MAE=3.6526e-02 | t=0.1897s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4254e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=5.9131e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3863e-01 | t=1.6164s

Completed: 2026-04-16T08:50:20.287124+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.