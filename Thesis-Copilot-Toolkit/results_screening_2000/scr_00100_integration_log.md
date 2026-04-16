# Integration Log: scr_00100
Started: 2026-04-16T15:02:24.390329+00:00
Description: Screening scr_00100 ds=bci_iv2a_real_s2 graph=aew miss=1ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: aew built OK
    mean | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.0044s
    nearest | MR=1ch | seed=0 | MAE=1.6572e-07 | t=0.0022s
    tikhonov | MR=1ch | seed=0 | MAE=1.3649e-06 | t=0.0072s
    tv | MR=1ch | seed=0 | MAE=1.7046e-07 | t=0.1988s
    trss | MR=1ch | seed=0 | MAE=1.4329e-07 | t=0.0168s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.5431e-06 | t=0.0088s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.3012e-05 | t=25.0246s
    mean | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.0128s
    nearest | MR=1ch | seed=1 | MAE=1.6467e-07 | t=0.0032s
    tikhonov | MR=1ch | seed=1 | MAE=1.3651e-06 | t=0.0090s
    tv | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.2093s
    trss | MR=1ch | seed=1 | MAE=1.4295e-07 | t=0.0242s

Completed: 2026-04-16T15:02:24.391474+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.