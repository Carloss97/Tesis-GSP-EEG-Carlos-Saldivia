# Integration Log: scr_00867
Started: 2026-04-16T12:07:01.120791+00:00
Description: Screening scr_00867 ds=bci_iv2a_real_s1 graph=knn miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0347e-06 | t=0.1485s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.0523e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=8.1913e-07 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.2028e-06 | t=1.2446s
    tv | MR=0.2 | seed=1 | MAE=3.3724e-06 | t=0.1459s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.3176e-06 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=1.0218e-06 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.3894e-06 | t=1.2646s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.1470s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.1521e-06 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.0348e-06 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0450e-05 | t=1.3610s

Completed: 2026-04-16T12:07:01.121629+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.