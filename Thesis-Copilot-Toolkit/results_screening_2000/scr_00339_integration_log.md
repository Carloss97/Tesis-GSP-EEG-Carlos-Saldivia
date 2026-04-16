# Integration Log: scr_00339
Started: 2026-04-16T15:42:25.289082+00:00
Description: Screening scr_00339 ds=bci_iv2a_real_s1 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0029s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0051s
    tikhonov | MR=0.1 | seed=0 | MAE=6.0125e-06 | t=0.0104s
    tv | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.7415s
    trss | MR=0.1 | seed=0 | MAE=9.1600e-07 | t=0.2516s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.0783e-05 | t=0.0141s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.6058e-05 | t=37.1066s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0501s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0041s
    tikhonov | MR=0.1 | seed=1 | MAE=5.9697e-06 | t=0.1003s
    tv | MR=0.1 | seed=1 | MAE=1.2371e-06 | t=0.8151s
    trss | MR=0.1 | seed=1 | MAE=8.3782e-07 | t=0.5007s

Completed: 2026-04-16T15:42:25.290212+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.