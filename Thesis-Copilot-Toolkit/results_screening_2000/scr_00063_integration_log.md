# Integration Log: scr_00063
Started: 2026-04-16T14:43:56.164317+00:00
Description: Screening scr_00063 ds=bci_iv2a_real_s1 graph=kalofolias miss=1ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: kalofolias built OK
    mean | MR=1ch | seed=0 | MAE=6.8694e-07 | t=0.0120s
    nearest | MR=1ch | seed=0 | MAE=6.7972e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=6.1645e-06 | t=0.0099s
    tv | MR=1ch | seed=0 | MAE=6.8694e-07 | t=0.5279s
    trss | MR=1ch | seed=0 | MAE=4.5228e-07 | t=0.0952s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.1146e-05 | t=0.0123s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.6347e-05 | t=25.0918s
    mean | MR=1ch | seed=1 | MAE=6.0230e-07 | t=0.0020s
    nearest | MR=1ch | seed=1 | MAE=6.3859e-07 | t=0.0034s
    tikhonov | MR=1ch | seed=1 | MAE=6.1411e-06 | t=0.0106s
    tv | MR=1ch | seed=1 | MAE=6.0230e-07 | t=0.1990s
    trss | MR=1ch | seed=1 | MAE=3.9143e-07 | t=0.0182s

Completed: 2026-04-16T14:43:56.165430+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.