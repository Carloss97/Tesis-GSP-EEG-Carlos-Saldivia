# Integration Log: scr_00291
Started: 2026-04-16T15:13:47.214271+00:00
Description: Screening scr_00291 ds=bci_iv2a_real_s1 graph=knng miss=3ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knng built OK
    mean | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.0054s
    nearest | MR=3ch | seed=0 | MAE=2.1144e-06 | t=0.0047s
    tikhonov | MR=3ch | seed=0 | MAE=5.8527e-06 | t=0.0060s
    tv | MR=3ch | seed=0 | MAE=1.8806e-06 | t=0.2078s
    trss | MR=3ch | seed=0 | MAE=1.3556e-06 | t=0.2657s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.0476e-05 | t=0.0126s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.5610e-05 | t=25.8018s
    mean | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.0036s
    nearest | MR=3ch | seed=1 | MAE=2.0591e-06 | t=0.0057s
    tikhonov | MR=3ch | seed=1 | MAE=5.8559e-06 | t=0.0157s
    tv | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.4445s
    trss | MR=3ch | seed=1 | MAE=1.3716e-06 | t=0.1840s

Completed: 2026-04-16T15:13:47.215150+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.