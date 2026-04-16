# Integration Log: scr_00124
Started: 2026-04-16T15:13:27.843114+00:00
Description: Screening scr_00124 ds=bci_iv2a_real_s2 graph=knn miss=2ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k5 built OK
    mean | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.0032s
    nearest | MR=2ch | seed=0 | MAE=3.2237e-07 | t=0.0044s
    tikhonov | MR=2ch | seed=0 | MAE=1.8042e-06 | t=0.0114s
    tv | MR=2ch | seed=0 | MAE=3.3430e-07 | t=0.3508s
    trss | MR=2ch | seed=0 | MAE=2.6884e-07 | t=0.1418s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.8386e-06 | t=0.0124s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.4370e-05 | t=17.7989s
    mean | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.0022s
    nearest | MR=2ch | seed=1 | MAE=3.1417e-07 | t=0.0068s
    tikhonov | MR=2ch | seed=1 | MAE=1.8118e-06 | t=0.0065s
    tv | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.4697s
    trss | MR=2ch | seed=1 | MAE=2.7431e-07 | t=0.2293s

Completed: 2026-04-16T15:13:27.844202+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.