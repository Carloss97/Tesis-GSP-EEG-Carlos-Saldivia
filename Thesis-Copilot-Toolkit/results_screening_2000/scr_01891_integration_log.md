# Integration Log: scr_01891
Started: 2026-04-16T09:51:49.818334+00:00
Description: Screening scr_01891 ds=iris_graph_signal graph=gaussian miss=[0.1] mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0009s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4303e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.1719e-01 | t=0.0612s
    trss | MR=0.2 | seed=0 | MAE=1.0946e-01 | t=0.0028s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.1187e-01 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8686e-01 | t=0.5823s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5504e-01 | t=0.0023s
    tv | MR=0.2 | seed=1 | MAE=1.2884e-01 | t=0.0525s
    trss | MR=0.2 | seed=1 | MAE=1.2042e-01 | t=0.0027s

Completed: 2026-04-16T09:51:49.819190+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.