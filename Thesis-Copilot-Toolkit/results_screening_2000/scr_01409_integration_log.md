# Integration Log: scr_01409
Started: 2026-04-16T08:45:16.265726+00:00
Description: Screening scr_01409 ds=bci_iv2a_real_s3 graph=knn miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=6.5832e-02 | t=0.1460s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6397e-01 | t=0.0091s
    trss | MR=0.2 | seed=0 | MAE=3.5502e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.6503e-01 | t=3.2347s
    tv | MR=0.2 | seed=1 | MAE=6.8932e-02 | t=0.1545s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.6593e-01 | t=0.0091s
    trss | MR=0.2 | seed=1 | MAE=3.6263e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.6435e-01 | t=2.9100s
    tv | MR=0.2 | seed=0 | MAE=6.5824e-02 | t=0.1493s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8949e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.7946e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.3607e-01 | t=3.0287s

Completed: 2026-04-16T08:45:16.266482+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.