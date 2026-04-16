# Integration Log: scr_00416
Started: 2026-04-16T13:23:58.613576+00:00
Description: Screening scr_00416 ds=movielens_graph_signal graph=vknng miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=6.7065e-02 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=1.4573e-02 | t=0.1450s
    trss | MR=0.1 | seed=0 | MAE=1.8883e-02 | t=0.2242s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.4457e-01 | t=0.0165s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4379e-01 | t=19.0862s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0044s
    tikhonov | MR=0.1 | seed=1 | MAE=7.1622e-02 | t=0.0087s
    tv | MR=0.1 | seed=1 | MAE=1.9099e-02 | t=0.6126s
    trss | MR=0.1 | seed=1 | MAE=2.7907e-02 | t=0.2675s

Completed: 2026-04-16T13:23:58.614428+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.