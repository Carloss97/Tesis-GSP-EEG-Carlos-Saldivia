# Integration Log: scr_00174
Started: 2026-04-16T14:15:12.946523+00:00
Description: Screening scr_00174 ds=iv100hz_mat graph=kalofolias miss=2ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: kalofolias built OK
    mean | MR=2ch | seed=0 | MAE=2.0300e+01 | t=0.0030s
    nearest | MR=2ch | seed=0 | MAE=3.2925e+01 | t=0.0042s
    tikhonov | MR=2ch | seed=0 | MAE=1.6141e+02 | t=0.0097s
    tv | MR=2ch | seed=0 | MAE=1.9663e+01 | t=0.3193s
    trss | MR=2ch | seed=0 | MAE=7.4870e+00 | t=0.3781s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.6315e+02 | t=0.0099s
    temporal_laplacian | MR=2ch | seed=0 | MAE=2.8863e+02 | t=33.2851s
    mean | MR=2ch | seed=1 | MAE=2.0537e+01 | t=0.0031s
    nearest | MR=2ch | seed=1 | MAE=3.3573e+01 | t=0.0043s
    tikhonov | MR=2ch | seed=1 | MAE=1.6248e+02 | t=0.0102s
    tv | MR=2ch | seed=1 | MAE=2.0234e+01 | t=0.2282s
    trss | MR=2ch | seed=1 | MAE=7.6641e+00 | t=0.3388s

Completed: 2026-04-16T14:15:12.947872+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.