# Integration Log: scr_00232
Started: 2026-04-16T14:44:15.143168+00:00
Description: Screening scr_00232 ds=bci_iv2a_real_s2 graph=knn miss=3ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k5 built OK
    mean | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.0350s
    nearest | MR=3ch | seed=0 | MAE=5.1829e-07 | t=0.0054s
    tikhonov | MR=3ch | seed=0 | MAE=1.9308e-06 | t=0.0087s
    tv | MR=3ch | seed=0 | MAE=5.2947e-07 | t=0.2157s
    trss | MR=3ch | seed=0 | MAE=4.2957e-07 | t=0.0181s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.8758e-06 | t=0.0122s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.4539e-05 | t=26.4715s
    mean | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=4.9473e-07 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=1.9328e-06 | t=0.0241s
    tv | MR=3ch | seed=1 | MAE=5.2911e-07 | t=0.4713s
    trss | MR=3ch | seed=1 | MAE=4.2931e-07 | t=0.2688s

Completed: 2026-04-16T14:44:15.144159+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.