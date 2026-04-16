# Integration Log: scr_00806
Started: 2026-04-16T11:59:02.886820+00:00
Description: Screening scr_00806 ds=physionet_real graph=gaussian miss=1ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.1892s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5393e-05 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=2.1567e-06 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7080e-05 | t=2.7698s
    tv | MR=0.2 | seed=1 | MAE=5.2167e-06 | t=0.1881s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5410e-05 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=2.2202e-06 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7195e-05 | t=2.6992s
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.1916s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8283e-05 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=2.3815e-06 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2204e-05 | t=2.7127s

Completed: 2026-04-16T11:59:02.887665+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.