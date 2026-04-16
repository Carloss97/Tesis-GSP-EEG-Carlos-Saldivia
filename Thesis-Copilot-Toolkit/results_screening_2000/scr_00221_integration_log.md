# Integration Log: scr_00221
Started: 2026-04-16T14:38:59.319231+00:00
Description: Screening scr_00221 ds=bci_iv2a_real_s3 graph=knn miss=3ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k3 built OK
    mean | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.0189s
    nearest | MR=3ch | seed=0 | MAE=4.0021e-07 | t=0.0054s
    tikhonov | MR=3ch | seed=0 | MAE=1.3309e-06 | t=0.0088s
    tv | MR=3ch | seed=0 | MAE=4.5069e-07 | t=0.3890s
    trss | MR=3ch | seed=0 | MAE=4.0174e-07 | t=0.5586s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.4532e-06 | t=0.0142s
    temporal_laplacian | MR=3ch | seed=0 | MAE=4.8802e-06 | t=23.0998s
    mean | MR=3ch | seed=1 | MAE=4.4119e-07 | t=0.0090s
    nearest | MR=3ch | seed=1 | MAE=3.7573e-07 | t=0.0106s
    tikhonov | MR=3ch | seed=1 | MAE=1.3195e-06 | t=0.0100s
    tv | MR=3ch | seed=1 | MAE=4.4120e-07 | t=0.3130s
    trss | MR=3ch | seed=1 | MAE=3.9451e-07 | t=0.0211s

Completed: 2026-04-16T14:38:59.320450+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.