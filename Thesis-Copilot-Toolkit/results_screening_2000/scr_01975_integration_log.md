# Integration Log: scr_01975
Started: 2026-04-16T10:03:47.074185+00:00
Description: Screening scr_01975 ds=iris_graph_signal graph=knn miss=[0.2] mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0010s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6653e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.2731e-01 | t=0.0517s
    trss | MR=0.2 | seed=0 | MAE=1.0212e-01 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2341e-01 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6112e-01 | t=0.0180s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0010s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7224e-01 | t=0.0024s
    tv | MR=0.2 | seed=1 | MAE=1.3763e-01 | t=0.0523s
    trss | MR=0.2 | seed=1 | MAE=1.1111e-01 | t=0.0030s

Completed: 2026-04-16T10:03:47.075055+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.