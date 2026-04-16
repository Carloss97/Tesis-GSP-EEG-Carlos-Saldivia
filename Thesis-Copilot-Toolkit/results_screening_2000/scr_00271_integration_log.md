# Integration Log: scr_00271
Started: 2026-04-16T15:05:05.732417+00:00
Description: Screening scr_00271 ds=iris_graph_signal graph=gaussian miss=3ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.0014s
    nearest | MR=3ch | seed=0 | MAE=5.1257e-01 | t=0.0062s
    tikhonov | MR=3ch | seed=0 | MAE=4.4096e-01 | t=0.0036s
    tv | MR=3ch | seed=0 | MAE=4.4176e-01 | t=0.1733s
    trss | MR=3ch | seed=0 | MAE=4.2191e-01 | t=0.0101s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.5284e-01 | t=0.0040s
    temporal_laplacian | MR=3ch | seed=0 | MAE=5.5615e-01 | t=13.7588s
    mean | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.0019s
    nearest | MR=3ch | seed=1 | MAE=5.3166e-01 | t=0.0343s
    tikhonov | MR=3ch | seed=1 | MAE=4.2606e-01 | t=0.0671s
    tv | MR=3ch | seed=1 | MAE=4.2520e-01 | t=0.1637s
    trss | MR=3ch | seed=1 | MAE=4.2325e-01 | t=0.0038s

Completed: 2026-04-16T15:05:05.733564+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.