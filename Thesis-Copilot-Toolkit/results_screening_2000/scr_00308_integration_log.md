# Integration Log: scr_00308
Started: 2026-04-16T15:26:26.989483+00:00
Description: Screening scr_00308 ds=movielens_graph_signal graph=vknng miss=3ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.0034s
    nearest | MR=3ch | seed=0 | MAE=1.8112e-02 | t=0.0588s
    tikhonov | MR=3ch | seed=0 | MAE=7.1303e-02 | t=0.0106s
    tv | MR=3ch | seed=0 | MAE=2.3320e-02 | t=0.8198s
    trss | MR=3ch | seed=0 | MAE=2.8823e-02 | t=0.1500s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.4515e-01 | t=0.0665s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.4694e-01 | t=16.6998s
    mean | MR=3ch | seed=1 | MAE=2.1784e-02 | t=0.0048s
    nearest | MR=3ch | seed=1 | MAE=1.9343e-02 | t=0.0064s
    tikhonov | MR=3ch | seed=1 | MAE=7.4887e-02 | t=0.0840s
    tv | MR=3ch | seed=1 | MAE=2.1854e-02 | t=0.6659s
    trss | MR=3ch | seed=1 | MAE=3.1125e-02 | t=0.3263s

Completed: 2026-04-16T15:26:26.991579+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.