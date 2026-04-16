# Integration Log: scr_00077
Started: 2026-04-16T14:51:25.843273+00:00
Description: Screening scr_00077 ds=bci_iv2a_real_s3 graph=knng miss=1ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knng built OK
    mean | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.0033s
    nearest | MR=1ch | seed=0 | MAE=1.2148e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=1.3240e-06 | t=0.0138s
    tv | MR=1ch | seed=0 | MAE=1.5215e-07 | t=0.3236s
    trss | MR=1ch | seed=0 | MAE=1.2834e-07 | t=0.0581s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.5585e-06 | t=0.0148s
    temporal_laplacian | MR=1ch | seed=0 | MAE=5.2630e-06 | t=31.6809s
    mean | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.0033s
    nearest | MR=1ch | seed=1 | MAE=1.2335e-07 | t=0.0360s
    tikhonov | MR=1ch | seed=1 | MAE=1.3205e-06 | t=0.0090s
    tv | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.3376s
    trss | MR=1ch | seed=1 | MAE=1.2848e-07 | t=0.3111s

Completed: 2026-04-16T14:51:25.844167+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.