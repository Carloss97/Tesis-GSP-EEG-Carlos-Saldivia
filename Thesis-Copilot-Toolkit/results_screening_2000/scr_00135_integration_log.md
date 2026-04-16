# Integration Log: scr_00135
Started: 2026-04-16T15:19:49.294500+00:00
Description: Screening scr_00135 ds=bci_iv2a_real_s1 graph=knn miss=2ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k7 built OK
    mean | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.0036s
    nearest | MR=2ch | seed=0 | MAE=1.3708e-06 | t=0.0054s
    tikhonov | MR=2ch | seed=0 | MAE=6.9979e-06 | t=0.0459s
    tv | MR=2ch | seed=0 | MAE=1.3024e-06 | t=0.5526s
    trss | MR=2ch | seed=0 | MAE=8.5933e-07 | t=0.3521s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.1542e-05 | t=0.1263s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.7024e-05 | t=26.1987s
    mean | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.0037s
    nearest | MR=2ch | seed=1 | MAE=1.2545e-06 | t=0.0044s
    tikhonov | MR=2ch | seed=1 | MAE=6.9717e-06 | t=0.0578s
    tv | MR=2ch | seed=1 | MAE=1.2371e-06 | t=0.9011s
    trss | MR=2ch | seed=1 | MAE=8.0482e-07 | t=0.1266s

Completed: 2026-04-16T15:19:49.295407+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.