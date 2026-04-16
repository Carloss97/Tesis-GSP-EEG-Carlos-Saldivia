# Integration Log: scr_00303
Started: 2026-04-16T15:21:54.166741+00:00
Description: Screening scr_00303 ds=bci_iv2a_real_s1 graph=vknng miss=3ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: vknng built OK
    mean | MR=3ch | seed=0 | MAE=1.8807e-06 | t=0.0038s
    nearest | MR=3ch | seed=0 | MAE=2.1144e-06 | t=0.0825s
    tikhonov | MR=3ch | seed=0 | MAE=4.2686e-06 | t=0.0231s
    tv | MR=3ch | seed=0 | MAE=1.8806e-06 | t=0.8484s
    trss | MR=3ch | seed=0 | MAE=1.4035e-06 | t=0.5128s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=8.4699e-06 | t=0.0494s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.3098e-05 | t=26.3462s
    mean | MR=3ch | seed=1 | MAE=1.9164e-06 | t=0.0120s
    nearest | MR=3ch | seed=1 | MAE=2.0591e-06 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=4.2862e-06 | t=0.0782s
    tv | MR=3ch | seed=1 | MAE=1.9163e-06 | t=0.5656s
    trss | MR=3ch | seed=1 | MAE=1.4097e-06 | t=0.1081s

Completed: 2026-04-16T15:21:54.170410+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.