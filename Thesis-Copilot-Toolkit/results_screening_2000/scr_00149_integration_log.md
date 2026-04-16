# Integration Log: scr_00149
Started: 2026-04-16T15:29:03.120023+00:00
Description: Screening scr_00149 ds=bci_iv2a_real_s3 graph=gaussian miss=2ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.0356s
    nearest | MR=2ch | seed=0 | MAE=2.4876e-07 | t=0.0094s
    tikhonov | MR=2ch | seed=0 | MAE=2.4703e-06 | t=0.0117s
    tv | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.7494s
    trss | MR=2ch | seed=0 | MAE=2.1652e-07 | t=0.5756s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=3.2163e-06 | t=0.0167s
    temporal_laplacian | MR=2ch | seed=0 | MAE=6.4614e-06 | t=30.5342s
    mean | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.0038s
    nearest | MR=2ch | seed=1 | MAE=2.5230e-07 | t=0.0052s
    tikhonov | MR=2ch | seed=1 | MAE=2.4663e-06 | t=0.0101s
    tv | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.8002s
    trss | MR=2ch | seed=1 | MAE=2.0313e-07 | t=0.4725s

Completed: 2026-04-16T15:29:03.140139+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.