# Integration Log: scr_00254
Started: 2026-04-16T14:54:35.538583+00:00
Description: Screening scr_00254 ds=physionet_real graph=gaussian miss=3ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=3.5155e-06 | t=0.0060s
    tikhonov | MR=3ch | seed=0 | MAE=1.7522e-05 | t=0.0113s
    tv | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.4725s
    trss | MR=3ch | seed=0 | MAE=2.2814e-06 | t=0.0428s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.2070e-05 | t=0.0151s
    temporal_laplacian | MR=3ch | seed=0 | MAE=3.8878e-05 | t=25.8388s
    mean | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=3.5329e-06 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=1.7534e-05 | t=0.0089s
    tv | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.6932s
    trss | MR=3ch | seed=1 | MAE=2.2924e-06 | t=0.3479s

Completed: 2026-04-16T14:54:35.539447+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.