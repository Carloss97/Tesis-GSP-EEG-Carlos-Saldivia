# Integration Log: scr_00028
Started: 2026-04-16T15:30:01.420394+00:00
Description: Screening scr_00028 ds=bci_iv2a_real_s2 graph=knn miss=1ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k7 built OK
    mean | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.0036s
    nearest | MR=1ch | seed=0 | MAE=1.6572e-07 | t=0.0038s
    tikhonov | MR=1ch | seed=0 | MAE=2.0424e-06 | t=0.0098s
    tv | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.4648s
    trss | MR=1ch | seed=0 | MAE=1.3151e-07 | t=0.2388s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.9652e-06 | t=0.0287s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.5281e-05 | t=23.5218s
    mean | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.0077s
    nearest | MR=1ch | seed=1 | MAE=1.6467e-07 | t=0.0065s
    tikhonov | MR=1ch | seed=1 | MAE=2.0431e-06 | t=0.0119s
    tv | MR=1ch | seed=1 | MAE=1.7402e-07 | t=0.6958s
    trss | MR=1ch | seed=1 | MAE=1.3624e-07 | t=0.1814s

Completed: 2026-04-16T15:30:01.422614+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.