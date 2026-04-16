# Integration Log: scr_01145
Started: 2026-04-16T14:26:26.368221+00:00
Description: Screening scr_01145 ds=bci_iv2a_real_s3 graph=kalofolias miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: kalofolias built OK
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.3268s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6484e-06 | t=0.0135s
    trss | MR=0.2 | seed=0 | MAE=3.1698e-07 | t=0.2545s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8155e-06 | t=22.1048s
    tv | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.1910s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.6466e-06 | t=0.0161s
    trss | MR=0.2 | seed=1 | MAE=3.3128e-07 | t=0.0226s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.8300e-06 | t=26.4932s
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.4444s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9989e-06 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=3.4582e-07 | t=0.0207s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7357e-06 | t=25.2321s

Completed: 2026-04-16T14:26:26.369084+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.