# Integration Log: scr_00092
Started: 2026-04-16T14:59:30.460247+00:00
Description: Screening scr_00092 ds=movielens_graph_signal graph=vknng miss=1ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.0280s
    nearest | MR=1ch | seed=0 | MAE=1.9262e-02 | t=0.0048s
    tikhonov | MR=1ch | seed=0 | MAE=6.5919e-02 | t=0.0125s
    tv | MR=1ch | seed=0 | MAE=1.5667e-02 | t=0.3276s
    trss | MR=1ch | seed=0 | MAE=1.7849e-02 | t=0.1328s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.3821e-01 | t=0.0128s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.3967e-01 | t=21.1756s
    mean | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.0033s
    nearest | MR=1ch | seed=1 | MAE=1.7187e-02 | t=0.0390s
    tikhonov | MR=1ch | seed=1 | MAE=6.4939e-02 | t=0.0089s
    tv | MR=1ch | seed=1 | MAE=1.2803e-02 | t=0.8043s
    trss | MR=1ch | seed=1 | MAE=1.5842e-02 | t=0.2092s

Completed: 2026-04-16T14:59:30.493634+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.