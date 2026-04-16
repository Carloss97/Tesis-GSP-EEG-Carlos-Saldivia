# Integration Log: scr_01603
Started: 2026-04-16T09:11:09.268131+00:00
Description: Screening scr_01603 ds=iris_graph_signal graph=vknng miss=1ch mode=noise

## Dataset: iris_graph_signal | rows=42
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=1.2976e-01 | t=0.0009s
    nearest | MR=0.2 | seed=0 | MAE=1.6607e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6653e-01 | t=0.0023s
    tv | MR=0.2 | seed=0 | MAE=1.2731e-01 | t=0.0515s
    trss | MR=0.2 | seed=0 | MAE=1.0212e-01 | t=0.0025s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2341e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6112e-01 | t=0.6665s
    mean | MR=0.2 | seed=1 | MAE=1.3990e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5334e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7224e-01 | t=0.0023s
    tv | MR=0.2 | seed=1 | MAE=1.3763e-01 | t=0.0528s
    trss | MR=0.2 | seed=1 | MAE=1.1111e-01 | t=0.0026s

Completed: 2026-04-16T09:11:09.269012+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.