# Integration Log: scr_01298
Started: 2026-04-16T08:31:03.587324+00:00
Description: Screening scr_01298 ds=physionet_real graph=knn miss=[0.3] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=7.2169e-02 | t=0.1416s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0060e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.9443e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7492e-01 | t=1.2790s
    tv | MR=0.2 | seed=1 | MAE=7.1211e-02 | t=0.1421s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0060e-01 | t=0.0084s
    trss | MR=0.2 | seed=1 | MAE=2.8577e-02 | t=0.0203s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7513e-01 | t=1.2794s
    tv | MR=0.2 | seed=0 | MAE=7.4659e-02 | t=0.1399s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2108e-01 | t=0.0084s
    trss | MR=0.2 | seed=0 | MAE=2.9805e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.3742e-01 | t=1.3023s

Completed: 2026-04-16T08:31:03.588046+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.