# Integration Log: scr_00182
Started: 2026-04-16T14:17:44.478569+00:00
Description: Screening scr_00182 ds=physionet_real graph=knng miss=2ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knng built OK
    mean | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.0031s
    nearest | MR=2ch | seed=0 | MAE=2.3639e-06 | t=0.0044s
    tikhonov | MR=2ch | seed=0 | MAE=5.6348e-06 | t=0.0098s
    tv | MR=2ch | seed=0 | MAE=2.0688e-06 | t=0.2898s
    trss | MR=2ch | seed=0 | MAE=1.0043e-06 | t=0.2271s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.2052e-05 | t=0.0081s
    temporal_laplacian | MR=2ch | seed=0 | MAE=3.0146e-05 | t=26.7476s
    mean | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.0030s
    nearest | MR=2ch | seed=1 | MAE=2.3187e-06 | t=0.0047s
    tikhonov | MR=2ch | seed=1 | MAE=5.6214e-06 | t=0.0091s
    tv | MR=2ch | seed=1 | MAE=2.0300e-06 | t=0.4032s
    trss | MR=2ch | seed=1 | MAE=9.8924e-07 | t=0.6959s

Completed: 2026-04-16T14:17:44.479793+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.