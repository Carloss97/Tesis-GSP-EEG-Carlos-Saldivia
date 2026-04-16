# Integration Log: scr_00255
Started: 2026-04-16T14:55:33.087211+00:00
Description: Screening scr_00255 ds=bci_iv2a_real_s1 graph=gaussian miss=3ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.0040s
    nearest | MR=3ch | seed=0 | MAE=2.1144e-06 | t=0.0070s
    tikhonov | MR=3ch | seed=0 | MAE=1.0547e-05 | t=0.0120s
    tv | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.4096s
    trss | MR=3ch | seed=0 | MAE=1.2875e-06 | t=0.3319s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.3287e-05 | t=0.0159s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.9096e-05 | t=23.8318s
    mean | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=2.0591e-06 | t=0.0385s
    tikhonov | MR=3ch | seed=1 | MAE=1.0502e-05 | t=0.0089s
    tv | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.5540s
    trss | MR=3ch | seed=1 | MAE=1.2990e-06 | t=0.5777s

Completed: 2026-04-16T14:55:33.088147+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.