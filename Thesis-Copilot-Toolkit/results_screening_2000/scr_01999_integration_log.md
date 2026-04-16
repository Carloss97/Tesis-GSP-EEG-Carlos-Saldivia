# Integration Log: scr_01999
Started: 2026-04-16T10:07:21.787008+00:00
Description: Screening scr_01999 ds=iris_graph_signal graph=gaussian miss=[0.2] mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0009s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0010s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4303e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.1719e-01 | t=0.0645s
    trss | MR=0.2 | seed=0 | MAE=1.0946e-01 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.1187e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8686e-01 | t=0.2031s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5504e-01 | t=0.0023s
    tv | MR=0.2 | seed=1 | MAE=1.2884e-01 | t=0.0827s
    trss | MR=0.2 | seed=1 | MAE=1.2042e-01 | t=0.0027s

Completed: 2026-04-16T10:07:21.787878+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.