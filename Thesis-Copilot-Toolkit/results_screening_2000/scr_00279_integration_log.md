# Integration Log: scr_00279
Started: 2026-04-16T15:07:51.447708+00:00
Description: Screening scr_00279 ds=bci_iv2a_real_s1 graph=kalofolias miss=3ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: kalofolias built OK
    mean | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.0032s
    nearest | MR=3ch | seed=0 | MAE=2.1144e-06 | t=0.0240s
    tikhonov | MR=3ch | seed=0 | MAE=6.9711e-06 | t=0.0088s
    tv | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.2027s
    trss | MR=3ch | seed=0 | MAE=1.2875e-06 | t=0.0190s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.1567e-05 | t=0.0083s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.6776e-05 | t=28.3614s
    mean | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=2.0591e-06 | t=0.0054s
    tikhonov | MR=3ch | seed=1 | MAE=6.9592e-06 | t=0.0088s
    tv | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.2905s
    trss | MR=3ch | seed=1 | MAE=1.2990e-06 | t=0.0175s

Completed: 2026-04-16T15:07:51.448760+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.