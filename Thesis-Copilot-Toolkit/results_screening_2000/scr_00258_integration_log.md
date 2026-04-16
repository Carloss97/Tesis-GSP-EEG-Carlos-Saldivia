# Integration Log: scr_00258
Started: 2026-04-16T14:58:13.505547+00:00
Description: Screening scr_00258 ds=iv100hz_mat graph=gaussian miss=3ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=3ch | seed=0 | MAE=3.0766e+01 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=4.8015e+01 | t=0.0055s
    tikhonov | MR=3ch | seed=0 | MAE=1.3951e+02 | t=0.0088s
    tv | MR=3ch | seed=0 | MAE=1.9279e+01 | t=0.8586s
    trss | MR=3ch | seed=0 | MAE=2.1688e+01 | t=0.8329s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.0644e+02 | t=0.1340s
    temporal_laplacian | MR=3ch | seed=0 | MAE=2.6809e+02 | t=11.9896s
    mean | MR=3ch | seed=1 | MAE=3.1144e+01 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=4.9179e+01 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=1.3951e+02 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=1.7661e+01 | t=1.0229s
    trss | MR=3ch | seed=1 | MAE=2.1883e+01 | t=0.4243s

Completed: 2026-04-16T14:58:13.506520+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.