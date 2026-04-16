# Integration Log: scr_01951
Started: 2026-04-16T10:00:19.440632+00:00
Description: Screening scr_01951 ds=iris_graph_signal graph=knn miss=[0.2] mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0011s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6852e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.3002e-01 | t=0.0521s
    trss | MR=0.2 | seed=0 | MAE=1.1350e-01 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1880e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1179e-01 | t=0.0217s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7264e-01 | t=0.0023s
    tv | MR=0.2 | seed=1 | MAE=1.4016e-01 | t=0.0527s
    trss | MR=0.2 | seed=1 | MAE=1.2040e-01 | t=0.0026s

Completed: 2026-04-16T10:00:19.441548+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.