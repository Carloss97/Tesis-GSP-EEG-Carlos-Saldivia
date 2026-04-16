# Integration Log: scr_00375
Started: 2026-04-16T13:10:33.883978+00:00
Description: Screening scr_00375 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0028s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=1.0252e-05 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.2827s
    trss | MR=0.1 | seed=0 | MAE=8.8942e-07 | t=0.0390s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.3119e-05 | t=0.0125s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.8943e-05 | t=2.5064s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=1.0262e-05 | t=0.0085s
    tv | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.4031s
    trss | MR=0.1 | seed=1 | MAE=8.3377e-07 | t=0.0569s

Completed: 2026-04-16T13:10:33.885107+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.