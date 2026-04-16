# Integration Log: scr_00015
Started: 2026-04-16T15:22:31.564895+00:00
Description: Screening scr_00015 ds=bci_iv2a_real_s1 graph=knn miss=1ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k5 built OK
    mean | MR=1ch | seed=0 | MAE=6.8694e-07 | t=0.0195s
    nearest | MR=1ch | seed=0 | MAE=6.7972e-07 | t=0.0030s
    tikhonov | MR=1ch | seed=0 | MAE=5.6068e-06 | t=0.0276s
    tv | MR=1ch | seed=0 | MAE=6.8692e-07 | t=0.7976s
    trss | MR=1ch | seed=0 | MAE=4.6766e-07 | t=0.1665s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.0569e-05 | t=0.0609s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.5860e-05 | t=9.5184s
    mean | MR=1ch | seed=1 | MAE=6.0230e-07 | t=0.0073s
    nearest | MR=1ch | seed=1 | MAE=6.3859e-07 | t=0.0039s
    tikhonov | MR=1ch | seed=1 | MAE=5.5712e-06 | t=0.0086s
    tv | MR=1ch | seed=1 | MAE=6.0227e-07 | t=0.2858s
    trss | MR=1ch | seed=1 | MAE=3.9527e-07 | t=0.0203s

Completed: 2026-04-16T15:22:31.565781+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.