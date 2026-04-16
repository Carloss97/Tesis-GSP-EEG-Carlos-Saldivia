# Integration Log: scr_00064
Started: 2026-04-16T14:44:48.861014+00:00
Description: Screening scr_00064 ds=bci_iv2a_real_s2 graph=kalofolias miss=1ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: kalofolias built OK
    mean | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=1.6572e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=1.7590e-06 | t=0.0087s
    tv | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.8709s
    trss | MR=1ch | seed=0 | MAE=1.1940e-07 | t=0.4779s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.8924e-06 | t=0.0168s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.4557e-05 | t=18.4028s
    mean | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.0021s
    nearest | MR=1ch | seed=1 | MAE=1.6467e-07 | t=0.0021s
    tikhonov | MR=1ch | seed=1 | MAE=1.7614e-06 | t=0.0059s
    tv | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.4418s
    trss | MR=1ch | seed=1 | MAE=1.2046e-07 | t=0.0945s

Completed: 2026-04-16T14:44:48.861912+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.