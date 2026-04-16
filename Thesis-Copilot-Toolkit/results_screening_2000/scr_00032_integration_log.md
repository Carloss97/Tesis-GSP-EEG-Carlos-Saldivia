# Integration Log: scr_00032
Started: 2026-04-16T15:33:16.840118+00:00
Description: Screening scr_00032 ds=movielens_graph_signal graph=knn miss=1ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.0084s
    nearest | MR=1ch | seed=0 | MAE=1.9262e-02 | t=0.0114s
    tikhonov | MR=1ch | seed=0 | MAE=9.1541e-02 | t=0.0159s
    tv | MR=1ch | seed=0 | MAE=1.5667e-02 | t=0.4095s
    trss | MR=1ch | seed=0 | MAE=1.7740e-02 | t=0.0609s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.5826e-01 | t=0.0588s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.4732e-01 | t=20.4330s
    mean | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.0106s
    nearest | MR=1ch | seed=1 | MAE=1.7187e-02 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=9.1250e-02 | t=0.0278s
    tv | MR=1ch | seed=1 | MAE=1.2783e-02 | t=0.5827s
    trss | MR=1ch | seed=1 | MAE=1.5725e-02 | t=0.1945s

Completed: 2026-04-16T15:33:16.843802+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.