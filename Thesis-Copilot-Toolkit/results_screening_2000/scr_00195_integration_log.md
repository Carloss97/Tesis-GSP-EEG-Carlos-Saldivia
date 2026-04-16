# Integration Log: scr_00195
Started: 2026-04-16T14:24:53.913393+00:00
Description: Screening scr_00195 ds=bci_iv2a_real_s1 graph=vknng miss=2ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: vknng built OK
    mean | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.0038s
    nearest | MR=2ch | seed=0 | MAE=1.3708e-06 | t=0.0047s
    tikhonov | MR=2ch | seed=0 | MAE=3.7983e-06 | t=0.0101s
    tv | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.3573s
    trss | MR=2ch | seed=0 | MAE=9.8827e-07 | t=0.1239s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=8.1459e-06 | t=0.0085s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.2740e-05 | t=21.3158s
    mean | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.0030s
    nearest | MR=2ch | seed=1 | MAE=1.2545e-06 | t=0.0042s
    tikhonov | MR=2ch | seed=1 | MAE=3.7340e-06 | t=0.0411s
    tv | MR=2ch | seed=1 | MAE=1.2371e-06 | t=0.4784s
    trss | MR=2ch | seed=1 | MAE=9.0847e-07 | t=0.0182s

Completed: 2026-04-16T14:24:53.914298+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.