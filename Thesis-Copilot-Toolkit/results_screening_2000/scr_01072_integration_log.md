# Integration Log: scr_01072
Started: 2026-04-16T13:20:51.186059+00:00
Description: Screening scr_01072 ds=bci_iv2a_real_s2 graph=aew miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=8.7631e-07 | t=0.3976s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.9807e-06 | t=0.0452s
    trss | MR=0.2 | seed=0 | MAE=4.4648e-07 | t=0.2280s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.0502e-06 | t=17.5629s
    tv | MR=0.2 | seed=1 | MAE=9.0486e-07 | t=0.1722s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.0232e-06 | t=0.0133s
    trss | MR=0.2 | seed=1 | MAE=4.5200e-07 | t=0.2809s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.0840e-06 | t=17.0367s
    tv | MR=0.2 | seed=0 | MAE=8.7634e-07 | t=0.1544s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1076e-06 | t=0.0085s
    trss | MR=0.2 | seed=0 | MAE=4.7795e-07 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.2317e-06 | t=17.1990s

Completed: 2026-04-16T13:20:51.187050+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.