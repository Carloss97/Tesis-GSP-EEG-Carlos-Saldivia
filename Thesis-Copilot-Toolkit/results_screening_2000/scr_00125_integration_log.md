# Integration Log: scr_00125
Started: 2026-04-16T15:14:41.398125+00:00
Description: Screening scr_00125 ds=bci_iv2a_real_s3 graph=knn miss=2ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k5 built OK
    mean | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.0536s
    nearest | MR=2ch | seed=0 | MAE=2.4876e-07 | t=0.0046s
    tikhonov | MR=2ch | seed=0 | MAE=1.6053e-06 | t=0.0301s
    tv | MR=2ch | seed=0 | MAE=3.0422e-07 | t=0.3432s
    trss | MR=2ch | seed=0 | MAE=2.6523e-07 | t=0.1251s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.7461e-06 | t=0.0402s
    temporal_laplacian | MR=2ch | seed=0 | MAE=5.5097e-06 | t=25.1967s
    mean | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=2.5230e-07 | t=0.1356s
    tikhonov | MR=2ch | seed=1 | MAE=1.5892e-06 | t=0.0114s
    tv | MR=2ch | seed=1 | MAE=2.8474e-07 | t=0.6255s
    trss | MR=2ch | seed=1 | MAE=2.5138e-07 | t=0.8335s

Completed: 2026-04-16T15:14:41.399186+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.