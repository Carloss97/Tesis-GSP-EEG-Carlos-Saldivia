# Integration Log: scr_01446
Started: 2026-04-16T08:49:58.911368+00:00
Description: Screening scr_01446 ds=iv100hz_mat graph=gaussian miss=[0.4] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=1.0087e-02 | t=0.1861s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5931e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.6321e-03 | t=0.0211s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.0335e-02 | t=1.2285s
    tv | MR=0.2 | seed=1 | MAE=1.0479e-02 | t=0.1864s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.5941e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.5765e-03 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=7.0266e-02 | t=1.3280s
    tv | MR=0.2 | seed=0 | MAE=1.0842e-02 | t=0.1852s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.9243e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=5.0087e-03 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.1136e-02 | t=1.2494s

Completed: 2026-04-16T08:49:58.912241+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.