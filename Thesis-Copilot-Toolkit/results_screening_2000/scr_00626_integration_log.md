# Integration Log: scr_00626
Started: 2026-04-16T14:47:46.536399+00:00
Description: Screening scr_00626 ds=physionet_real graph=vknng miss=[0.3] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: vknng built OK
    mean | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=8.1341e-06 | t=0.0273s
    tikhonov | MR=0.3 | seed=0 | MAE=8.1466e-06 | t=0.0101s
    tv | MR=0.3 | seed=0 | MAE=7.0828e-06 | t=0.4323s
    trss | MR=0.3 | seed=0 | MAE=3.7979e-06 | t=0.1345s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.3567e-05 | t=0.0135s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=3.2260e-05 | t=25.9153s
    mean | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.0388s
    nearest | MR=0.3 | seed=1 | MAE=8.0659e-06 | t=0.0121s
    tikhonov | MR=0.3 | seed=1 | MAE=8.2278e-06 | t=0.0402s
    tv | MR=0.3 | seed=1 | MAE=7.2418e-06 | t=0.9333s
    trss | MR=0.3 | seed=1 | MAE=3.8429e-06 | t=0.5082s

Completed: 2026-04-16T14:47:46.537265+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.