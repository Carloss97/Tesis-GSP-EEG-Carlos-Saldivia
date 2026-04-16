# Integration Log: scr_00235
Started: 2026-04-16T14:46:47.792852+00:00
Description: Screening scr_00235 ds=iris_graph_signal graph=knn miss=3ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.0015s
    nearest | MR=3ch | seed=0 | MAE=5.1257e-01 | t=0.0626s
    tikhonov | MR=3ch | seed=0 | MAE=4.8135e-01 | t=0.0105s
    tv | MR=3ch | seed=0 | MAE=4.3452e-01 | t=0.1152s
    trss | MR=3ch | seed=0 | MAE=4.0411e-01 | t=0.0036s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=5.2111e-01 | t=0.0039s
    temporal_laplacian | MR=3ch | seed=0 | MAE=7.6657e-01 | t=15.9073s
    mean | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.0014s
    nearest | MR=3ch | seed=1 | MAE=5.3166e-01 | t=0.0357s
    tikhonov | MR=3ch | seed=1 | MAE=4.7129e-01 | t=0.0392s
    tv | MR=3ch | seed=1 | MAE=4.1929e-01 | t=0.1903s
    trss | MR=3ch | seed=1 | MAE=3.8858e-01 | t=0.0038s

Completed: 2026-04-16T14:46:47.793810+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.