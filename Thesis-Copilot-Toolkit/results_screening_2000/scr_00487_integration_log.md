# Integration Log: scr_00487
Started: 2026-04-16T13:47:50.639179+00:00
Description: Screening scr_00487 ds=iris_graph_signal graph=gaussian miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0009s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4209e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.0936e-01 | t=0.1134s
    trss | MR=0.2 | seed=0 | MAE=1.0897e-01 | t=0.0039s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.1049e-01 | t=0.0039s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8607e-01 | t=8.0277s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0016s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0017s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5325e-01 | t=0.0047s
    tv | MR=0.2 | seed=1 | MAE=1.2181e-01 | t=0.1094s
    trss | MR=0.2 | seed=1 | MAE=1.1909e-01 | t=0.0049s

Completed: 2026-04-16T13:47:50.640065+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.