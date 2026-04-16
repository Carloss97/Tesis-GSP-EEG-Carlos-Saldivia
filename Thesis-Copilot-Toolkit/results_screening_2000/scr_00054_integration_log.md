# Integration Log: scr_00054
Started: 2026-04-16T14:40:45.014817+00:00
Description: Screening scr_00054 ds=iv100hz_mat graph=gaussian miss=1ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=1ch | seed=0 | MAE=1.1091e+01 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=1.6962e+01 | t=0.0047s
    tikhonov | MR=1ch | seed=0 | MAE=9.4794e+01 | t=0.0088s
    tv | MR=1ch | seed=0 | MAE=6.7740e+00 | t=0.8442s
    trss | MR=1ch | seed=0 | MAE=7.6770e+00 | t=0.3404s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.7887e+02 | t=0.0182s
    temporal_laplacian | MR=1ch | seed=0 | MAE=2.2174e+02 | t=19.4572s
    mean | MR=1ch | seed=1 | MAE=1.0242e+01 | t=0.0030s
    nearest | MR=1ch | seed=1 | MAE=1.6572e+01 | t=0.0043s
    tikhonov | MR=1ch | seed=1 | MAE=9.4607e+01 | t=0.0481s
    tv | MR=1ch | seed=1 | MAE=6.2697e+00 | t=0.5916s
    trss | MR=1ch | seed=1 | MAE=7.4732e+00 | t=0.1792s

Completed: 2026-04-16T14:40:45.015754+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.