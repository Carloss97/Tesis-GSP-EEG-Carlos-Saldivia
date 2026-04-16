# Integration Log: scr_01106
Started: 2026-04-16T13:47:12.559545+00:00
Description: Screening scr_01106 ds=physionet_real graph=knn miss=[0.1] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1566e-06 | t=0.3502s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.9522e-06 | t=0.0124s
    trss | MR=0.2 | seed=0 | MAE=1.8510e-06 | t=0.1791s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.9030e-05 | t=19.9009s
    tv | MR=0.2 | seed=1 | MAE=5.1672e-06 | t=0.4324s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=7.9369e-06 | t=0.0157s
    trss | MR=0.2 | seed=1 | MAE=1.8855e-06 | t=0.1112s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.9216e-05 | t=6.2662s
    tv | MR=0.2 | seed=0 | MAE=5.1809e-06 | t=0.3070s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0121e-05 | t=0.0086s
    trss | MR=0.2 | seed=0 | MAE=1.9543e-06 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4069e-05 | t=16.9733s

Completed: 2026-04-16T13:47:12.560244+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.