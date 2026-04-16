# Integration Log: scr_00173
Started: 2026-04-16T15:42:03.215676+00:00
Description: Screening scr_00173 ds=bci_iv2a_real_s3 graph=kalofolias miss=2ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: kalofolias built OK
    mean | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.0035s
    nearest | MR=2ch | seed=0 | MAE=2.4876e-07 | t=0.0045s
    tikhonov | MR=2ch | seed=0 | MAE=1.5765e-06 | t=0.0102s
    tv | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.7976s
    trss | MR=2ch | seed=0 | MAE=2.1652e-07 | t=0.0256s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.7983e-06 | t=0.0332s
    temporal_laplacian | MR=2ch | seed=0 | MAE=5.5764e-06 | t=33.9382s
    mean | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=2.5230e-07 | t=0.0050s
    tikhonov | MR=2ch | seed=1 | MAE=1.5661e-06 | t=0.0100s
    tv | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.9760s
    trss | MR=2ch | seed=1 | MAE=2.0313e-07 | t=0.6048s

Completed: 2026-04-16T15:42:03.218225+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.