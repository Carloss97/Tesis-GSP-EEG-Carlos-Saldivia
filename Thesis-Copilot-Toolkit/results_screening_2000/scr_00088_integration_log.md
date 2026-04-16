# Integration Log: scr_00088
Started: 2026-04-16T14:56:09.763070+00:00
Description: Screening scr_00088 ds=bci_iv2a_real_s2 graph=vknng miss=1ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: vknng built OK
    mean | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.0282s
    nearest | MR=1ch | seed=0 | MAE=1.6572e-07 | t=0.0035s
    tikhonov | MR=1ch | seed=0 | MAE=9.8278e-07 | t=0.0095s
    tv | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.4154s
    trss | MR=1ch | seed=0 | MAE=1.4733e-07 | t=0.3862s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.2846e-06 | t=0.0345s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.0303e-05 | t=9.2454s
    mean | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.0033s
    nearest | MR=1ch | seed=1 | MAE=1.6467e-07 | t=0.0076s
    tikhonov | MR=1ch | seed=1 | MAE=9.8784e-07 | t=0.0088s
    tv | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.9526s
    trss | MR=1ch | seed=1 | MAE=1.4792e-07 | t=1.1379s

Completed: 2026-04-16T14:56:09.764137+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.