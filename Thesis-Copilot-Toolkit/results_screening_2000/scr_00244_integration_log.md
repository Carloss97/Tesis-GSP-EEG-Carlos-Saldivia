# Integration Log: scr_00244
Started: 2026-04-16T14:50:20.693569+00:00
Description: Screening scr_00244 ds=bci_iv2a_real_s2 graph=knn miss=3ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k7 built OK
    mean | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.0020s
    nearest | MR=3ch | seed=0 | MAE=5.1829e-07 | t=0.0054s
    tikhonov | MR=3ch | seed=0 | MAE=2.2361e-06 | t=0.0091s
    tv | MR=3ch | seed=0 | MAE=5.2947e-07 | t=0.4724s
    trss | MR=3ch | seed=0 | MAE=4.2371e-07 | t=0.0764s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=5.0244e-06 | t=0.0148s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.5549e-05 | t=29.2578s
    mean | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=4.9473e-07 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=2.2316e-06 | t=0.0114s
    tv | MR=3ch | seed=1 | MAE=5.2912e-07 | t=0.3647s
    trss | MR=3ch | seed=1 | MAE=4.2887e-07 | t=0.0223s

Completed: 2026-04-16T14:50:20.735721+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.