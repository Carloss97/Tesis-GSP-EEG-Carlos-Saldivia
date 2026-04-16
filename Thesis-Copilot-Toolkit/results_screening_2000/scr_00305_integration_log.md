# Integration Log: scr_00305
Started: 2026-04-16T15:23:41.454656+00:00
Description: Screening scr_00305 ds=bci_iv2a_real_s3 graph=vknng miss=3ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: vknng built OK
    mean | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=4.0021e-07 | t=0.0064s
    tikhonov | MR=3ch | seed=0 | MAE=1.1116e-06 | t=0.0284s
    tv | MR=3ch | seed=0 | MAE=4.5069e-07 | t=0.6787s
    trss | MR=3ch | seed=0 | MAE=4.0919e-07 | t=0.4546s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.1794e-06 | t=0.0402s
    temporal_laplacian | MR=3ch | seed=0 | MAE=4.2107e-06 | t=34.1780s
    mean | MR=3ch | seed=1 | MAE=4.4119e-07 | t=0.0361s
    nearest | MR=3ch | seed=1 | MAE=3.7573e-07 | t=0.0058s
    tikhonov | MR=3ch | seed=1 | MAE=1.1051e-06 | t=0.0095s
    tv | MR=3ch | seed=1 | MAE=4.4120e-07 | t=0.5348s
    trss | MR=3ch | seed=1 | MAE=4.0169e-07 | t=0.0697s

Completed: 2026-04-16T15:23:41.455823+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.