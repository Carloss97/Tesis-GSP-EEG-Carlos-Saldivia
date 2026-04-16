# Integration Log: scr_00222
Started: 2026-04-16T14:39:52.925244+00:00
Description: Screening scr_00222 ds=iv100hz_mat graph=knn miss=3ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k3 built OK
    mean | MR=3ch | seed=0 | MAE=3.0766e+01 | t=0.0037s
    nearest | MR=3ch | seed=0 | MAE=4.8015e+01 | t=0.0060s
    tikhonov | MR=3ch | seed=0 | MAE=9.1917e+01 | t=0.0135s
    tv | MR=3ch | seed=0 | MAE=2.8677e+01 | t=0.3414s
    trss | MR=3ch | seed=0 | MAE=2.4730e+01 | t=0.2475s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.6305e+02 | t=0.0126s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.9785e+02 | t=21.3288s
    mean | MR=3ch | seed=1 | MAE=3.1144e+01 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=4.9179e+01 | t=0.0239s
    tikhonov | MR=3ch | seed=1 | MAE=9.1776e+01 | t=0.0090s
    tv | MR=3ch | seed=1 | MAE=2.8052e+01 | t=0.3410s
    trss | MR=3ch | seed=1 | MAE=2.5037e+01 | t=0.2238s

Completed: 2026-04-16T14:39:52.926510+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.