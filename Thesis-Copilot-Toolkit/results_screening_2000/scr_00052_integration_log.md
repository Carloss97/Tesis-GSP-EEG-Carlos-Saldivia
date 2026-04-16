# Integration Log: scr_00052
Started: 2026-04-16T15:42:57.619068+00:00
Description: Screening scr_00052 ds=bci_iv2a_real_s2 graph=gaussian miss=1ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=1.6572e-07 | t=0.0032s
    tikhonov | MR=1ch | seed=0 | MAE=2.8749e-06 | t=0.0100s
    tv | MR=1ch | seed=0 | MAE=1.7047e-07 | t=1.4553s
    trss | MR=1ch | seed=0 | MAE=1.1940e-07 | t=0.4946s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=5.2780e-06 | t=0.0139s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.7039e-05 | t=39.0595s
    mean | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.0031s
    nearest | MR=1ch | seed=1 | MAE=1.6467e-07 | t=0.0038s
    tikhonov | MR=1ch | seed=1 | MAE=2.8765e-06 | t=0.0378s
    tv | MR=1ch | seed=1 | MAE=1.7401e-07 | t=1.0457s
    trss | MR=1ch | seed=1 | MAE=1.2046e-07 | t=0.1400s

Completed: 2026-04-16T15:42:57.620093+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.