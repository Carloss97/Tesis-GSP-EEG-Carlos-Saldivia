# Integration Log: scr_00220
Started: 2026-04-16T14:37:59.479964+00:00
Description: Screening scr_00220 ds=bci_iv2a_real_s2 graph=knn miss=3ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k3 built OK
    mean | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.0048s
    nearest | MR=3ch | seed=0 | MAE=5.1829e-07 | t=0.0056s
    tikhonov | MR=3ch | seed=0 | MAE=1.5283e-06 | t=0.0098s
    tv | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.4527s
    trss | MR=3ch | seed=0 | MAE=4.5423e-07 | t=0.6569s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.6140e-06 | t=0.0124s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.2711e-05 | t=18.1475s
    mean | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.0026s
    nearest | MR=3ch | seed=1 | MAE=4.9473e-07 | t=0.0038s
    tikhonov | MR=3ch | seed=1 | MAE=1.5279e-06 | t=0.0060s
    tv | MR=3ch | seed=1 | MAE=5.2911e-07 | t=0.2731s
    trss | MR=3ch | seed=1 | MAE=4.5335e-07 | t=0.1865s

Completed: 2026-04-16T14:37:59.480859+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.