# Integration Log: scr_00068
Started: 2026-04-16T14:47:53.341181+00:00
Description: Screening scr_00068 ds=movielens_graph_signal graph=kalofolias miss=1ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.0030s
    nearest | MR=1ch | seed=0 | MAE=1.9262e-02 | t=0.0032s
    tikhonov | MR=1ch | seed=0 | MAE=1.9572e-01 | t=0.0087s
    tv | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.8673s
    trss | MR=1ch | seed=0 | MAE=2.1328e-02 | t=0.5683s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.9189e-01 | t=0.0777s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.7239e-01 | t=28.0803s
    mean | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.0030s
    nearest | MR=1ch | seed=1 | MAE=1.7187e-02 | t=0.0036s
    tikhonov | MR=1ch | seed=1 | MAE=1.9841e-01 | t=0.0087s
    tv | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.5366s
    trss | MR=1ch | seed=1 | MAE=1.8338e-02 | t=0.3967s

Completed: 2026-04-16T14:47:53.342106+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.