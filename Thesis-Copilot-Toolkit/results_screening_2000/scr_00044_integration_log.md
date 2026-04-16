# Integration Log: scr_00044
Started: 2026-04-16T15:39:13.506843+00:00
Description: Screening scr_00044 ds=movielens_graph_signal graph=gaussian miss=1ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.0301s
    nearest | MR=1ch | seed=0 | MAE=1.9262e-02 | t=0.0034s
    tikhonov | MR=1ch | seed=0 | MAE=1.0782e-01 | t=0.0121s
    tv | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.6160s
    trss | MR=1ch | seed=0 | MAE=1.7477e-02 | t=0.0328s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.6800e-01 | t=0.0210s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.5001e-01 | t=21.2396s
    mean | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.0534s
    nearest | MR=1ch | seed=1 | MAE=1.7187e-02 | t=0.0034s
    tikhonov | MR=1ch | seed=1 | MAE=1.0797e-01 | t=0.0280s
    tv | MR=1ch | seed=1 | MAE=1.2779e-02 | t=0.6487s
    trss | MR=1ch | seed=1 | MAE=1.5183e-02 | t=0.4026s

Completed: 2026-04-16T15:39:13.509413+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.