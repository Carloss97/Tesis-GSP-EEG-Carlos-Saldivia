# Integration Log: scr_00315
Started: 2026-04-16T15:28:59.519768+00:00
Description: Screening scr_00315 ds=bci_iv2a_real_s1 graph=aew miss=3ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: aew built OK
    mean | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.0397s
    nearest | MR=3ch | seed=0 | MAE=2.1144e-06 | t=0.0853s
    tikhonov | MR=3ch | seed=0 | MAE=4.0723e-06 | t=0.0321s
    tv | MR=3ch | seed=0 | MAE=1.8779e-06 | t=0.5521s
    trss | MR=3ch | seed=0 | MAE=1.3621e-06 | t=0.4996s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=7.7624e-06 | t=0.0950s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.4107e-05 | t=27.5092s
    mean | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.0045s
    nearest | MR=3ch | seed=1 | MAE=2.0591e-06 | t=0.0066s
    tikhonov | MR=3ch | seed=1 | MAE=4.0968e-06 | t=0.0089s
    tv | MR=3ch | seed=1 | MAE=1.9137e-06 | t=1.5354s
    trss | MR=3ch | seed=1 | MAE=1.3797e-06 | t=0.4916s

Completed: 2026-04-16T15:28:59.521080+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.