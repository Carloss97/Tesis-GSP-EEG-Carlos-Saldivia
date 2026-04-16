# Integration Log: scr_01687
Started: 2026-04-16T09:22:57.155275+00:00
Description: Screening scr_01687 ds=iris_graph_signal graph=kalofolias miss=2ch mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0009s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=5.4007e-01 | t=0.0022s
    tv | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0522s
    trss | MR=0.2 | seed=0 | MAE=9.4246e-02 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.3422e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.2340e-01 | t=0.0173s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=1 | MAE=5.3692e-01 | t=0.0022s
    tv | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0505s
    trss | MR=0.2 | seed=1 | MAE=1.0397e-01 | t=0.0026s

Completed: 2026-04-16T09:22:57.156141+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.