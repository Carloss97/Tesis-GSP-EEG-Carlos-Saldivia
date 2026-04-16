# Integration Log: scr_00127
Started: 2026-04-16T15:16:30.161128+00:00
Description: Screening scr_00127 ds=iris_graph_signal graph=knn miss=2ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=2ch | seed=0 | MAE=2.7644e-01 | t=0.0018s
    nearest | MR=2ch | seed=0 | MAE=3.5475e-01 | t=0.0046s
    tikhonov | MR=2ch | seed=0 | MAE=3.6513e-01 | t=0.0038s
    tv | MR=2ch | seed=0 | MAE=2.7676e-01 | t=0.2162s
    trss | MR=2ch | seed=0 | MAE=2.3848e-01 | t=0.0037s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.5934e-01 | t=0.0042s
    temporal_laplacian | MR=2ch | seed=0 | MAE=7.0364e-01 | t=15.0497s
    mean | MR=2ch | seed=1 | MAE=2.5974e-01 | t=0.0203s
    nearest | MR=2ch | seed=1 | MAE=3.7471e-01 | t=0.0020s
    tikhonov | MR=2ch | seed=1 | MAE=3.6275e-01 | t=0.0055s
    tv | MR=2ch | seed=1 | MAE=2.5927e-01 | t=0.0823s
    trss | MR=2ch | seed=1 | MAE=2.1786e-01 | t=0.0042s

Completed: 2026-04-16T15:16:30.162024+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.