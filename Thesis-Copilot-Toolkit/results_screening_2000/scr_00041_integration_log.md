# Integration Log: scr_00041
Started: 2026-04-16T15:37:06.080190+00:00
Description: Screening scr_00041 ds=bci_iv2a_real_s3 graph=gaussian miss=1ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=1.2148e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=2.4228e-06 | t=0.0142s
    tv | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.7721s
    trss | MR=1ch | seed=0 | MAE=1.0862e-07 | t=0.1354s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=3.2012e-06 | t=0.0169s
    temporal_laplacian | MR=1ch | seed=0 | MAE=6.4357e-06 | t=33.1125s
    mean | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.0031s
    nearest | MR=1ch | seed=1 | MAE=1.2335e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=2.4197e-06 | t=0.0094s
    tv | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.2872s
    trss | MR=1ch | seed=1 | MAE=1.0668e-07 | t=0.0209s

Completed: 2026-04-16T15:37:06.081593+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.