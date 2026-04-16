# Integration Log: scr_00316
Started: 2026-04-16T15:30:00.245037+00:00
Description: Screening scr_00316 ds=bci_iv2a_real_s2 graph=aew miss=3ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: aew built OK
    mean | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.0036s
    nearest | MR=3ch | seed=0 | MAE=5.1829e-07 | t=0.0070s
    tikhonov | MR=3ch | seed=0 | MAE=1.6212e-06 | t=0.0128s
    tv | MR=3ch | seed=0 | MAE=5.2943e-07 | t=0.2883s
    trss | MR=3ch | seed=0 | MAE=4.5191e-07 | t=0.0237s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.6431e-06 | t=0.0128s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.3437e-05 | t=24.6423s
    mean | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.0073s
    nearest | MR=3ch | seed=1 | MAE=4.9473e-07 | t=0.0064s
    tikhonov | MR=3ch | seed=1 | MAE=1.6201e-06 | t=0.0094s
    tv | MR=3ch | seed=1 | MAE=5.2907e-07 | t=1.4499s
    trss | MR=3ch | seed=1 | MAE=4.4387e-07 | t=0.2444s

Completed: 2026-04-16T15:30:00.246232+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.