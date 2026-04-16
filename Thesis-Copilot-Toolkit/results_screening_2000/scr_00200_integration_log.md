# Integration Log: scr_00200
Started: 2026-04-16T14:29:16.449841+00:00
Description: Screening scr_00200 ds=movielens_graph_signal graph=vknng miss=2ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.0031s
    nearest | MR=2ch | seed=0 | MAE=1.3191e-02 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=6.7065e-02 | t=0.0090s
    tv | MR=2ch | seed=0 | MAE=1.4573e-02 | t=0.3902s
    trss | MR=2ch | seed=0 | MAE=1.8883e-02 | t=0.3334s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.4457e-01 | t=0.0127s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.4379e-01 | t=24.2581s
    mean | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.1033s
    nearest | MR=2ch | seed=1 | MAE=2.1272e-02 | t=0.0042s
    tikhonov | MR=2ch | seed=1 | MAE=7.1622e-02 | t=0.0089s
    tv | MR=2ch | seed=1 | MAE=1.9099e-02 | t=0.3916s
    trss | MR=2ch | seed=1 | MAE=2.7907e-02 | t=1.3647s

Completed: 2026-04-16T14:29:16.450735+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.