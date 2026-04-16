# Integration Log: scr_01987
Started: 2026-04-16T10:05:34.477337+00:00
Description: Screening scr_01987 ds=iris_graph_signal graph=gaussian miss=[0.2] mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0009s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8458e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.2591e-01 | t=0.0523s
    trss | MR=0.2 | seed=0 | MAE=9.9725e-02 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1844e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.1540e-01 | t=0.0179s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0013s
    tikhonov | MR=0.2 | seed=1 | MAE=1.9407e-01 | t=0.0023s
    tv | MR=0.2 | seed=1 | MAE=1.3352e-01 | t=0.0523s
    trss | MR=0.2 | seed=1 | MAE=1.0914e-01 | t=0.0026s

Completed: 2026-04-16T10:05:34.478046+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.