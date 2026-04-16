# Integration Log: scr_00208
Started: 2026-04-16T14:32:10.793406+00:00
Description: Screening scr_00208 ds=bci_iv2a_real_s2 graph=aew miss=2ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: aew built OK
    mean | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.0035s
    nearest | MR=2ch | seed=0 | MAE=3.2237e-07 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=1.4771e-06 | t=0.0175s
    tv | MR=2ch | seed=0 | MAE=3.3427e-07 | t=0.5204s
    trss | MR=2ch | seed=0 | MAE=2.7577e-07 | t=0.6108s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.5895e-06 | t=0.0128s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.3238e-05 | t=23.8888s
    mean | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.0031s
    nearest | MR=2ch | seed=1 | MAE=3.1417e-07 | t=0.0055s
    tikhonov | MR=2ch | seed=1 | MAE=1.4825e-06 | t=0.0683s
    tv | MR=2ch | seed=1 | MAE=3.4817e-07 | t=0.7618s
    trss | MR=2ch | seed=1 | MAE=2.8207e-07 | t=0.1866s

Completed: 2026-04-16T14:32:10.794404+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.