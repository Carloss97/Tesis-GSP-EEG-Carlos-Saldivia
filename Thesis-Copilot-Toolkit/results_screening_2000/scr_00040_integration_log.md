# Integration Log: scr_00040
Started: 2026-04-16T15:35:43.159766+00:00
Description: Screening scr_00040 ds=bci_iv2a_real_s2 graph=gaussian miss=1ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.0087s
    nearest | MR=1ch | seed=0 | MAE=1.6572e-07 | t=0.0097s
    tikhonov | MR=1ch | seed=0 | MAE=2.8749e-06 | t=0.0143s
    tv | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.6116s
    trss | MR=1ch | seed=0 | MAE=1.1940e-07 | t=0.1243s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=5.2780e-06 | t=0.0242s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.7039e-05 | t=21.6529s
    mean | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.0031s
    nearest | MR=1ch | seed=1 | MAE=1.6467e-07 | t=0.0033s
    tikhonov | MR=1ch | seed=1 | MAE=2.8765e-06 | t=0.0192s
    tv | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.8294s
    trss | MR=1ch | seed=1 | MAE=1.2046e-07 | t=0.1779s

Completed: 2026-04-16T15:35:43.161081+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.