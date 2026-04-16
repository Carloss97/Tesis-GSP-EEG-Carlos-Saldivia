# Integration Log: scr_00270
Started: 2026-04-16T15:04:27.277472+00:00
Description: Screening scr_00270 ds=iv100hz_mat graph=gaussian miss=3ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=3ch | seed=0 | MAE=3.0766e+01 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=4.8015e+01 | t=0.0054s
    tikhonov | MR=3ch | seed=0 | MAE=1.0880e+02 | t=0.0090s
    tv | MR=3ch | seed=0 | MAE=1.9134e+01 | t=0.4081s
    trss | MR=3ch | seed=0 | MAE=2.3121e+01 | t=0.0183s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.8453e+02 | t=0.0105s
    temporal_laplacian | MR=3ch | seed=0 | MAE=2.2779e+02 | t=24.0888s
    mean | MR=3ch | seed=1 | MAE=3.1144e+01 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=4.9179e+01 | t=0.0061s
    tikhonov | MR=3ch | seed=1 | MAE=1.0868e+02 | t=0.0126s
    tv | MR=3ch | seed=1 | MAE=1.9028e+01 | t=0.5836s
    trss | MR=3ch | seed=1 | MAE=2.3218e+01 | t=0.3815s

Completed: 2026-04-16T15:04:27.278512+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.