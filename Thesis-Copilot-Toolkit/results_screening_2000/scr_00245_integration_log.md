# Integration Log: scr_00245
Started: 2026-04-16T14:51:28.249791+00:00
Description: Screening scr_00245 ds=bci_iv2a_real_s3 graph=knn miss=3ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k7 built OK
    mean | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.0020s
    nearest | MR=3ch | seed=0 | MAE=4.0021e-07 | t=0.0035s
    tikhonov | MR=3ch | seed=0 | MAE=1.9271e-06 | t=0.0087s
    tv | MR=3ch | seed=0 | MAE=4.5068e-07 | t=0.3506s
    trss | MR=3ch | seed=0 | MAE=3.6452e-07 | t=0.0545s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.9450e-06 | t=0.0132s
    temporal_laplacian | MR=3ch | seed=0 | MAE=5.9277e-06 | t=32.6621s
    mean | MR=3ch | seed=1 | MAE=4.4119e-07 | t=0.0037s
    nearest | MR=3ch | seed=1 | MAE=3.7573e-07 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=1.9179e-06 | t=0.0294s
    tv | MR=3ch | seed=1 | MAE=4.4120e-07 | t=0.3671s
    trss | MR=3ch | seed=1 | MAE=3.5400e-07 | t=0.2774s

Completed: 2026-04-16T14:51:28.250656+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.