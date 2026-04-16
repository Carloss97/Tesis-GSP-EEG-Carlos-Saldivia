# Integration Log: scr_00230
Started: 2026-04-16T14:42:23.629180+00:00
Description: Screening scr_00230 ds=physionet_real graph=knn miss=3ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k5 built OK
    mean | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.0031s
    nearest | MR=3ch | seed=0 | MAE=3.5155e-06 | t=0.0072s
    tikhonov | MR=3ch | seed=0 | MAE=6.6659e-06 | t=0.0513s
    tv | MR=3ch | seed=0 | MAE=3.0738e-06 | t=0.7145s
    trss | MR=3ch | seed=0 | MAE=1.5180e-06 | t=0.3905s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.3391e-05 | t=0.0141s
    temporal_laplacian | MR=3ch | seed=0 | MAE=3.2026e-05 | t=20.0781s
    mean | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=3.5329e-06 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=6.6916e-06 | t=0.0415s
    tv | MR=3ch | seed=1 | MAE=3.0817e-06 | t=0.8914s
    trss | MR=3ch | seed=1 | MAE=1.5214e-06 | t=0.3461s

Completed: 2026-04-16T14:42:23.630061+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.