# Integration Log: scr_00020
Started: 2026-04-16T15:26:52.997605+00:00
Description: Screening scr_00020 ds=movielens_graph_signal graph=knn miss=1ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.0041s
    nearest | MR=1ch | seed=0 | MAE=1.9262e-02 | t=0.0072s
    tikhonov | MR=1ch | seed=0 | MAE=7.6408e-02 | t=0.0088s
    tv | MR=1ch | seed=0 | MAE=1.5668e-02 | t=0.8996s
    trss | MR=1ch | seed=0 | MAE=1.7415e-02 | t=0.2657s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.4758e-01 | t=0.0672s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.4393e-01 | t=12.0172s
    mean | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.0030s
    nearest | MR=1ch | seed=1 | MAE=1.7187e-02 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=7.5853e-02 | t=0.0264s
    tv | MR=1ch | seed=1 | MAE=1.2788e-02 | t=0.5577s
    trss | MR=1ch | seed=1 | MAE=1.6145e-02 | t=0.1546s

Completed: 2026-04-16T15:26:52.999058+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.