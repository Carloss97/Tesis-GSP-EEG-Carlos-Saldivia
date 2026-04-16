# Integration Log: scr_01118
Started: 2026-04-16T13:57:33.023292+00:00
Description: Screening scr_01118 ds=physionet_real graph=gaussian miss=[0.1] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.5341s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5482e-05 | t=0.0738s
    trss | MR=0.2 | seed=0 | MAE=2.1605e-06 | t=0.0466s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7202e-05 | t=9.6683s
    tv | MR=0.2 | seed=1 | MAE=5.2167e-06 | t=0.2023s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5499e-05 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=2.2244e-06 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7316e-05 | t=18.7209s
    tv | MR=0.2 | seed=0 | MAE=5.2058e-06 | t=0.3512s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8356e-05 | t=0.0089s
    trss | MR=0.2 | seed=0 | MAE=2.3869e-06 | t=0.0226s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2305e-05 | t=17.4161s

Completed: 2026-04-16T13:57:33.024240+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.