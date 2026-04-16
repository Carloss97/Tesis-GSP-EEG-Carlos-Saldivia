# Integration Log: scr_00039
Started: 2026-04-16T15:34:49.629104+00:00
Description: Screening scr_00039 ds=bci_iv2a_real_s1 graph=gaussian miss=1ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=1ch | seed=0 | MAE=6.8694e-07 | t=0.0072s
    nearest | MR=1ch | seed=0 | MAE=6.7972e-07 | t=0.0288s
    tikhonov | MR=1ch | seed=0 | MAE=1.0012e-05 | t=0.0094s
    tv | MR=1ch | seed=0 | MAE=6.8694e-07 | t=0.8618s
    trss | MR=1ch | seed=0 | MAE=4.5228e-07 | t=0.0561s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.3003e-05 | t=0.0424s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.8860e-05 | t=17.4343s
    mean | MR=1ch | seed=1 | MAE=6.0230e-07 | t=0.0031s
    nearest | MR=1ch | seed=1 | MAE=6.3859e-07 | t=0.0037s
    tikhonov | MR=1ch | seed=1 | MAE=1.0032e-05 | t=0.0619s
    tv | MR=1ch | seed=1 | MAE=6.0230e-07 | t=1.0931s
    trss | MR=1ch | seed=1 | MAE=3.9143e-07 | t=0.0424s

Completed: 2026-04-16T15:34:49.630004+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.