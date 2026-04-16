# Integration Log: scr_01322
Started: 2026-04-16T08:34:02.106377+00:00
Description: Screening scr_01322 ds=physionet_real graph=knn miss=[0.3] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=7.7262e-02 | t=0.1521s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4192e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.0118e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4981e-01 | t=1.2935s
    tv | MR=0.2 | seed=1 | MAE=7.6552e-02 | t=0.1542s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.4113e-01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=2.8945e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.4987e-01 | t=1.2878s
    tv | MR=0.2 | seed=0 | MAE=7.7635e-02 | t=0.1517s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8396e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.1091e-02 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4754e-01 | t=1.2927s

Completed: 2026-04-16T08:34:02.107301+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.