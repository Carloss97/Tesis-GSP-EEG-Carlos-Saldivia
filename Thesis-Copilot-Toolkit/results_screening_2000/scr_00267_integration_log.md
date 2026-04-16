# Integration Log: scr_00267
Started: 2026-04-16T15:01:35.061086+00:00
Description: Screening scr_00267 ds=bci_iv2a_real_s1 graph=gaussian miss=3ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=2.1144e-06 | t=0.0054s
    tikhonov | MR=3ch | seed=0 | MAE=1.0547e-05 | t=0.0087s
    tv | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.9756s
    trss | MR=3ch | seed=0 | MAE=1.2875e-06 | t=0.4317s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.3287e-05 | t=0.1101s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.9096e-05 | t=24.5346s
    mean | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.0037s
    nearest | MR=3ch | seed=1 | MAE=2.0591e-06 | t=0.0058s
    tikhonov | MR=3ch | seed=1 | MAE=1.0502e-05 | t=0.0165s
    tv | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.3006s
    trss | MR=3ch | seed=1 | MAE=1.2990e-06 | t=0.0174s

Completed: 2026-04-16T15:01:35.061861+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.