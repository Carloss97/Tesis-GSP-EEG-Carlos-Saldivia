# Integration Log: scr_00293
Started: 2026-04-16T15:16:23.476380+00:00
Description: Screening scr_00293 ds=bci_iv2a_real_s3 graph=knng miss=3ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knng built OK
    mean | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.0036s
    nearest | MR=3ch | seed=0 | MAE=4.0021e-07 | t=0.1786s
    tikhonov | MR=3ch | seed=0 | MAE=1.5217e-06 | t=0.1426s
    tv | MR=3ch | seed=0 | MAE=4.5069e-07 | t=0.6052s
    trss | MR=3ch | seed=0 | MAE=4.0081e-07 | t=1.0732s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.6434e-06 | t=0.1075s
    temporal_laplacian | MR=3ch | seed=0 | MAE=5.4038e-06 | t=30.4027s
    mean | MR=3ch | seed=1 | MAE=4.4119e-07 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=3.7573e-07 | t=0.0068s
    tikhonov | MR=3ch | seed=1 | MAE=1.5197e-06 | t=0.0126s
    tv | MR=3ch | seed=1 | MAE=4.4121e-07 | t=0.7304s
    trss | MR=3ch | seed=1 | MAE=3.9137e-07 | t=0.5091s

Completed: 2026-04-16T15:16:23.477263+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.