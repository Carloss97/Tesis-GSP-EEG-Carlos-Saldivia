# Integration Log: scr_00295
Started: 2026-04-16T15:18:16.499254+00:00
Description: Screening scr_00295 ds=iris_graph_signal graph=knng miss=3ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=3ch | seed=0 | MAE=4.3446e-01 | t=0.0016s
    nearest | MR=3ch | seed=0 | MAE=5.1257e-01 | t=0.0026s
    tikhonov | MR=3ch | seed=0 | MAE=4.5408e-01 | t=0.0036s
    tv | MR=3ch | seed=0 | MAE=4.3500e-01 | t=0.3329s
    trss | MR=3ch | seed=0 | MAE=3.9495e-01 | t=0.0050s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.8776e-01 | t=0.0041s
    temporal_laplacian | MR=3ch | seed=0 | MAE=6.7779e-01 | t=15.4459s
    mean | MR=3ch | seed=1 | MAE=4.1932e-01 | t=0.0017s
    nearest | MR=3ch | seed=1 | MAE=5.3166e-01 | t=0.0071s
    tikhonov | MR=3ch | seed=1 | MAE=4.4057e-01 | t=0.0048s
    tv | MR=3ch | seed=1 | MAE=4.1961e-01 | t=0.1300s
    trss | MR=3ch | seed=1 | MAE=3.8020e-01 | t=0.0039s

Completed: 2026-04-16T15:18:16.500153+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.