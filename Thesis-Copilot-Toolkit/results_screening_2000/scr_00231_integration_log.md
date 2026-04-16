# Integration Log: scr_00231
Started: 2026-04-16T14:43:20.329131+00:00
Description: Screening scr_00231 ds=bci_iv2a_real_s1 graph=knn miss=3ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k5 built OK
    mean | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.0037s
    nearest | MR=3ch | seed=0 | MAE=2.1144e-06 | t=0.0063s
    tikhonov | MR=3ch | seed=0 | MAE=6.4132e-06 | t=0.0094s
    tv | MR=3ch | seed=0 | MAE=1.8806e-06 | t=0.3775s
    trss | MR=3ch | seed=0 | MAE=1.2860e-06 | t=0.1965s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.1023e-05 | t=0.0081s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.6303e-05 | t=21.2954s
    mean | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=2.0591e-06 | t=0.0053s
    tikhonov | MR=3ch | seed=1 | MAE=6.4145e-06 | t=0.0260s
    tv | MR=3ch | seed=1 | MAE=1.9163e-06 | t=1.3706s
    trss | MR=3ch | seed=1 | MAE=1.3108e-06 | t=0.4699s

Completed: 2026-04-16T14:43:20.330075+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.