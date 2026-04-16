# Integration Log: scr_00246
Started: 2026-04-16T14:52:17.834393+00:00
Description: Screening scr_00246 ds=iv100hz_mat graph=knn miss=3ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k7 built OK
    mean | MR=3ch | seed=0 | MAE=3.0766e+01 | t=0.0137s
    nearest | MR=3ch | seed=0 | MAE=4.8015e+01 | t=0.0069s
    tikhonov | MR=3ch | seed=0 | MAE=1.2516e+02 | t=0.0405s
    tv | MR=3ch | seed=0 | MAE=2.2421e+01 | t=0.4643s
    trss | MR=3ch | seed=0 | MAE=2.3070e+01 | t=0.4281s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.9603e+02 | t=0.0166s
    temporal_laplacian | MR=3ch | seed=0 | MAE=2.3694e+02 | t=18.5626s
    mean | MR=3ch | seed=1 | MAE=3.1144e+01 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=4.9179e+01 | t=0.1858s
    tikhonov | MR=3ch | seed=1 | MAE=1.2502e+02 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=2.2818e+01 | t=0.7668s
    trss | MR=3ch | seed=1 | MAE=2.3127e+01 | t=0.5059s

Completed: 2026-04-16T14:52:17.835290+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.