# Integration Log: scr_00302
Started: 2026-04-16T15:20:39.099678+00:00
Description: Screening scr_00302 ds=physionet_real graph=vknng miss=3ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: vknng built OK
    mean | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.0037s
    nearest | MR=3ch | seed=0 | MAE=3.5155e-06 | t=0.0055s
    tikhonov | MR=3ch | seed=0 | MAE=6.0800e-06 | t=0.0092s
    tv | MR=3ch | seed=0 | MAE=3.0612e-06 | t=0.5810s
    trss | MR=3ch | seed=0 | MAE=1.5584e-06 | t=0.2263s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.2233e-05 | t=0.0276s
    temporal_laplacian | MR=3ch | seed=0 | MAE=3.0205e-05 | t=17.8676s
    mean | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.0635s
    nearest | MR=3ch | seed=1 | MAE=3.5329e-06 | t=0.0054s
    tikhonov | MR=3ch | seed=1 | MAE=6.0885e-06 | t=0.0110s
    tv | MR=3ch | seed=1 | MAE=3.0695e-06 | t=0.7092s
    trss | MR=3ch | seed=1 | MAE=1.5292e-06 | t=0.2191s

Completed: 2026-04-16T15:20:39.100669+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.