# Integration Log: scr_01592
Started: 2026-04-16T09:09:43.562546+00:00
Description: Screening scr_01592 ds=movielens_graph_signal graph=knng miss=1ch mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4042e-01 | t=0.0062s
    tv | MR=0.2 | seed=0 | MAE=5.8603e-02 | t=0.1489s
    trss | MR=0.2 | seed=0 | MAE=7.2339e-02 | t=0.0195s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.4958e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5499e-01 | t=1.4454s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=1 | MAE=1.4283e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.5939e-02 | t=0.1465s
    trss | MR=0.2 | seed=1 | MAE=8.0003e-02 | t=0.0195s

Completed: 2026-04-16T09:09:43.563409+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.