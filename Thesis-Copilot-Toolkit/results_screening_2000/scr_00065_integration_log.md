# Integration Log: scr_00065
Started: 2026-04-16T14:45:46.196694+00:00
Description: Screening scr_00065 ds=bci_iv2a_real_s3 graph=kalofolias miss=1ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: kalofolias built OK
    mean | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.0030s
    nearest | MR=1ch | seed=0 | MAE=1.2148e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=1.4859e-06 | t=0.0089s
    tv | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.4421s
    trss | MR=1ch | seed=0 | MAE=1.0862e-07 | t=0.4365s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.7631e-06 | t=0.0355s
    temporal_laplacian | MR=1ch | seed=0 | MAE=5.5141e-06 | t=20.9970s
    mean | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.0034s
    nearest | MR=1ch | seed=1 | MAE=1.2335e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=1.4827e-06 | t=0.0088s
    tv | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.4215s
    trss | MR=1ch | seed=1 | MAE=1.0668e-07 | t=0.0971s

Completed: 2026-04-16T14:45:46.197667+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.