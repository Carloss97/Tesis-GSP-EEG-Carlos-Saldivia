# Integration Log: scr_00089
Started: 2026-04-16T14:56:58.206630+00:00
Description: Screening scr_00089 ds=bci_iv2a_real_s3 graph=vknng miss=1ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: vknng built OK
    mean | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.0033s
    nearest | MR=1ch | seed=0 | MAE=1.2148e-07 | t=0.0073s
    tikhonov | MR=1ch | seed=0 | MAE=8.6410e-07 | t=0.0089s
    tv | MR=1ch | seed=0 | MAE=1.5215e-07 | t=0.7214s
    trss | MR=1ch | seed=0 | MAE=1.3606e-07 | t=0.0772s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.0432e-06 | t=0.0127s
    temporal_laplacian | MR=1ch | seed=0 | MAE=4.0031e-06 | t=25.0521s
    mean | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.0022s
    nearest | MR=1ch | seed=1 | MAE=1.2335e-07 | t=0.0028s
    tikhonov | MR=1ch | seed=1 | MAE=8.6619e-07 | t=0.0066s
    tv | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.1695s
    trss | MR=1ch | seed=1 | MAE=1.3177e-07 | t=0.0151s

Completed: 2026-04-16T14:56:58.207607+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.