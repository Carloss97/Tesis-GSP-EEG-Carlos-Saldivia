# Integration Log: scr_00368
Started: 2026-04-16T13:10:01.562882+00:00
Description: Screening scr_00368 ds=movielens_graph_signal graph=gaussian miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0036s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0027s
    tikhonov | MR=0.1 | seed=0 | MAE=1.1244e-01 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.1890s
    trss | MR=0.1 | seed=0 | MAE=1.9136e-02 | t=0.0177s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.7704e-01 | t=0.0192s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.5397e-01 | t=7.7755s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=1.1240e-01 | t=0.0059s
    tv | MR=0.1 | seed=1 | MAE=1.9049e-02 | t=0.2125s
    trss | MR=0.1 | seed=1 | MAE=2.4474e-02 | t=0.1199s

Completed: 2026-04-16T13:10:01.563737+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.