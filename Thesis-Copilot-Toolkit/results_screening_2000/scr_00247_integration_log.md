# Integration Log: scr_00247
Started: 2026-04-16T14:52:47.370296+00:00
Description: Screening scr_00247 ds=iris_graph_signal graph=knn miss=3ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.0014s
    nearest | MR=3ch | seed=0 | MAE=5.1257e-01 | t=0.0071s
    tikhonov | MR=3ch | seed=0 | MAE=4.8135e-01 | t=0.0046s
    tv | MR=3ch | seed=0 | MAE=4.3452e-01 | t=0.2134s
    trss | MR=3ch | seed=0 | MAE=4.0411e-01 | t=0.0280s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=5.2111e-01 | t=0.0115s
    temporal_laplacian | MR=3ch | seed=0 | MAE=7.6657e-01 | t=11.9185s
    mean | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.0176s
    nearest | MR=3ch | seed=1 | MAE=5.3166e-01 | t=0.0025s
    tikhonov | MR=3ch | seed=1 | MAE=4.7129e-01 | t=0.0035s
    tv | MR=3ch | seed=1 | MAE=4.1929e-01 | t=0.1232s
    trss | MR=3ch | seed=1 | MAE=3.8858e-01 | t=0.0363s

Completed: 2026-04-16T14:52:47.371563+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.