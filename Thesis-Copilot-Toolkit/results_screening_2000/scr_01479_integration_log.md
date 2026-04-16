# Integration Log: scr_01479
Started: 2026-04-16T08:53:53.192180+00:00
Description: Screening scr_01479 ds=bci_iv2a_real_s1 graph=knng miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=6.9305e-02 | t=0.1500s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5461e-01 | t=0.0088s
    trss | MR=0.2 | seed=0 | MAE=1.8541e-02 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.6397e-01 | t=2.6351s
    tv | MR=0.2 | seed=1 | MAE=6.8269e-02 | t=0.1483s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5349e-01 | t=0.0096s
    trss | MR=0.2 | seed=1 | MAE=1.8388e-02 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.6375e-01 | t=2.9428s
    tv | MR=0.2 | seed=0 | MAE=6.9312e-02 | t=0.1508s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9106e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.4028e-02 | t=0.0201s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2107e-01 | t=2.6007s

Completed: 2026-04-16T08:53:53.192892+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.