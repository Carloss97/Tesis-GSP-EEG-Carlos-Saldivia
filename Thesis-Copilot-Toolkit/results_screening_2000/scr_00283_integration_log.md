# Integration Log: scr_00283
Started: 2026-04-16T15:11:06.090755+00:00
Description: Screening scr_00283 ds=iris_graph_signal graph=kalofolias miss=3ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.0014s
    nearest | MR=3ch | seed=0 | MAE=5.1257e-01 | t=0.0025s
    tikhonov | MR=3ch | seed=0 | MAE=5.7514e-01 | t=0.0036s
    tv | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.1845s
    trss | MR=3ch | seed=0 | MAE=3.7618e-01 | t=0.0313s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=5.5717e-01 | t=0.0038s
    temporal_laplacian | MR=3ch | seed=0 | MAE=8.4670e-01 | t=21.0276s
    mean | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.0014s
    nearest | MR=3ch | seed=1 | MAE=5.3166e-01 | t=0.0029s
    tikhonov | MR=3ch | seed=1 | MAE=5.7525e-01 | t=0.0589s
    tv | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.2568s
    trss | MR=3ch | seed=1 | MAE=3.5388e-01 | t=0.0058s

Completed: 2026-04-16T15:11:06.091499+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.