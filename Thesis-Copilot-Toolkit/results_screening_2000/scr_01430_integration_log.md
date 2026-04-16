# Integration Log: scr_01430
Started: 2026-04-16T08:47:31.638643+00:00
Description: Screening scr_01430 ds=physionet_real graph=knn miss=[0.4] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=7.7262e-02 | t=0.1618s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4192e-01 | t=0.0086s
    trss | MR=0.2 | seed=0 | MAE=3.0118e-02 | t=0.0208s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4981e-01 | t=1.3645s
    tv | MR=0.2 | seed=1 | MAE=7.6552e-02 | t=0.1564s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.4113e-01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=2.8945e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.4987e-01 | t=1.2517s
    tv | MR=0.2 | seed=0 | MAE=7.7635e-02 | t=0.1592s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8396e-01 | t=0.0091s
    trss | MR=0.2 | seed=0 | MAE=3.1091e-02 | t=0.0207s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4754e-01 | t=1.2613s

Completed: 2026-04-16T08:47:31.639483+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.