# Integration Log: scr_00207
Started: 2026-04-16T14:31:10.457414+00:00
Description: Screening scr_00207 ds=bci_iv2a_real_s1 graph=aew miss=2ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: aew built OK
    mean | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.0037s
    nearest | MR=2ch | seed=0 | MAE=1.3708e-06 | t=0.0050s
    tikhonov | MR=2ch | seed=0 | MAE=3.6299e-06 | t=0.0332s
    tv | MR=2ch | seed=0 | MAE=1.3008e-06 | t=0.5048s
    trss | MR=2ch | seed=0 | MAE=9.4998e-07 | t=0.3259s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=7.4389e-06 | t=0.0122s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.3811e-05 | t=32.9745s
    mean | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.0030s
    nearest | MR=2ch | seed=1 | MAE=1.2545e-06 | t=0.0043s
    tikhonov | MR=2ch | seed=1 | MAE=3.5630e-06 | t=0.0088s
    tv | MR=2ch | seed=1 | MAE=1.2356e-06 | t=0.6200s
    trss | MR=2ch | seed=1 | MAE=8.9560e-07 | t=0.4438s

Completed: 2026-04-16T14:31:10.458293+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.