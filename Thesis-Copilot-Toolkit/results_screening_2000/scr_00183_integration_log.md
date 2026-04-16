# Integration Log: scr_00183
Started: 2026-04-16T14:18:40.418299+00:00
Description: Screening scr_00183 ds=bci_iv2a_real_s1 graph=knng miss=2ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knng built OK
    mean | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.0021s
    nearest | MR=2ch | seed=0 | MAE=1.3708e-06 | t=0.0027s
    tikhonov | MR=2ch | seed=0 | MAE=5.4259e-06 | t=0.0080s
    tv | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.2750s
    trss | MR=2ch | seed=0 | MAE=9.5392e-07 | t=0.5488s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.0216e-05 | t=0.0241s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.5353e-05 | t=26.7688s
    mean | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.0021s
    nearest | MR=2ch | seed=1 | MAE=1.2545e-06 | t=0.0045s
    tikhonov | MR=2ch | seed=1 | MAE=5.3746e-06 | t=0.0059s
    tv | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.2420s
    trss | MR=2ch | seed=1 | MAE=8.8079e-07 | t=0.2266s

Completed: 2026-04-16T14:18:40.419170+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.