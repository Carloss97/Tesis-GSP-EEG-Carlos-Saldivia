# Integration Log: scr_00029
Started: 2026-04-16T15:30:52.353003+00:00
Description: Screening scr_00029 ds=bci_iv2a_real_s3 graph=knn miss=1ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k7 built OK
    mean | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.0052s
    nearest | MR=1ch | seed=0 | MAE=1.2148e-07 | t=0.0047s
    tikhonov | MR=1ch | seed=0 | MAE=1.7706e-06 | t=0.0168s
    tv | MR=1ch | seed=0 | MAE=1.5214e-07 | t=1.4067s
    trss | MR=1ch | seed=0 | MAE=1.1653e-07 | t=0.2290s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.8899e-06 | t=0.0599s
    temporal_laplacian | MR=1ch | seed=0 | MAE=5.8301e-06 | t=19.4202s
    mean | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.0034s
    nearest | MR=1ch | seed=1 | MAE=1.2335e-07 | t=0.0049s
    tikhonov | MR=1ch | seed=1 | MAE=1.7679e-06 | t=0.0229s
    tv | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.4325s
    trss | MR=1ch | seed=1 | MAE=1.1959e-07 | t=0.0809s

Completed: 2026-04-16T15:30:52.354252+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.