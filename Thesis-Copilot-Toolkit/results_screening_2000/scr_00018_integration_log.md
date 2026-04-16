# Integration Log: scr_00018
Started: 2026-04-16T15:25:43.952720+00:00
Description: Screening scr_00018 ds=iv100hz_mat graph=knn miss=1ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k5 built OK
    mean | MR=1ch | seed=0 | MAE=1.1091e+01 | t=0.0039s
    nearest | MR=1ch | seed=0 | MAE=1.6962e+01 | t=0.0042s
    tikhonov | MR=1ch | seed=0 | MAE=9.8743e+01 | t=0.0088s
    tv | MR=1ch | seed=0 | MAE=7.9368e+00 | t=0.2843s
    trss | MR=1ch | seed=0 | MAE=7.9486e+00 | t=0.3263s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.8007e+02 | t=0.0176s
    temporal_laplacian | MR=1ch | seed=0 | MAE=2.1133e+02 | t=22.5856s
    mean | MR=1ch | seed=1 | MAE=1.0242e+01 | t=0.0033s
    nearest | MR=1ch | seed=1 | MAE=1.6572e+01 | t=0.0047s
    tikhonov | MR=1ch | seed=1 | MAE=9.8621e+01 | t=0.0225s
    tv | MR=1ch | seed=1 | MAE=7.4958e+00 | t=0.9324s
    trss | MR=1ch | seed=1 | MAE=7.8128e+00 | t=0.2403s

Completed: 2026-04-16T15:25:43.954055+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.