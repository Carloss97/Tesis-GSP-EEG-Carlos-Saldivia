# Integration Log: scr_00712
Started: 2026-04-16T15:35:04.093418+00:00
Description: Screening scr_00712 ds=bci_iv2a_real_s2 graph=kalofolias miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.0032s
    nearest | MR=0.4 | seed=0 | MAE=1.7309e-06 | t=0.1065s
    tikhonov | MR=0.4 | seed=0 | MAE=2.7611e-06 | t=0.0503s
    tv | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.6505s
    trss | MR=0.4 | seed=0 | MAE=1.4569e-06 | t=0.2894s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=5.1847e-06 | t=0.0490s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.6057e-05 | t=21.9768s
    mean | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.0042s
    nearest | MR=0.4 | seed=1 | MAE=1.7485e-06 | t=0.0301s
    tikhonov | MR=0.4 | seed=1 | MAE=2.7186e-06 | t=0.0127s
    tv | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.4159s
    trss | MR=0.4 | seed=1 | MAE=1.4107e-06 | t=0.0285s

Completed: 2026-04-16T15:35:04.094328+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.