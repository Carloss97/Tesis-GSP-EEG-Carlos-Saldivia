# Integration Log: scr_00102
Started: 2026-04-16T15:03:58.303676+00:00
Description: Screening scr_00102 ds=iv100hz_mat graph=aew miss=1ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: aew built OK
    mean | MR=1ch | seed=0 | MAE=1.1091e+01 | t=0.0032s
    nearest | MR=1ch | seed=0 | MAE=1.6962e+01 | t=0.0034s
    tikhonov | MR=1ch | seed=0 | MAE=6.7502e+01 | t=0.0088s
    tv | MR=1ch | seed=0 | MAE=7.6128e+00 | t=1.4144s
    trss | MR=1ch | seed=0 | MAE=7.3095e+00 | t=0.5661s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.4712e+02 | t=0.0189s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.8431e+02 | t=14.0244s
    mean | MR=1ch | seed=1 | MAE=1.0242e+01 | t=0.0024s
    nearest | MR=1ch | seed=1 | MAE=1.6572e+01 | t=0.0021s
    tikhonov | MR=1ch | seed=1 | MAE=6.7360e+01 | t=0.0061s
    tv | MR=1ch | seed=1 | MAE=7.0670e+00 | t=0.2310s
    trss | MR=1ch | seed=1 | MAE=7.1959e+00 | t=0.8425s

Completed: 2026-04-16T15:03:58.304774+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.