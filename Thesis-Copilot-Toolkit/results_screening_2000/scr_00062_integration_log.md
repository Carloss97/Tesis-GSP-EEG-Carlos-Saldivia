# Integration Log: scr_00062
Started: 2026-04-16T14:42:56.871856+00:00
Description: Screening scr_00062 ds=physionet_real graph=kalofolias miss=1ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: kalofolias built OK
    mean | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.0030s
    nearest | MR=1ch | seed=0 | MAE=1.0997e-06 | t=0.0042s
    tikhonov | MR=1ch | seed=0 | MAE=1.0342e-05 | t=0.0232s
    tv | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.8238s
    trss | MR=1ch | seed=0 | MAE=6.7960e-07 | t=0.2308s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.8768e-05 | t=0.0123s
    temporal_laplacian | MR=1ch | seed=0 | MAE=3.3181e-05 | t=19.8948s
    mean | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.0035s
    nearest | MR=1ch | seed=1 | MAE=1.1352e-06 | t=0.0101s
    tikhonov | MR=1ch | seed=1 | MAE=1.0373e-05 | t=0.0128s
    tv | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.4880s
    trss | MR=1ch | seed=1 | MAE=7.1998e-07 | t=0.0152s

Completed: 2026-04-16T14:42:56.872744+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.