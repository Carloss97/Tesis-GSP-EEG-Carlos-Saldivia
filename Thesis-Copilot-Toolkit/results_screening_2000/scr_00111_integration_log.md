# Integration Log: scr_00111
Started: 2026-04-16T15:07:06.561603+00:00
Description: Screening scr_00111 ds=bci_iv2a_real_s1 graph=knn miss=2ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.0038s
    nearest | MR=2ch | seed=0 | MAE=1.3708e-06 | t=0.0044s
    tikhonov | MR=2ch | seed=0 | MAE=4.5749e-06 | t=0.0126s
    tv | MR=2ch | seed=0 | MAE=1.3024e-06 | t=0.5525s
    trss | MR=2ch | seed=0 | MAE=9.1525e-07 | t=0.4434s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=9.3331e-06 | t=0.0281s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.4248e-05 | t=27.9963s
    mean | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=1.2545e-06 | t=0.0045s
    tikhonov | MR=2ch | seed=1 | MAE=4.5276e-06 | t=0.0090s
    tv | MR=2ch | seed=1 | MAE=1.2371e-06 | t=0.3933s
    trss | MR=2ch | seed=1 | MAE=8.4390e-07 | t=0.4037s

Completed: 2026-04-16T15:07:06.563304+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.