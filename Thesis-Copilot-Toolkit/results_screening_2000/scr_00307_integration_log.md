# Integration Log: scr_00307
Started: 2026-04-16T15:25:37.968543+00:00
Description: Screening scr_00307 ds=iris_graph_signal graph=vknng miss=3ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.0017s
    nearest | MR=3ch | seed=0 | MAE=5.1257e-01 | t=0.0025s
    tikhonov | MR=3ch | seed=0 | MAE=4.8135e-01 | t=0.0046s
    tv | MR=3ch | seed=0 | MAE=4.3452e-01 | t=0.2302s
    trss | MR=3ch | seed=0 | MAE=4.0411e-01 | t=0.0062s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=5.2111e-01 | t=0.0054s
    temporal_laplacian | MR=3ch | seed=0 | MAE=7.6657e-01 | t=16.3597s
    mean | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.0016s
    nearest | MR=3ch | seed=1 | MAE=5.3166e-01 | t=0.0206s
    tikhonov | MR=3ch | seed=1 | MAE=4.7129e-01 | t=0.0070s
    tv | MR=3ch | seed=1 | MAE=4.1929e-01 | t=0.5138s
    trss | MR=3ch | seed=1 | MAE=3.8858e-01 | t=0.0040s

Completed: 2026-04-16T15:25:37.969525+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.