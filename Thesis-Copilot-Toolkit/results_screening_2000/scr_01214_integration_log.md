# Integration Log: scr_01214
Started: 2026-04-16T08:20:35.201712+00:00
Description: Screening scr_01214 ds=physionet_real graph=knn miss=[0.2] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=7.7262e-02 | t=0.1525s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4192e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.0118e-02 | t=0.0181s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4981e-01 | t=1.2680s
    tv | MR=0.2 | seed=1 | MAE=7.6552e-02 | t=0.1532s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.4113e-01 | t=0.0084s
    trss | MR=0.2 | seed=1 | MAE=2.8945e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.4987e-01 | t=1.2803s
    tv | MR=0.2 | seed=0 | MAE=7.7635e-02 | t=0.1518s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8396e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=3.1091e-02 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4754e-01 | t=1.3209s

Completed: 2026-04-16T08:20:35.202404+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.