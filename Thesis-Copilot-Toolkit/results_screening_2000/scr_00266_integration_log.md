# Integration Log: scr_00266
Started: 2026-04-16T15:00:29.806845+00:00
Description: Screening scr_00266 ds=physionet_real graph=gaussian miss=3ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=3.5155e-06 | t=0.0485s
    tikhonov | MR=3ch | seed=0 | MAE=1.7439e-05 | t=0.0087s
    tv | MR=3ch | seed=0 | MAE=3.0916e-06 | t=0.6403s
    trss | MR=3ch | seed=0 | MAE=2.2741e-06 | t=0.1844s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.2042e-05 | t=0.0989s
    temporal_laplacian | MR=3ch | seed=0 | MAE=3.8839e-05 | t=21.4522s
    mean | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=3.5329e-06 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=1.7451e-05 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.7614s
    trss | MR=3ch | seed=1 | MAE=2.2851e-06 | t=0.7978s

Completed: 2026-04-16T15:00:29.807638+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.