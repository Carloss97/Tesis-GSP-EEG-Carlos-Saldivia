# Integration Log: scr_00027
Started: 2026-04-16T15:29:04.239012+00:00
Description: Screening scr_00027 ds=bci_iv2a_real_s1 graph=knn miss=1ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k7 built OK
    mean | MR=1ch | seed=0 | MAE=6.8694e-07 | t=0.0037s
    nearest | MR=1ch | seed=0 | MAE=6.7972e-07 | t=0.0032s
    tikhonov | MR=1ch | seed=0 | MAE=6.6442e-06 | t=0.0803s
    tv | MR=1ch | seed=0 | MAE=6.8690e-07 | t=0.7258s
    trss | MR=1ch | seed=0 | MAE=4.4197e-07 | t=0.1728s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.1364e-05 | t=0.0141s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.6863e-05 | t=24.0886s
    mean | MR=1ch | seed=1 | MAE=6.0230e-07 | t=0.0038s
    nearest | MR=1ch | seed=1 | MAE=6.3859e-07 | t=0.0361s
    tikhonov | MR=1ch | seed=1 | MAE=6.6152e-06 | t=0.0101s
    tv | MR=1ch | seed=1 | MAE=6.0226e-07 | t=0.7838s
    trss | MR=1ch | seed=1 | MAE=3.8429e-07 | t=0.1253s

Completed: 2026-04-16T15:29:04.240582+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.