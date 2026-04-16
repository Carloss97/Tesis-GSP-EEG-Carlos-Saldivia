# Integration Log: scr_00259
Started: 2026-04-16T14:58:38.244043+00:00
Description: Screening scr_00259 ds=iris_graph_signal graph=gaussian miss=3ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.0014s
    nearest | MR=3ch | seed=0 | MAE=5.1257e-01 | t=0.0025s
    tikhonov | MR=3ch | seed=0 | MAE=4.5408e-01 | t=0.0035s
    tv | MR=3ch | seed=0 | MAE=4.3500e-01 | t=0.1620s
    trss | MR=3ch | seed=0 | MAE=3.9495e-01 | t=0.0041s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.8776e-01 | t=0.0039s
    temporal_laplacian | MR=3ch | seed=0 | MAE=6.7779e-01 | t=11.3762s
    mean | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.0023s
    nearest | MR=3ch | seed=1 | MAE=5.3166e-01 | t=0.0695s
    tikhonov | MR=3ch | seed=1 | MAE=4.4057e-01 | t=0.0034s
    tv | MR=3ch | seed=1 | MAE=4.1961e-01 | t=0.2519s
    trss | MR=3ch | seed=1 | MAE=3.8020e-01 | t=0.0036s

Completed: 2026-04-16T14:58:38.245038+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.