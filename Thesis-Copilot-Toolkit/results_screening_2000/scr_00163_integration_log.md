# Integration Log: scr_00163
Started: 2026-04-16T15:36:13.739121+00:00
Description: Screening scr_00163 ds=iris_graph_signal graph=gaussian miss=2ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=2ch | seed=0 | MAE=2.7644e-01 | t=0.0016s
    nearest | MR=2ch | seed=0 | MAE=3.5475e-01 | t=0.0287s
    tikhonov | MR=2ch | seed=0 | MAE=2.8845e-01 | t=0.0099s
    tv | MR=2ch | seed=0 | MAE=2.7070e-01 | t=0.2243s
    trss | MR=2ch | seed=0 | MAE=2.5538e-01 | t=0.0080s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=3.2490e-01 | t=0.0041s
    temporal_laplacian | MR=2ch | seed=0 | MAE=4.5295e-01 | t=3.0164s
    mean | MR=2ch | seed=1 | MAE=2.5974e-01 | t=0.0068s
    nearest | MR=2ch | seed=1 | MAE=3.7471e-01 | t=0.0044s
    tikhonov | MR=2ch | seed=1 | MAE=2.8703e-01 | t=0.0041s
    tv | MR=2ch | seed=1 | MAE=2.5923e-01 | t=0.1364s
    trss | MR=2ch | seed=1 | MAE=2.4612e-01 | t=0.0039s

Completed: 2026-04-16T15:36:13.740110+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.