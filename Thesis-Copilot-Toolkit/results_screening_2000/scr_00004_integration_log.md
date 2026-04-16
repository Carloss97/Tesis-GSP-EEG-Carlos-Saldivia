# Integration Log: scr_00004
Started: 2026-04-16T15:16:52.996204+00:00
Description: Screening scr_00004 ds=bci_iv2a_real_s2 graph=knn miss=1ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.0037s
    nearest | MR=1ch | seed=0 | MAE=1.6572e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=1.2653e-06 | t=0.0088s
    tv | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.5853s
    trss | MR=1ch | seed=0 | MAE=1.4152e-07 | t=0.3150s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.5174e-06 | t=0.0422s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.2230e-05 | t=24.6168s
    mean | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.0034s
    nearest | MR=1ch | seed=1 | MAE=1.6467e-07 | t=0.0032s
    tikhonov | MR=1ch | seed=1 | MAE=1.2679e-06 | t=0.0102s
    tv | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.6142s
    trss | MR=1ch | seed=1 | MAE=1.4300e-07 | t=0.5907s

Completed: 2026-04-16T15:16:52.997223+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.