# Integration Log: scr_01143
Started: 2026-04-16T14:21:34.832078+00:00
Description: Screening scr_01143 ds=bci_iv2a_real_s1 graph=kalofolias miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: kalofolias built OK
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.7905s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.2471e-06 | t=0.0125s
    trss | MR=0.2 | seed=0 | MAE=7.0725e-07 | t=0.3182s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0348e-05 | t=18.0927s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.4348s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.4531e-06 | t=0.0456s
    trss | MR=0.2 | seed=1 | MAE=8.3690e-07 | t=0.4684s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.0466e-05 | t=23.4672s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.2058s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.8998e-06 | t=0.0084s
    trss | MR=0.2 | seed=0 | MAE=9.6682e-07 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2237e-05 | t=27.3853s

Completed: 2026-04-16T14:21:34.832860+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.