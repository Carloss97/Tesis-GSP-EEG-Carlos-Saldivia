# Integration Log: scr_00234
Started: 2026-04-16T14:46:11.870473+00:00
Description: Screening scr_00234 ds=iv100hz_mat graph=knn miss=3ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k5 built OK
    mean | MR=3ch | seed=0 | MAE=3.0766e+01 | t=0.0033s
    nearest | MR=3ch | seed=0 | MAE=4.8015e+01 | t=0.0065s
    tikhonov | MR=3ch | seed=0 | MAE=1.1287e+02 | t=0.0101s
    tv | MR=3ch | seed=0 | MAE=2.2479e+01 | t=0.3844s
    trss | MR=3ch | seed=0 | MAE=2.4196e+01 | t=0.2736s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.8572e+02 | t=0.0111s
    temporal_laplacian | MR=3ch | seed=0 | MAE=2.1711e+02 | t=28.1500s
    mean | MR=3ch | seed=1 | MAE=3.1144e+01 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=4.9179e+01 | t=0.0060s
    tikhonov | MR=3ch | seed=1 | MAE=1.1259e+02 | t=0.0351s
    tv | MR=3ch | seed=1 | MAE=2.3246e+01 | t=0.5257s
    trss | MR=3ch | seed=1 | MAE=2.4294e+01 | t=0.0860s

Completed: 2026-04-16T14:46:11.871665+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.