# Integration Log: scr_00644
Started: 2026-04-16T14:58:57.885203+00:00
Description: Screening scr_00644 ds=movielens_graph_signal graph=aew miss=[0.3] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=6.7099e-02 | t=0.0102s
    tikhonov | MR=0.3 | seed=0 | MAE=6.8349e-02 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=6.2757e-02 | t=0.8247s
    trss | MR=0.3 | seed=0 | MAE=6.9478e-02 | t=0.6367s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.0716e-01 | t=0.0428s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.3005e-01 | t=25.3207s
    mean | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.0030s
    nearest | MR=0.3 | seed=1 | MAE=6.3035e-02 | t=0.0233s
    tikhonov | MR=0.3 | seed=1 | MAE=7.1828e-02 | t=0.0116s
    tv | MR=0.3 | seed=1 | MAE=6.5228e-02 | t=0.2871s
    trss | MR=0.3 | seed=1 | MAE=7.2438e-02 | t=0.0620s

Completed: 2026-04-16T14:58:57.886212+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.