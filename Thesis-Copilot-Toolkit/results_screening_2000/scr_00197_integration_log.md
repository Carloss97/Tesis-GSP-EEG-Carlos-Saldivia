# Integration Log: scr_00197
Started: 2026-04-16T14:26:44.720332+00:00
Description: Screening scr_00197 ds=bci_iv2a_real_s3 graph=vknng miss=2ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: vknng built OK
    mean | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.0032s
    nearest | MR=2ch | seed=0 | MAE=2.4876e-07 | t=0.0208s
    tikhonov | MR=2ch | seed=0 | MAE=9.9585e-07 | t=0.0114s
    tv | MR=2ch | seed=0 | MAE=3.0422e-07 | t=0.4033s
    trss | MR=2ch | seed=0 | MAE=2.8468e-07 | t=0.3879s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.1139e-06 | t=0.0140s
    temporal_laplacian | MR=2ch | seed=0 | MAE=4.1087e-06 | t=27.7830s
    mean | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.0031s
    nearest | MR=2ch | seed=1 | MAE=2.5230e-07 | t=0.0043s
    tikhonov | MR=2ch | seed=1 | MAE=9.7938e-07 | t=0.0090s
    tv | MR=2ch | seed=1 | MAE=2.8474e-07 | t=0.5030s
    trss | MR=2ch | seed=1 | MAE=2.7221e-07 | t=0.2188s

Completed: 2026-04-16T14:26:44.721229+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.