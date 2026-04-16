# Integration Log: scr_00075
Started: 2026-04-16T14:49:26.055776+00:00
Description: Screening scr_00075 ds=bci_iv2a_real_s1 graph=knng miss=1ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knng built OK
    mean | MR=1ch | seed=0 | MAE=6.8694e-07 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=6.7972e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=4.9883e-06 | t=0.0809s
    tv | MR=1ch | seed=0 | MAE=6.8692e-07 | t=0.4572s
    trss | MR=1ch | seed=0 | MAE=4.8481e-07 | t=0.3092s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=9.9758e-06 | t=0.0501s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.5129e-05 | t=16.8921s
    mean | MR=1ch | seed=1 | MAE=6.0230e-07 | t=0.0033s
    nearest | MR=1ch | seed=1 | MAE=6.3859e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=4.9423e-06 | t=0.0096s
    tv | MR=1ch | seed=1 | MAE=6.0229e-07 | t=0.5837s
    trss | MR=1ch | seed=1 | MAE=4.2594e-07 | t=0.2854s

Completed: 2026-04-16T14:49:26.056612+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.