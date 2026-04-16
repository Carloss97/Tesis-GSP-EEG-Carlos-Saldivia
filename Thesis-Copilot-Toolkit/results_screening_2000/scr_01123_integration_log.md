# Integration Log: scr_01123
Started: 2026-04-16T14:04:19.790049+00:00
Description: Screening scr_01123 ds=iris_graph_signal graph=gaussian miss=[0.1] mode=lambda

## Dataset: iris_graph_signal | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=1.0968e-01 | t=0.2336s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8432e-01 | t=0.0041s
    trss | MR=0.2 | seed=0 | MAE=7.7729e-02 | t=0.0069s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.6116e-01 | t=12.6330s
    tv | MR=0.2 | seed=1 | MAE=1.2948e-01 | t=0.0535s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.9347e-01 | t=0.0025s
    trss | MR=0.2 | seed=1 | MAE=8.6784e-02 | t=0.0027s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.6164e-01 | t=1.4536s
    tv | MR=0.2 | seed=0 | MAE=1.1401e-01 | t=0.0549s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0534e-01 | t=0.0026s
    trss | MR=0.2 | seed=0 | MAE=7.8196e-02 | t=0.0027s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8465e-01 | t=1.5081s

Completed: 2026-04-16T14:04:19.790887+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.