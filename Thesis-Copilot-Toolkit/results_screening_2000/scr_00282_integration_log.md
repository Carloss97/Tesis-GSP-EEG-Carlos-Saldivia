# Integration Log: scr_00282
Started: 2026-04-16T15:10:33.558683+00:00
Description: Screening scr_00282 ds=iv100hz_mat graph=kalofolias miss=3ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: kalofolias built OK
    mean | MR=3ch | seed=0 | MAE=3.0766e+01 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=4.8015e+01 | t=0.0074s
    tikhonov | MR=3ch | seed=0 | MAE=1.5415e+02 | t=0.0078s
    tv | MR=3ch | seed=0 | MAE=3.0071e+01 | t=0.2240s
    trss | MR=3ch | seed=0 | MAE=1.1302e+01 | t=0.0188s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.5591e+02 | t=0.0158s
    temporal_laplacian | MR=3ch | seed=0 | MAE=2.8935e+02 | t=25.1067s
    mean | MR=3ch | seed=1 | MAE=3.1144e+01 | t=0.0050s
    nearest | MR=3ch | seed=1 | MAE=4.9179e+01 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=1.5683e+02 | t=0.0112s
    tv | MR=3ch | seed=1 | MAE=3.0631e+01 | t=1.1411s
    trss | MR=3ch | seed=1 | MAE=1.1756e+01 | t=0.2936s

Completed: 2026-04-16T15:10:33.559961+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.