# Integration Log: scr_01695
Started: 2026-04-16T09:23:46.198194+00:00
Description: Screening scr_01695 ds=bci_iv2a_real_s1 graph=knng miss=2ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8408e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.0457e-02 | t=0.1488s
    trss | MR=0.2 | seed=0 | MAE=5.4487e-02 | t=0.0202s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.0930e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.9915e-01 | t=1.2458s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8102e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.9162e-02 | t=0.1496s
    trss | MR=0.2 | seed=1 | MAE=5.4176e-02 | t=0.0208s

Completed: 2026-04-16T09:23:46.198983+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.