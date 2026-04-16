# Integration Log: scr_01263
Started: 2026-04-16T08:26:50.814859+00:00
Description: Screening scr_01263 ds=bci_iv2a_real_s1 graph=knng miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=6.9305e-02 | t=0.1511s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5461e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.8541e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.6397e-01 | t=1.4409s
    tv | MR=0.2 | seed=1 | MAE=6.8269e-02 | t=0.1521s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5349e-01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=1.8388e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.6375e-01 | t=1.2966s
    tv | MR=0.2 | seed=0 | MAE=6.9312e-02 | t=0.1486s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9106e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=2.4028e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2107e-01 | t=1.3277s

Completed: 2026-04-16T08:26:50.815677+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.