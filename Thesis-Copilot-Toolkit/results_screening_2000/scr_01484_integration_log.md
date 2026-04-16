# Integration Log: scr_01484
Started: 2026-04-16T08:54:52.128893+00:00
Description: Screening scr_01484 ds=movielens_graph_signal graph=knng miss=[0.4] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=3.6166e-02 | t=0.1441s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.5678e-02 | t=0.0086s
    trss | MR=0.2 | seed=0 | MAE=6.1912e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2500e-01 | t=1.3182s
    tv | MR=0.2 | seed=1 | MAE=4.0359e-02 | t=0.1568s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.2332e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=7.3697e-02 | t=0.0210s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2440e-01 | t=1.3668s
    tv | MR=0.2 | seed=0 | MAE=3.6335e-02 | t=0.1428s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0267e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=5.8482e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3262e-01 | t=1.3147s

Completed: 2026-04-16T08:54:52.129744+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.