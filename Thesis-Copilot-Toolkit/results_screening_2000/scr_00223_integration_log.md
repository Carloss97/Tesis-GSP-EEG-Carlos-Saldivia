# Integration Log: scr_00223
Started: 2026-04-16T14:40:18.709515+00:00
Description: Screening scr_00223 ds=iris_graph_signal graph=knn miss=3ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.0021s
    nearest | MR=3ch | seed=0 | MAE=5.1257e-01 | t=0.0037s
    tikhonov | MR=3ch | seed=0 | MAE=4.9340e-01 | t=0.0052s
    tv | MR=3ch | seed=0 | MAE=4.3487e-01 | t=0.1046s
    trss | MR=3ch | seed=0 | MAE=4.2982e-01 | t=0.0065s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=5.2316e-01 | t=0.0175s
    temporal_laplacian | MR=3ch | seed=0 | MAE=7.3884e-01 | t=7.4911s
    mean | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.0322s
    nearest | MR=3ch | seed=1 | MAE=5.3166e-01 | t=0.0058s
    tikhonov | MR=3ch | seed=1 | MAE=4.8595e-01 | t=0.0339s
    tv | MR=3ch | seed=1 | MAE=4.1969e-01 | t=0.1210s
    trss | MR=3ch | seed=1 | MAE=4.1913e-01 | t=0.0036s

Completed: 2026-04-16T14:40:18.710775+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.