# Integration Log: it104_noise_sensitivity_tv
Started: 2026-04-09T17:49:19.471915+00:00
Description: Noise sensitivity analysis for TV methods

## Dataset: physionet_eegmmidb_real | rows=112
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1646e-06 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=4.8008e-06 | t=0.0044s
    tikhonov | MR=0.2 | seed=0 | MAE=7.7515e-06 | t=0.0062s
    tv | MR=0.2 | seed=0 | MAE=4.0885e-06 | t=0.1453s
    trss | MR=0.2 | seed=0 | MAE=2.7686e-06 | t=0.0170s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3527e-05 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5455e-05 | t=1.3290s
    mean | MR=0.2 | seed=1 | MAE=4.1469e-06 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=4.7521e-06 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=7.7251e-06 | t=0.0059s
    tv | MR=0.2 | seed=1 | MAE=4.0694e-06 | t=0.1415s
    trss | MR=0.2 | seed=1 | MAE=2.7842e-06 | t=0.0166s

Completed: 2026-04-09T17:49:19.472644+00:00
Total rows: 112
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.