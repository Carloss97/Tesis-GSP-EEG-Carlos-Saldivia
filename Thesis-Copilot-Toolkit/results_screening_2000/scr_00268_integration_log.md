# Integration Log: scr_00268
Started: 2026-04-16T15:02:29.004743+00:00
Description: Screening scr_00268 ds=bci_iv2a_real_s2 graph=gaussian miss=3ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.0709s
    nearest | MR=3ch | seed=0 | MAE=5.1829e-07 | t=0.0056s
    tikhonov | MR=3ch | seed=0 | MAE=2.9925e-06 | t=0.0087s
    tv | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.6469s
    trss | MR=3ch | seed=0 | MAE=3.8275e-07 | t=0.7434s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=5.3107e-06 | t=0.0553s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.7165e-05 | t=20.2918s
    mean | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.0036s
    nearest | MR=3ch | seed=1 | MAE=4.9473e-07 | t=0.0072s
    tikhonov | MR=3ch | seed=1 | MAE=2.9910e-06 | t=0.0060s
    tv | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.2083s
    trss | MR=3ch | seed=1 | MAE=3.8330e-07 | t=0.1636s

Completed: 2026-04-16T15:02:29.005666+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.