# Integration Log: scr_01803
Started: 2026-04-16T09:39:02.486933+00:00
Description: Screening scr_01803 ds=bci_iv2a_real_s1 graph=knng miss=3ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8408e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=7.0457e-02 | t=0.1531s
    trss | MR=0.2 | seed=0 | MAE=5.4487e-02 | t=0.0203s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.0930e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.9915e-01 | t=1.2997s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8102e-01 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=6.9162e-02 | t=0.1488s
    trss | MR=0.2 | seed=1 | MAE=5.4176e-02 | t=0.0208s

Completed: 2026-04-16T09:39:02.487801+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.