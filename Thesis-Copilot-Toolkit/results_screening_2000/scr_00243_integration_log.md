# Integration Log: scr_00243
Started: 2026-04-16T14:49:23.741950+00:00
Description: Screening scr_00243 ds=bci_iv2a_real_s1 graph=knn miss=3ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k7 built OK
    mean | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=2.1144e-06 | t=0.0055s
    tikhonov | MR=3ch | seed=0 | MAE=7.3710e-06 | t=0.0087s
    tv | MR=3ch | seed=0 | MAE=1.8805e-06 | t=0.6788s
    trss | MR=3ch | seed=0 | MAE=1.2318e-06 | t=0.1095s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.1757e-05 | t=0.0411s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.7232e-05 | t=22.8450s
    mean | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.0681s
    nearest | MR=3ch | seed=1 | MAE=2.0591e-06 | t=0.0066s
    tikhonov | MR=3ch | seed=1 | MAE=7.3539e-06 | t=0.0313s
    tv | MR=3ch | seed=1 | MAE=1.9163e-06 | t=1.1287s
    trss | MR=3ch | seed=1 | MAE=1.2495e-06 | t=0.1628s

Completed: 2026-04-16T14:49:23.742845+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.