# Integration Log: scr_01181
Started: 2026-04-16T15:12:02.883290+00:00
Description: Screening scr_01181 ds=bci_iv2a_real_s3 graph=aew miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=7.3128e-07 | t=0.3755s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5097e-06 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=3.6818e-07 | t=0.4061s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5319e-06 | t=25.8947s
    tv | MR=0.2 | seed=1 | MAE=7.3452e-07 | t=0.3965s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5058e-06 | t=0.0086s
    trss | MR=0.2 | seed=1 | MAE=3.7758e-07 | t=0.0245s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.5359e-06 | t=21.1423s
    tv | MR=0.2 | seed=0 | MAE=7.3131e-07 | t=0.3593s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6885e-06 | t=0.0167s
    trss | MR=0.2 | seed=0 | MAE=3.9960e-07 | t=0.3821s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.1862e-06 | t=27.9121s

Completed: 2026-04-16T15:12:02.884140+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.