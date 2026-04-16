# Integration Log: scr_00016
Started: 2026-04-16T15:23:42.016908+00:00
Description: Screening scr_00016 ds=bci_iv2a_real_s2 graph=knn miss=1ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k5 built OK
    mean | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.0032s
    nearest | MR=1ch | seed=0 | MAE=1.6572e-07 | t=0.0032s
    tikhonov | MR=1ch | seed=0 | MAE=1.7061e-06 | t=0.0829s
    tv | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.5683s
    trss | MR=1ch | seed=0 | MAE=1.3699e-07 | t=1.1424s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.7999e-06 | t=0.0162s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.4188e-05 | t=30.6222s
    mean | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.0057s
    nearest | MR=1ch | seed=1 | MAE=1.6467e-07 | t=0.0360s
    tikhonov | MR=1ch | seed=1 | MAE=1.7081e-06 | t=0.0137s
    tv | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.5586s
    trss | MR=1ch | seed=1 | MAE=1.3512e-07 | t=0.3611s

Completed: 2026-04-16T15:23:42.017796+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.