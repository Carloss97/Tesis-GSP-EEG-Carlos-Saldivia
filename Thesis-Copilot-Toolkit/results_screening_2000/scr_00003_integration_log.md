# Integration Log: scr_00003
Started: 2026-04-16T15:15:48.706655+00:00
Description: Screening scr_00003 ds=bci_iv2a_real_s1 graph=knn miss=1ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=6.8694e-07 | t=0.0032s
    nearest | MR=1ch | seed=0 | MAE=6.7972e-07 | t=0.0368s
    tikhonov | MR=1ch | seed=0 | MAE=4.1065e-06 | t=0.0086s
    tv | MR=1ch | seed=0 | MAE=6.8690e-07 | t=0.5158s
    trss | MR=1ch | seed=0 | MAE=4.6482e-07 | t=0.2326s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=9.0544e-06 | t=0.0124s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.4005e-05 | t=28.7074s
    mean | MR=1ch | seed=1 | MAE=6.0230e-07 | t=0.0031s
    nearest | MR=1ch | seed=1 | MAE=6.3859e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=4.0543e-06 | t=0.0654s
    tv | MR=1ch | seed=1 | MAE=6.0227e-07 | t=0.9360s
    trss | MR=1ch | seed=1 | MAE=4.0693e-07 | t=0.8259s

Completed: 2026-04-16T15:15:48.707567+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.