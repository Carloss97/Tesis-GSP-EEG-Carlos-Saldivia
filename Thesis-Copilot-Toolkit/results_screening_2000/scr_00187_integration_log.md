# Integration Log: scr_00187
Started: 2026-04-16T14:22:04.010619+00:00
Description: Screening scr_00187 ds=iris_graph_signal graph=knng miss=2ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=2ch | seed=0 | MAE=2.7644e-01 | t=0.0019s
    nearest | MR=2ch | seed=0 | MAE=3.5475e-01 | t=0.0020s
    tikhonov | MR=2ch | seed=0 | MAE=3.0955e-01 | t=0.0034s
    tv | MR=2ch | seed=0 | MAE=2.7279e-01 | t=0.0908s
    trss | MR=2ch | seed=0 | MAE=2.3350e-01 | t=0.0037s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=3.9060e-01 | t=0.0078s
    temporal_laplacian | MR=2ch | seed=0 | MAE=5.8216e-01 | t=12.5044s
    mean | MR=2ch | seed=1 | MAE=2.5974e-01 | t=0.0017s
    nearest | MR=2ch | seed=1 | MAE=3.7471e-01 | t=0.0020s
    tikhonov | MR=2ch | seed=1 | MAE=3.0554e-01 | t=0.0351s
    tv | MR=2ch | seed=1 | MAE=2.6089e-01 | t=0.2743s
    trss | MR=2ch | seed=1 | MAE=2.2330e-01 | t=0.0038s

Completed: 2026-04-16T14:22:04.011333+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.