# Integration Log: scr_00248
Started: 2026-04-16T14:53:38.767478+00:00
Description: Screening scr_00248 ds=movielens_graph_signal graph=knn miss=3ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.0031s
    nearest | MR=3ch | seed=0 | MAE=1.8112e-02 | t=0.0207s
    tikhonov | MR=3ch | seed=0 | MAE=9.8647e-02 | t=0.0127s
    tv | MR=3ch | seed=0 | MAE=2.3378e-02 | t=0.2026s
    trss | MR=3ch | seed=0 | MAE=3.0048e-02 | t=0.0169s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.6656e-01 | t=0.0083s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.5426e-01 | t=24.0661s
    mean | MR=3ch | seed=1 | MAE=2.1784e-02 | t=0.0454s
    nearest | MR=3ch | seed=1 | MAE=1.9343e-02 | t=0.0062s
    tikhonov | MR=3ch | seed=1 | MAE=1.0119e-01 | t=0.0105s
    tv | MR=3ch | seed=1 | MAE=2.1798e-02 | t=0.7807s
    trss | MR=3ch | seed=1 | MAE=3.1391e-02 | t=0.1766s

Completed: 2026-04-16T14:53:38.768549+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.