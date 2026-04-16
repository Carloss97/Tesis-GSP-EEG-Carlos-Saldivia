# Integration Log: scr_00101
Started: 2026-04-16T15:03:09.127093+00:00
Description: Screening scr_00101 ds=bci_iv2a_real_s3 graph=aew miss=1ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: aew built OK
    mean | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.0032s
    nearest | MR=1ch | seed=0 | MAE=1.2148e-07 | t=0.0040s
    tikhonov | MR=1ch | seed=0 | MAE=1.0150e-06 | t=0.0089s
    tv | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.7693s
    trss | MR=1ch | seed=0 | MAE=1.2564e-07 | t=0.1212s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.2085e-06 | t=0.0177s
    temporal_laplacian | MR=1ch | seed=0 | MAE=4.6906e-06 | t=16.7091s
    mean | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.0033s
    nearest | MR=1ch | seed=1 | MAE=1.2335e-07 | t=0.0032s
    tikhonov | MR=1ch | seed=1 | MAE=1.0123e-06 | t=0.0800s
    tv | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.7505s
    trss | MR=1ch | seed=1 | MAE=1.2600e-07 | t=0.6349s

Completed: 2026-04-16T15:03:09.128521+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.