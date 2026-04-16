# Integration Log: scr_00218
Started: 2026-04-16T14:36:12.081051+00:00
Description: Screening scr_00218 ds=physionet_real graph=knn miss=3ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k3 built OK
    mean | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=3.5155e-06 | t=0.0054s
    tikhonov | MR=3ch | seed=0 | MAE=5.0802e-06 | t=0.0089s
    tv | MR=3ch | seed=0 | MAE=3.0179e-06 | t=0.4889s
    trss | MR=3ch | seed=0 | MAE=1.5159e-06 | t=0.1875s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.0362e-05 | t=0.0425s
    temporal_laplacian | MR=3ch | seed=0 | MAE=2.8251e-05 | t=27.1222s
    mean | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=3.5329e-06 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=5.0927e-06 | t=0.0114s
    tv | MR=3ch | seed=1 | MAE=3.0275e-06 | t=0.3497s
    trss | MR=3ch | seed=1 | MAE=1.5031e-06 | t=0.0971s

Completed: 2026-04-16T14:36:12.082022+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.