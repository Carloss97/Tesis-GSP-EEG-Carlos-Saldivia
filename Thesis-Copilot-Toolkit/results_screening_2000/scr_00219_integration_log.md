# Integration Log: scr_00219
Started: 2026-04-16T14:37:05.560774+00:00
Description: Screening scr_00219 ds=bci_iv2a_real_s1 graph=knn miss=3ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k3 built OK
    mean | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.0020s
    nearest | MR=3ch | seed=0 | MAE=2.1144e-06 | t=0.0055s
    tikhonov | MR=3ch | seed=0 | MAE=5.0227e-06 | t=0.0686s
    tv | MR=3ch | seed=0 | MAE=1.8806e-06 | t=0.5655s
    trss | MR=3ch | seed=0 | MAE=1.3070e-06 | t=0.3656s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=9.6196e-06 | t=0.0124s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.4550e-05 | t=23.6247s
    mean | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.0021s
    nearest | MR=3ch | seed=1 | MAE=2.0591e-06 | t=0.0037s
    tikhonov | MR=3ch | seed=1 | MAE=5.0292e-06 | t=0.0059s
    tv | MR=3ch | seed=1 | MAE=1.9163e-06 | t=0.2853s
    trss | MR=3ch | seed=1 | MAE=1.3195e-06 | t=0.3839s

Completed: 2026-04-16T14:37:05.561728+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.