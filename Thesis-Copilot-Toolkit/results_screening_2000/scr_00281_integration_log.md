# Integration Log: scr_00281
Started: 2026-04-16T15:09:37.024826+00:00
Description: Screening scr_00281 ds=bci_iv2a_real_s3 graph=kalofolias miss=3ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: kalofolias built OK
    mean | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=4.0021e-07 | t=0.0055s
    tikhonov | MR=3ch | seed=0 | MAE=1.6620e-06 | t=0.0129s
    tv | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.4108s
    trss | MR=3ch | seed=0 | MAE=3.3028e-07 | t=0.0662s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.8281e-06 | t=0.0165s
    temporal_laplacian | MR=3ch | seed=0 | MAE=5.6360e-06 | t=18.6276s
    mean | MR=3ch | seed=1 | MAE=4.4119e-07 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=3.7573e-07 | t=0.0054s
    tikhonov | MR=3ch | seed=1 | MAE=1.6585e-06 | t=0.0089s
    tv | MR=3ch | seed=1 | MAE=4.4119e-07 | t=1.3943s
    trss | MR=3ch | seed=1 | MAE=3.2113e-07 | t=0.9333s

Completed: 2026-04-16T15:09:37.025951+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.