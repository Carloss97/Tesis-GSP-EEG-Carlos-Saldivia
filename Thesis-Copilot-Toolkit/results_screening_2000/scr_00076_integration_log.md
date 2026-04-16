# Integration Log: scr_00076
Started: 2026-04-16T14:50:21.942017+00:00
Description: Screening scr_00076 ds=bci_iv2a_real_s2 graph=knng miss=1ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knng built OK
    mean | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.0035s
    nearest | MR=1ch | seed=0 | MAE=1.6572e-07 | t=0.0034s
    tikhonov | MR=1ch | seed=0 | MAE=1.5058e-06 | t=0.0377s
    tv | MR=1ch | seed=0 | MAE=1.7047e-07 | t=0.5864s
    trss | MR=1ch | seed=0 | MAE=1.4393e-07 | t=0.7532s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.6796e-06 | t=0.0126s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.3394e-05 | t=26.5444s
    mean | MR=1ch | seed=1 | MAE=1.7401e-07 | t=0.0032s
    nearest | MR=1ch | seed=1 | MAE=1.6467e-07 | t=0.0042s
    tikhonov | MR=1ch | seed=1 | MAE=1.5052e-06 | t=0.0064s
    tv | MR=1ch | seed=1 | MAE=1.7402e-07 | t=0.1989s
    trss | MR=1ch | seed=1 | MAE=1.4357e-07 | t=0.0171s

Completed: 2026-04-16T14:50:21.946689+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.