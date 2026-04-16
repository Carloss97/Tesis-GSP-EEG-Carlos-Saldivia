# Integration Log: scr_00185
Started: 2026-04-16T14:20:37.248606+00:00
Description: Screening scr_00185 ds=bci_iv2a_real_s3 graph=knng miss=2ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knng built OK
    mean | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.0030s
    nearest | MR=2ch | seed=0 | MAE=2.4876e-07 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=1.4321e-06 | t=0.0095s
    tv | MR=2ch | seed=0 | MAE=3.0422e-07 | t=0.3309s
    trss | MR=2ch | seed=0 | MAE=2.7018e-07 | t=0.5743s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.6054e-06 | t=0.0189s
    temporal_laplacian | MR=2ch | seed=0 | MAE=5.3351e-06 | t=25.5052s
    mean | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.0020s
    nearest | MR=2ch | seed=1 | MAE=2.5230e-07 | t=0.0028s
    tikhonov | MR=2ch | seed=1 | MAE=1.4129e-06 | t=0.0061s
    tv | MR=2ch | seed=1 | MAE=2.8474e-07 | t=0.1572s
    trss | MR=2ch | seed=1 | MAE=2.5676e-07 | t=0.0166s

Completed: 2026-04-16T14:20:37.250710+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.