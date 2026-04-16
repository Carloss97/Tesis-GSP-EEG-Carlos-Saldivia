# Integration Log: scr_00423
Started: 2026-04-16T13:25:03.764960+00:00
Description: Screening scr_00423 ds=bci_iv2a_real_s1 graph=aew miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0032s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0032s
    tikhonov | MR=0.1 | seed=0 | MAE=3.6299e-06 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=1.3008e-06 | t=0.1607s
    trss | MR=0.1 | seed=0 | MAE=9.4998e-07 | t=0.0180s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=7.4389e-06 | t=0.0092s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.3811e-05 | t=4.8456s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0045s
    tikhonov | MR=0.1 | seed=1 | MAE=3.5630e-06 | t=0.0087s
    tv | MR=0.1 | seed=1 | MAE=1.2356e-06 | t=0.7418s
    trss | MR=0.1 | seed=1 | MAE=8.9560e-07 | t=0.0540s

Completed: 2026-04-16T13:25:03.765764+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.