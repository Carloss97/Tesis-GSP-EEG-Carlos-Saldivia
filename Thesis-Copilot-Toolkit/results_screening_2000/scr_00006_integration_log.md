# Integration Log: scr_00006
Started: 2026-04-16T15:19:13.104415+00:00
Description: Screening scr_00006 ds=iv100hz_mat graph=knn miss=1ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=1.1091e+01 | t=0.0378s
    nearest | MR=1ch | seed=0 | MAE=1.6962e+01 | t=0.0033s
    tikhonov | MR=1ch | seed=0 | MAE=7.4768e+01 | t=0.0751s
    tv | MR=1ch | seed=0 | MAE=8.7583e+00 | t=0.7999s
    trss | MR=1ch | seed=0 | MAE=8.2021e+00 | t=0.1222s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.5444e+02 | t=0.0776s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.9163e+02 | t=31.3400s
    mean | MR=1ch | seed=1 | MAE=1.0242e+01 | t=0.0031s
    nearest | MR=1ch | seed=1 | MAE=1.6572e+01 | t=0.0030s
    tikhonov | MR=1ch | seed=1 | MAE=7.4690e+01 | t=0.0595s
    tv | MR=1ch | seed=1 | MAE=8.7711e+00 | t=0.6815s
    trss | MR=1ch | seed=1 | MAE=8.0440e+00 | t=0.9139s

Completed: 2026-04-16T15:19:13.105357+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.