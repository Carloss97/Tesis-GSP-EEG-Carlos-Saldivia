# Integration Log: scr_01251
Started: 2026-04-16T08:25:20.632150+00:00
Description: Screening scr_01251 ds=bci_iv2a_real_s1 graph=kalofolias miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: kalofolias built OK
    tv | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.1873s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6709e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.6709e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8401e-01 | t=1.3262s
    tv | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.2121s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.6509e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.6476e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.8351e-01 | t=1.2380s
    tv | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.1852s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.1437e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.1741e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.5584e-01 | t=1.2697s

Completed: 2026-04-16T08:25:20.632862+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.