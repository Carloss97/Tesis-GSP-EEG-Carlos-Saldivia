# Integration Log: scr_01268
Started: 2026-04-16T08:27:51.369967+00:00
Description: Screening scr_01268 ds=movielens_graph_signal graph=knng miss=[0.2] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=3.6166e-02 | t=0.1423s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.5678e-02 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=6.1912e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2500e-01 | t=1.3104s
    tv | MR=0.2 | seed=1 | MAE=4.0359e-02 | t=0.1409s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.2332e-02 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=7.3697e-02 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2440e-01 | t=1.4565s
    tv | MR=0.2 | seed=0 | MAE=3.6335e-02 | t=0.1430s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0267e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=5.8482e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3262e-01 | t=1.4111s

Completed: 2026-04-16T08:27:51.370659+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.