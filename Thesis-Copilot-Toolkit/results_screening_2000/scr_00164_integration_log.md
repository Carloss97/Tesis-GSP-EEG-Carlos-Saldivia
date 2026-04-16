# Integration Log: scr_00164
Started: 2026-04-16T15:37:28.700157+00:00
Description: Screening scr_00164 ds=movielens_graph_signal graph=gaussian miss=2ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.0677s
    nearest | MR=2ch | seed=0 | MAE=1.3191e-02 | t=0.0082s
    tikhonov | MR=2ch | seed=0 | MAE=7.9446e-02 | t=0.0496s
    tv | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.5926s
    trss | MR=2ch | seed=0 | MAE=1.9530e-02 | t=0.0250s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.5675e-01 | t=0.0090s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.4374e-01 | t=37.6156s
    mean | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=2.1272e-02 | t=0.0044s
    tikhonov | MR=2ch | seed=1 | MAE=8.1704e-02 | t=0.0554s
    tv | MR=2ch | seed=1 | MAE=1.9061e-02 | t=0.6605s
    trss | MR=2ch | seed=1 | MAE=2.5699e-02 | t=0.1519s

Completed: 2026-04-16T15:37:28.701517+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.