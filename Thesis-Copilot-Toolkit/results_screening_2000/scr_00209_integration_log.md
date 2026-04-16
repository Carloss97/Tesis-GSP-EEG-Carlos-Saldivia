# Integration Log: scr_00209
Started: 2026-04-16T14:32:48.054168+00:00
Description: Screening scr_00209 ds=bci_iv2a_real_s3 graph=aew miss=2ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: aew built OK
    mean | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.0352s
    nearest | MR=2ch | seed=0 | MAE=2.4876e-07 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=1.1395e-06 | t=0.0086s
    tv | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.8761s
    trss | MR=2ch | seed=0 | MAE=2.6581e-07 | t=0.3273s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.2714e-06 | t=0.0125s
    temporal_laplacian | MR=2ch | seed=0 | MAE=4.7802e-06 | t=16.9561s
    mean | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.0031s
    nearest | MR=2ch | seed=1 | MAE=2.5230e-07 | t=0.0043s
    tikhonov | MR=2ch | seed=1 | MAE=1.1171e-06 | t=0.0095s
    tv | MR=2ch | seed=1 | MAE=2.8470e-07 | t=0.9437s
    trss | MR=2ch | seed=1 | MAE=2.5203e-07 | t=0.5842s

Completed: 2026-04-16T14:32:48.055012+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.