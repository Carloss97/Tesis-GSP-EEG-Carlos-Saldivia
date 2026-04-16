# Integration Log: scr_01843
Started: 2026-04-16T09:44:58.081118+00:00
Description: Screening scr_01843 ds=iris_graph_signal graph=knn miss=[0.1] mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0010s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6852e-01 | t=0.0028s
    tv | MR=0.2 | seed=0 | MAE=1.3002e-01 | t=0.0530s
    trss | MR=0.2 | seed=0 | MAE=1.1350e-01 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1880e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1179e-01 | t=0.0824s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7264e-01 | t=0.0023s
    tv | MR=0.2 | seed=1 | MAE=1.4016e-01 | t=0.0525s
    trss | MR=0.2 | seed=1 | MAE=1.2040e-01 | t=0.0027s

Completed: 2026-04-16T09:44:58.081815+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.