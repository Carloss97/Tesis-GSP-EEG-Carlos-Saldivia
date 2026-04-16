# Integration Log: scr_00284
Started: 2026-04-16T15:12:00.020193+00:00
Description: Screening scr_00284 ds=movielens_graph_signal graph=kalofolias miss=3ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=1.8112e-02 | t=0.0062s
    tikhonov | MR=3ch | seed=0 | MAE=2.0600e-01 | t=0.0087s
    tv | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.2550s
    trss | MR=3ch | seed=0 | MAE=3.9493e-02 | t=0.1755s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.0167e-01 | t=0.0459s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.8133e-01 | t=23.0284s
    mean | MR=3ch | seed=1 | MAE=2.1784e-02 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=1.9343e-02 | t=0.0358s
    tikhonov | MR=3ch | seed=1 | MAE=2.0878e-01 | t=0.0090s
    tv | MR=3ch | seed=1 | MAE=2.1784e-02 | t=1.1062s
    trss | MR=3ch | seed=1 | MAE=3.7568e-02 | t=0.4004s

Completed: 2026-04-16T15:12:00.021082+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.