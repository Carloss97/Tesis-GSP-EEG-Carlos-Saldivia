# Integration Log: scr_01371
Started: 2026-04-16T08:40:18.635748+00:00
Description: Screening scr_01371 ds=bci_iv2a_real_s1 graph=knng miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=6.9305e-02 | t=0.1490s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5461e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.8541e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.6397e-01 | t=2.3163s
    tv | MR=0.2 | seed=1 | MAE=6.8269e-02 | t=0.1493s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5349e-01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=1.8388e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.6375e-01 | t=1.3230s
    tv | MR=0.2 | seed=0 | MAE=6.9312e-02 | t=0.1733s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9106e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=2.4028e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2107e-01 | t=1.2536s

Completed: 2026-04-16T08:40:18.636447+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.