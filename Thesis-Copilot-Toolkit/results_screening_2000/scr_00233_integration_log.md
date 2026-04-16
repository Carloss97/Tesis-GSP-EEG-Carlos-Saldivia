# Integration Log: scr_00233
Started: 2026-04-16T14:45:13.167718+00:00
Description: Screening scr_00233 ds=bci_iv2a_real_s3 graph=knn miss=3ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k5 built OK
    mean | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=4.0021e-07 | t=0.0036s
    tikhonov | MR=3ch | seed=0 | MAE=1.6921e-06 | t=0.0063s
    tv | MR=3ch | seed=0 | MAE=4.5069e-07 | t=0.1624s
    trss | MR=3ch | seed=0 | MAE=3.8389e-07 | t=0.1775s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.7812e-06 | t=0.0132s
    temporal_laplacian | MR=3ch | seed=0 | MAE=5.5727e-06 | t=23.8021s
    mean | MR=3ch | seed=1 | MAE=4.4119e-07 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=3.7573e-07 | t=0.0432s
    tikhonov | MR=3ch | seed=1 | MAE=1.6882e-06 | t=0.0181s
    tv | MR=3ch | seed=1 | MAE=4.4121e-07 | t=0.9876s
    trss | MR=3ch | seed=1 | MAE=3.7826e-07 | t=0.6106s

Completed: 2026-04-16T14:45:13.168612+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.