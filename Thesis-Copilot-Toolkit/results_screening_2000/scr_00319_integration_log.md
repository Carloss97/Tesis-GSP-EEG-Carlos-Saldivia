# Integration Log: scr_00319
Started: 2026-04-16T15:32:24.877983+00:00
Description: Screening scr_00319 ds=iris_graph_signal graph=aew miss=3ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.0016s
    nearest | MR=3ch | seed=0 | MAE=5.1257e-01 | t=0.0028s
    tikhonov | MR=3ch | seed=0 | MAE=3.9902e-01 | t=0.0036s
    tv | MR=3ch | seed=0 | MAE=4.3067e-01 | t=0.1610s
    trss | MR=3ch | seed=0 | MAE=3.3560e-01 | t=0.0109s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.2801e-01 | t=0.0409s
    temporal_laplacian | MR=3ch | seed=0 | MAE=6.4035e-01 | t=16.0878s
    mean | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.0014s
    nearest | MR=3ch | seed=1 | MAE=5.3166e-01 | t=0.0029s
    tikhonov | MR=3ch | seed=1 | MAE=3.8074e-01 | t=0.0055s
    tv | MR=3ch | seed=1 | MAE=4.1242e-01 | t=0.4853s
    trss | MR=3ch | seed=1 | MAE=3.3084e-01 | t=0.0039s

Completed: 2026-04-16T15:32:24.880440+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.