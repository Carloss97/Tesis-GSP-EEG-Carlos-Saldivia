# Integration Log: scr_00318
Started: 2026-04-16T15:31:37.363306+00:00
Description: Screening scr_00318 ds=iv100hz_mat graph=aew miss=3ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: aew built OK
    mean | MR=3ch | seed=0 | MAE=3.0766e+01 | t=0.0032s
    nearest | MR=3ch | seed=0 | MAE=4.8015e+01 | t=0.0065s
    tikhonov | MR=3ch | seed=0 | MAE=8.3616e+01 | t=0.0461s
    tv | MR=3ch | seed=0 | MAE=2.1388e+01 | t=0.4432s
    trss | MR=3ch | seed=0 | MAE=2.2122e+01 | t=0.4509s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.5554e+02 | t=0.0464s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.8998e+02 | t=17.5549s
    mean | MR=3ch | seed=1 | MAE=3.1144e+01 | t=0.0377s
    nearest | MR=3ch | seed=1 | MAE=4.9179e+01 | t=0.0419s
    tikhonov | MR=3ch | seed=1 | MAE=8.3785e+01 | t=0.0161s
    tv | MR=3ch | seed=1 | MAE=2.1103e+01 | t=0.7305s
    trss | MR=3ch | seed=1 | MAE=2.2833e+01 | t=0.4602s

Completed: 2026-04-16T15:31:37.364850+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.