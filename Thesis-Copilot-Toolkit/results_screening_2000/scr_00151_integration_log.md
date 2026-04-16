# Integration Log: scr_00151
Started: 2026-04-16T15:30:29.824264+00:00
Description: Screening scr_00151 ds=iris_graph_signal graph=gaussian miss=2ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=2ch | seed=0 | MAE=2.7644e-01 | t=0.0021s
    nearest | MR=2ch | seed=0 | MAE=3.5475e-01 | t=0.0031s
    tikhonov | MR=2ch | seed=0 | MAE=3.0955e-01 | t=0.0276s
    tv | MR=2ch | seed=0 | MAE=2.7279e-01 | t=0.1559s
    trss | MR=2ch | seed=0 | MAE=2.3350e-01 | t=0.0046s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=3.9060e-01 | t=0.0066s
    temporal_laplacian | MR=2ch | seed=0 | MAE=5.8216e-01 | t=12.6485s
    mean | MR=2ch | seed=1 | MAE=2.5974e-01 | t=0.0015s
    nearest | MR=2ch | seed=1 | MAE=3.7471e-01 | t=0.0042s
    tikhonov | MR=2ch | seed=1 | MAE=3.0554e-01 | t=0.0039s
    tv | MR=2ch | seed=1 | MAE=2.6089e-01 | t=0.2468s
    trss | MR=2ch | seed=1 | MAE=2.2330e-01 | t=0.0038s

Completed: 2026-04-16T15:30:29.825225+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.