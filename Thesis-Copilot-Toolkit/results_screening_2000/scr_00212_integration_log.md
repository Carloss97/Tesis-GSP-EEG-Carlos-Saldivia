# Integration Log: scr_00212
Started: 2026-04-16T14:35:14.428821+00:00
Description: Screening scr_00212 ds=movielens_graph_signal graph=aew miss=2ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.0029s
    nearest | MR=2ch | seed=0 | MAE=1.3191e-02 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=2.2943e-02 | t=0.0088s
    tv | MR=2ch | seed=0 | MAE=1.4559e-02 | t=0.2714s
    trss | MR=2ch | seed=0 | MAE=1.7240e-02 | t=0.0157s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=7.8101e-02 | t=0.0086s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.0919e-01 | t=30.2791s
    mean | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.0036s
    nearest | MR=2ch | seed=1 | MAE=2.1272e-02 | t=0.0058s
    tikhonov | MR=2ch | seed=1 | MAE=3.0653e-02 | t=0.0059s
    tv | MR=2ch | seed=1 | MAE=1.9397e-02 | t=0.1546s
    trss | MR=2ch | seed=1 | MAE=2.5813e-02 | t=0.0166s

Completed: 2026-04-16T14:35:14.429707+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.