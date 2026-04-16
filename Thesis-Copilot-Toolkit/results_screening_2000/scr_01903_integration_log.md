# Integration Log: scr_01903
Started: 2026-04-16T09:53:31.501835+00:00
Description: Screening scr_01903 ds=iris_graph_signal graph=kalofolias miss=[0.1] mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0009s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=5.4007e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0521s
    trss | MR=0.2 | seed=0 | MAE=9.4246e-02 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.3422e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.2340e-01 | t=0.0220s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0010s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=1 | MAE=5.3692e-01 | t=0.0023s
    tv | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0513s
    trss | MR=0.2 | seed=1 | MAE=1.0397e-01 | t=0.0026s

Completed: 2026-04-16T09:53:31.502527+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.