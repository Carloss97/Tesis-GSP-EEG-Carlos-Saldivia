# Integration Log: scr_01108
Started: 2026-04-16T13:50:17.743689+00:00
Description: Screening scr_01108 ds=bci_iv2a_real_s2 graph=knn miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7656e-07 | t=0.1646s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1567e-06 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=4.0514e-07 | t=0.0222s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.3842e-06 | t=16.1495s
    tv | MR=0.2 | seed=1 | MAE=9.0517e-07 | t=0.4100s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1961e-06 | t=0.0128s
    trss | MR=0.2 | seed=1 | MAE=4.1073e-07 | t=0.0706s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=8.4067e-06 | t=10.7550s
    tv | MR=0.2 | seed=0 | MAE=8.7647e-07 | t=0.6032s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.4054e-06 | t=0.0135s
    trss | MR=0.2 | seed=0 | MAE=4.5066e-07 | t=0.3032s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0963e-05 | t=2.8871s

Completed: 2026-04-16T13:50:17.744541+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.