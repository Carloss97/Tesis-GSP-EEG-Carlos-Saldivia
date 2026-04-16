# Integration Log: scr_00199
Started: 2026-04-16T14:28:22.315912+00:00
Description: Screening scr_00199 ds=iris_graph_signal graph=vknng miss=2ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: vknng built OK
    mean | MR=2ch | seed=0 | MAE=2.7644e-01 | t=0.0619s
    nearest | MR=2ch | seed=0 | MAE=3.5475e-01 | t=0.0334s
    tikhonov | MR=2ch | seed=0 | MAE=3.6513e-01 | t=0.0072s
    tv | MR=2ch | seed=0 | MAE=2.7676e-01 | t=0.1493s
    trss | MR=2ch | seed=0 | MAE=2.3848e-01 | t=0.0038s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.5934e-01 | t=0.0372s
    temporal_laplacian | MR=2ch | seed=0 | MAE=7.0364e-01 | t=18.4005s
    mean | MR=2ch | seed=1 | MAE=2.5974e-01 | t=0.0014s
    nearest | MR=2ch | seed=1 | MAE=3.7471e-01 | t=0.0023s
    tikhonov | MR=2ch | seed=1 | MAE=3.6275e-01 | t=0.0046s
    tv | MR=2ch | seed=1 | MAE=2.5927e-01 | t=0.2710s
    trss | MR=2ch | seed=1 | MAE=2.1786e-01 | t=0.1029s

Completed: 2026-04-16T14:28:22.316833+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.