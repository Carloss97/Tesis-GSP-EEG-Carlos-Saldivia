# Integration Log: scr_01579
Started: 2026-04-16T09:07:44.150019+00:00
Description: Screening scr_01579 ds=iris_graph_signal graph=kalofolias miss=1ch mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0014s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=5.4007e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0516s
    trss | MR=0.2 | seed=0 | MAE=9.4246e-02 | t=0.0027s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.3422e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.2340e-01 | t=0.0536s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=1 | MAE=5.3692e-01 | t=0.0023s
    tv | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0509s
    trss | MR=0.2 | seed=1 | MAE=1.0397e-01 | t=0.0025s

Completed: 2026-04-16T09:07:44.150804+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.