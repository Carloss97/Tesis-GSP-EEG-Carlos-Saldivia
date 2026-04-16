# Integration Log: scr_00242
Started: 2026-04-16T14:48:28.657815+00:00
Description: Screening scr_00242 ds=physionet_real graph=knn miss=3ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k7 built OK
    mean | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.0037s
    nearest | MR=3ch | seed=0 | MAE=3.5155e-06 | t=0.0055s
    tikhonov | MR=3ch | seed=0 | MAE=8.6650e-06 | t=0.0103s
    tv | MR=3ch | seed=0 | MAE=3.0834e-06 | t=0.8340s
    trss | MR=3ch | seed=0 | MAE=1.6022e-06 | t=0.3873s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.6150e-05 | t=0.0124s
    temporal_laplacian | MR=3ch | seed=0 | MAE=3.4407e-05 | t=10.4693s
    mean | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=3.5329e-06 | t=0.0054s
    tikhonov | MR=3ch | seed=1 | MAE=8.6921e-06 | t=0.0086s
    tv | MR=3ch | seed=1 | MAE=3.0909e-06 | t=0.4037s
    trss | MR=3ch | seed=1 | MAE=1.6365e-06 | t=0.2734s

Completed: 2026-04-16T14:48:28.667155+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.