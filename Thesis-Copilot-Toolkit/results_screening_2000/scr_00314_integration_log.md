# Integration Log: scr_00314
Started: 2026-04-16T15:27:47.638782+00:00
Description: Screening scr_00314 ds=physionet_real graph=aew miss=3ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: aew built OK
    mean | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.0031s
    nearest | MR=3ch | seed=0 | MAE=3.5155e-06 | t=0.0345s
    tikhonov | MR=3ch | seed=0 | MAE=5.3390e-06 | t=0.0797s
    tv | MR=3ch | seed=0 | MAE=3.0566e-06 | t=0.9735s
    trss | MR=3ch | seed=0 | MAE=1.4975e-06 | t=0.0693s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.1254e-05 | t=0.0555s
    temporal_laplacian | MR=3ch | seed=0 | MAE=2.8592e-05 | t=26.2819s
    mean | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.0370s
    nearest | MR=3ch | seed=1 | MAE=3.5329e-06 | t=0.0063s
    tikhonov | MR=3ch | seed=1 | MAE=5.3465e-06 | t=0.0088s
    tv | MR=3ch | seed=1 | MAE=3.0655e-06 | t=0.8121s
    trss | MR=3ch | seed=1 | MAE=1.4749e-06 | t=0.2214s

Completed: 2026-04-16T15:27:47.640182+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.